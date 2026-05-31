
init -800 python:


    from itertools import product
    import copy
    import inspect
    import functools


    class _m1_class_gallery__GalleryAllPriorCondition(object):
        @staticmethod
        def check(all_prior):
            return all_prior


    class _m1_class_gallery__GalleryArbitraryCondition(object):
        def __init__(self, condition):
            self.condition = condition
        
        def check(self, all_prior):
            return eval(self.condition)


    class _m1_class_gallery__GalleryUnlockCondition(object):
        def __init__(self, images):
            self.images = images
        
        def check(self, all_prior, literal_images):
            for gallery_img in self.images:
                if renpy.seen_image(gallery_img):
                    return True
                else:
                    if not isinstance(gallery_img, tuple):
                        name = tuple(gallery_img.split())
                    else:
                        name = gallery_img
                    for j in literal_images:
                        if j[: len(name)] == name:
                            renpy.game.persistent._seen_images[name] = True
                            return True
                    return False
            return True


    class _m1_class_gallery__GalleryImage(object):
        class _ImageComponent(object):
            def __init__(
            self,
            id,
            name,
            value=None,
            component_type=None,
            available_values=None,
            restrictions=None,
            available_for_interaction=True,
            to_display=False,
            variants=None,
            default_value=None,
            linked_component=None,
        ):
                self.id = id
                self.name = name
                self.value = value
                self.component_type = component_type
                if available_values:
                    self.available_values = available_values
                else:
                    self.available_values = set()
                if restrictions:
                    self.restrictions = restrictions
                else:
                    self.restrictions = defaultdict(dict)
                
                self.available_for_interaction = available_for_interaction
                self.to_display = to_display
                if variants:
                    self.variants = variants
                else:
                    self.variants = defaultdict(set)
                self.default_value = default_value
                self.linked_component = linked_component
            
            def set_restrictions(self, attribute_object):
                variant_restrictions = {
                "if_not": attribute_object.if_not,
                "if_any": attribute_object.if_any,
                "if_all": attribute_object.if_all,
            }
                if attribute_object.variant:
                    variant_name = attribute_object.variant
                else:
                    variant_name = "novariant"
                if variant_name not in self.restrictions:
                    self.restrictions[variant_name] = variant_restrictions
                else:
                    if self.restrictions[variant_name] != variant_restrictions:
                        suffix = 1
                        while (
                        f"{variant_name}_{suffix}" in self.restrictions
                        and self.restrictions[f"{variant_name}_{suffix}"]
                        != variant_restrictions
                    ):
                            suffix += 1
                        self.restrictions[f"{variant_name}_{suffix}"] = variant_restrictions
            
            @staticmethod
            def check_component_restrictions(variant_restrictions, displayed_attributes):
                check_results = []
                if variant_restrictions["if_all"]:
                    for restriction in variant_restrictions["if_all"]:
                        if restriction not in displayed_attributes:
                            check_results.append(False)
                            break
                    else:
                        check_results.append(True)
                else:
                    check_results.append(True)
                
                if variant_restrictions["if_any"]:
                    for restriction in variant_restrictions["if_any"]:
                        if restriction in displayed_attributes:
                            check_results.append(True)
                            break
                    else:
                        check_results.append(False)
                else:
                    check_results.append(True)
                
                if variant_restrictions["if_not"]:
                    for restriction in variant_restrictions["if_not"]:
                        if restriction in displayed_attributes:
                            check_results.append(False)
                            break
                    else:
                        check_results.append(True)
                else:
                    check_results.append(True)
                return check_results
            
            def check_restrictions(
            self, displayed_attributes, conflicts_attributes, changed_attribute=None
        ):
                all_variant_result = []
                for variant_name, variant_restrictions in self.restrictions.items():
                    if any(variant_restrictions.values()):
                        check_results = self.check_component_restrictions(
                        variant_restrictions, displayed_attributes
                    )
                    else:
                        check_results = [True, True, True]
                    all_variant_result.append(check_results)
                
                if changed_attribute:
                    attribute_id, current_value, previous_value = changed_attribute
                else:
                    attribute_id = current_value = previous_value = False
                if any(
                [all(variant_result) for variant_result in all_variant_result]
            ) and self.value not in list(conflicts_attributes):
                    
                    
                    if self.component_type == "group":
                        if attribute_id == self.id:
                            if current_value and previous_value == self.value:
                                self.to_display = True
                                if not self.default_value:
                                    self.available_for_interaction = True
                            else:
                                pass
                        elif current_value is False and previous_value == self.value:
                            pass
                        elif current_value is True and previous_value == self.value:
                            self.to_display = True
                            if not self.default_value:
                                self.available_for_interaction = True
                        else:
                            pass
                    elif attribute_id and current_value is False:
                        pass
                    else:
                        pass
                else:
                    if any([any(variant_result) for variant_result in all_variant_result]):
                        self.available_for_interaction = True
                    else:
                        self.available_for_interaction = False
                    
                    if attribute_id and current_value is True:
                        pass
                    else:
                        self.to_display = False
                        if self.linked_component:
                            self.available_for_interaction = True
                        else:
                            self.available_for_interaction = True
        
        show_properties = None
        
        def __init__(self, gallery, displayables, **properties):
            
            self.gallery = gallery
            
            
            self.conditions = []
            
            
            self.displayables = displayables
            
            
            
            self.transforms = [None] * len(displayables)
            
            self.missing_npc = properties.pop("missing_npc", None)
            self.init_attributes = set()
            (self.show_properties,) = renpy.split_properties(properties, "show_")
            
            self.layered_obj = None
            self.attribute_function = None
            self.image_components = dict()
        
        def check_unlock(self, all_prior):
            """
        Returns True if the image is unlocked.
        """
            literal_images = {
            tuple(k.split('"')[1].split())
            for j in renpy.game.persistent._seen_images
            for k in j
            if len(j) == 1 and '"' in k
        }
            literal_images.update(set(renpy.game.persistent._seen_images))
            for condition in self.conditions:
                if not condition.check(all_prior, literal_images):
                    return False
            
            return True
        
        @property
        def displayable_attributes(self):
            return {
            c_value.value
            for c_value in self.image_components.values()
            if c_value.to_display
        }
        
        @property
        def joined_displayable_attributes(self):
            return " ".join(list(self.displayable_attributes))
        
        def get_pickers_results(self):
            if self.attribute_function:
                if hasattr(self.attribute_function, "attr_pickers"):
                    self._patch_pickers(self.attribute_function.attr_pickers)
                pickers_result = self.attribute_function(self.displayable_attributes)
                for picker_display_value in pickers_result:
                    self.adjust_layers(("picker_display", picker_display_value, None))
            return
        
        def check_displayable_restrictions(self, changed_attr=None):
            conflicts_attributes, discarded_available_values = self.check_conflicts()
            for c_value in self.image_components.values():
                if c_value.component_type != "always":
                    c_value.check_restrictions(
                    self.displayable_attributes, conflicts_attributes, changed_attr
                )
        
        def check_conflicts(self, displayable_attributes=None):
            all_displayed_attributes = set()
            all_discarded_attributes = set()
            if not displayable_attributes:
                displayable_attributes = self.displayable_attributes
            for c_value in self.image_components.values():
                discarded_available_values = set()
                if (
                c_value.component_type == "group"
                and c_value.available_values & displayable_attributes
            ):
                    component_available_values = c_value.available_values
                    if c_value.variants:
                        for k, variant_value in c_value.variants.items():
                            if k in c_value.restrictions:
                                check_results = c_value.check_component_restrictions(
                                c_value.restrictions[k], displayable_attributes
                            )
                                if not all(check_results):
                                    discarded_available_values.update(variant_value)
                    if discarded_available_values:
                        all_discarded_attributes.update(discarded_available_values)
                        component_available_values = (
                        component_available_values - discarded_available_values
                    )
                    all_displayed_attributes.update(component_available_values)
            
            conflicts_attributes = all_displayed_attributes - displayable_attributes
            return conflicts_attributes, all_discarded_attributes
        
        def adjust_layers(self, changed_attribute):
            group_name, current_value, previous_value = changed_attribute
            if (current_value or previous_value) and not all(
            [
                isinstance(attr_value, bool)
                for attr_value in [current_value, previous_value]
            ]
        ):
                
                
                for c_value in self.image_components.values():
                    conflicts_attributes, discarded_available_values = self.check_conflicts(
                    {current_value}
                )
                    
                    if c_value.component_type == "always":
                        continue
                    if c_value.component_type == "standalone":
                        continue
                    
                    if current_value in c_value.available_values:
                        
                        c_value.value = current_value
                        if c_value.id == group_name and not c_value.to_display:
                            c_value.to_display = True
                    
                    elif (
                    c_value.value == previous_value
                    and current_value not in c_value.available_values
                ):
                        if isinstance(current_value, bool) and c_value.id == group_name:
                            c_value.to_display = current_value
                        elif isinstance(current_value, bool):
                            continue
                        else:
                            
                            if c_value.default_value:
                                c_value.value = c_value.default_value
                                continue
                            
                            for attr in self.displayable_attributes - {previous_value}:
                                if attr in c_value.available_values:
                                    c_value.value = attr
                                    break
                            
                            c_value.to_display = False
                    
                    elif c_value.value in list(conflicts_attributes):
                        c_value.to_display = False
        
        def show(
        self,
        locked,
        index,
        count,
        show_cg_options,
        changed_attr,
        page_number,
        current_shown_bg,
    ):
            """
        Shows this image when it's unlocked.
        """
            
            renpy.transition(self.gallery.transition)
            ui.saybehavior()
            
            if len(self.displayables) != 1:
                raise
            else:
                displayable = self.displayables[0]
                if not self.layered_obj:
                    self.layered_obj = renpy.get_registered_image(displayable)
                    self.parse_layered_image()
                    self.check_displayable_restrictions()
                    if self.missing_npc:
                        init_display_values = (
                        self.displayable_attributes
                        | {self.missing_npc}
                        | self.init_attributes
                    )
                    else:
                        init_display_values = (
                        self.displayable_attributes | self.init_attributes
                    )
                    for init_display_value in init_display_values:
                        self.adjust_layers(("init_display", init_display_value, None))
                else:
                    if changed_attr:
                        self.adjust_layers(changed_attr)
                    self.check_displayable_restrictions(changed_attr)
                    self.get_pickers_results()
                displayable = f"{displayable} {self.joined_displayable_attributes}"
                displayable = renpy.display.layout.AdjustTimes(
                config.default_transform(displayable), None, None
            )
            if current_shown_bg:
                renpy.scene()
                renpy.show(current_shown_bg)
            else:
                renpy.scene()
                renpy.show("bg black")
            renpy.show_screen(
            self.gallery.image_screen,
            _layer="gallery",
            locked=locked,
            displayable=displayable,
            gallery=self.gallery,
            **self.show_properties,
        )
            if show_cg_options:
                renpy.hide_screen("hidden_cg_options", layer="gallery")
                renpy.show_screen(
                "cg_options",
                _layer="gallery",
                layered_obj=self.layered_obj,
                image_components=self.image_components,
                page_number=page_number,
                current_bg=current_shown_bg,
            )
            else:
                renpy.hide_screen("cg_options", layer="gallery")
                renpy.show_screen("hidden_cg_options", _layer="gallery")
            return ui.interact()
        
        @staticmethod
        def _patch_pickers(pickers):
            from unittest.mock import patch
            
            pickers_to_patch = {
            NPCPicker,
            DickPicker,
            XrayPicker,
            MCGenderPicker,
            RoomPicker,
            MCPicker,
        }
            patched_pickers = []
            for picker in pickers:
                if hasattr(picker, "__mro__"):
                    mro = set(inspect.getmro(picker))
                else:
                    mro = set(inspect.getmro(picker.__class__))
                if mro & pickers_to_patch:
                    store.ORIGINAL_PATCHED_VALUES[picker] = picker.__call__
                    patched = patch.object(picker, "__call__", return_value=set())
                    patched_pickers.append(patched)
                    patched.start()
            return
        
        def _init_image_component(self, layer_object, component_id, component_attribute):
            if layer_object.variant:
                self.image_components[component_id].variants[layer_object.variant].add(
                component_attribute
            )
                self.image_components[component_id].available_values.discard(
                f"{layer_object.variant}_{component_attribute}"
            )
            if component_attribute in self.init_attributes:
                if self.image_components[component_id].value != component_attribute:
                    self.image_components[component_id].value = component_attribute
                    self.image_components[component_id].to_display = True
            self.image_components[component_id].available_values.add(component_attribute)
            self.image_components[component_id].set_restrictions(layer_object)
        
        def parse_layered_image(self):
            all_default_attribute = {
            layer_attribute.attribute
            for layer_attribute in self.layered_obj.attributes
            if layer_attribute.default
        }
            
            if (
            hasattr(self.layered_obj, "attribute_function")
            and self.layered_obj.attribute_function
        ):
                if self.missing_npc:
                    extra_attribute = {self.missing_npc}
                else:
                    extra_attribute = set()
                self.init_attributes.update(
                self.layered_obj.attribute_function(extra_attribute)
            )
                self.attribute_function = self.layered_obj.attribute_function
                if hasattr(self.attribute_function, "attr_pickers"):
                    self._patch_pickers(self.attribute_function.attr_pickers)
            
            for layer_object in self.layered_obj.layers:
                if isinstance(layer_object, store.layeredimage.Always):
                    
                    always_img_name = layer_object.image.name[0]
                    component_id = f"{always_img_name}_always"
                    self.image_components[component_id] = self._ImageComponent(
                    component_id, always_img_name, available_values={always_img_name}
                )
                elif isinstance(layer_object, store.layeredimage.ConditionGroup):
                    
                    continue
                elif layer_object.group or self.layered_obj.attribute_to_groups.get(
                layer_object.attribute
            ):
                    
                    if layer_object.group:
                        component_groups = [layer_object.group]
                    elif self.layered_obj.attribute_to_groups.get(layer_object.attribute):
                        component_groups = self.layered_obj.attribute_to_groups.get(
                        layer_object.attribute
                    )
                    else:
                        raise
                    for component_group in component_groups:
                        component_attribute = layer_object.attribute
                        component_id = f"{component_group}_group"
                        if component_id in self.image_components:
                            self._init_image_component(
                            layer_object, component_id, component_attribute
                        )
                        else:
                            
                            linked_component = None
                            if self.image_components.get(f"{component_group}_standalone"):
                                linked_component = f"{component_group}_standalone"
                                self.image_components[
                                linked_component
                            ].linked_component = component_id
                                available_for_interaction = True
                            else:
                                available_for_interaction = False
                            
                            if (
                            layer_object.default
                            or component_attribute in all_default_attribute
                        ):
                                self.image_components[component_id] = self._ImageComponent(
                                component_id,
                                component_group,
                                value=component_attribute,
                                component_type="group",
                                available_values={component_attribute},
                                available_for_interaction=available_for_interaction,
                                to_display=True,
                                default_value=component_attribute,
                                linked_component=linked_component,
                            )
                            elif component_attribute in self.init_attributes:
                                self.image_components[component_id] = self._ImageComponent(
                                component_id,
                                component_group,
                                value=component_attribute,
                                component_type="group",
                                available_values={component_attribute},
                                available_for_interaction=available_for_interaction,
                                to_display=True,
                                linked_component=linked_component,
                            )
                            else:
                                self.image_components[component_id] = self._ImageComponent(
                                component_id,
                                component_group,
                                value=component_attribute,
                                component_type="group",
                                available_values={component_attribute},
                                available_for_interaction=available_for_interaction,
                                linked_component=linked_component,
                            )
                            if layer_object.variant:
                                self.image_components[component_id].variants[
                                layer_object.variant
                            ].add(component_attribute)
                            self.image_components[component_id].set_restrictions(
                            layer_object
                        )
                
                else:
                    component_attribute = layer_object.attribute
                    
                    component_id = f"{component_attribute}_standalone"
                    if component_id in self.image_components:
                        self._init_image_component(
                        layer_object, component_id, component_attribute
                    )
                    else:
                        
                        linked_component = None
                        if self.image_components.get(f"{component_id}_group"):
                            linked_component = f"{component_id}_group"
                            self.image_components[
                            linked_component
                        ].linked_component = component_id
                            available_for_interaction = True
                        else:
                            available_for_interaction = False
                        
                        if layer_object.default:
                            self.image_components[component_id] = self._ImageComponent(
                            component_id,
                            component_attribute,
                            value=component_attribute,
                            component_type="standalone",
                            available_values={component_attribute},
                            available_for_interaction=available_for_interaction,
                            to_display=True,
                            default_value=component_attribute,
                            linked_component=linked_component,
                        )
                        elif component_attribute in self.init_attributes:
                            self.image_components[component_id] = self._ImageComponent(
                            component_id,
                            component_attribute,
                            value=component_attribute,
                            component_type="standalone",
                            available_values={component_attribute},
                            available_for_interaction=available_for_interaction,
                            to_display=True,
                            linked_component=linked_component,
                        )
                        else:
                            self.image_components[component_id] = self._ImageComponent(
                            component_id,
                            component_attribute,
                            value=component_attribute,
                            component_type="standalone",
                            available_values={component_attribute},
                            available_for_interaction=available_for_interaction,
                            linked_component=linked_component,
                        )
                        if layer_object.variant:
                            self.image_components[component_id].variants[
                            layer_object.variant
                        ].add(component_attribute)
                        self.image_components[component_id].set_restrictions(layer_object)
            
            self.cleanup()
            self.image_components = dict(sorted(self.image_components.items()))
            return
        
        def cleanup(self):
            
            groups_values = defaultdict(set)
            for c_value in list(self.image_components.values()):
                if c_value.variants:
                    variant_values = defaultdict(set)
                    for k, variant_value in c_value.variants.items():
                        for p in product(k, variant_value):
                            variant_values["_".join(p)].add(p)
                    for joined_variant, parts in variant_values.items():
                        if len(parts) > 1:
                            longest_variant = max([p[0] for p in parts], key=len)
                            smallest_attribute = min([p[1] for p in parts], key=len)
                            if f"{longest_variant}_{smallest_attribute}" == joined_variant:
                                for av in list(c_value.available_values):
                                    if (
                                    av in [p[1] for p in parts]
                                    and av != smallest_attribute
                                ):
                                        c_value.available_values.discard(av)
                    for j in c_value.variants:
                        
                        for k in copy.copy(c_value.available_values):
                            if k.startswith(j):
                                stripped_attr = k.replace(f"{j}_", "")
                                c_value.available_values.discard(k)
                                c_value.available_values.add(stripped_attr)
                        
                        if c_value.value.startswith(j):
                            stripped_attr = c_value.value.replace(f"{j}_", "")
                            c_value.value = stripped_attr
                        
                        for component_id, component in list(self.image_components.items()):
                            if component.name == f"{j}_{c_value.name}":
                                self.image_components.pop(component_id)
                
                for available_value in c_value.available_values:
                    groups_values[f"{c_value.name}_{available_value}"].add(
                    (c_value.name, available_value)
                )
                for k, variant_value in groups_values.items():
                    if len(variant_value) > 1:
                        smallest_key = None
                        longest_value = None
                        for group_name, attribute_name in variant_value:
                            if not smallest_key or (len(group_name) < len(smallest_key)):
                                smallest_key = group_name
                                longest_value = attribute_name
                        for img_value in self.image_components.values():
                            img_value.available_values.discard(longest_value)
                            if img_value.value not in list(img_value.available_values):
                                img_value.value = list(img_value.available_values)[0]
                
                if c_value.value not in list(c_value.available_values):
                    c_value.value = list(c_value.available_values)[0]
            return


    class _m1_class_gallery__GalleryButton(object):
        def __init__(self, gallery, index):
            self.gallery = gallery
            self.images = []
            self.conditions = []
            self.index = index
        
        def check_unlock(self):
            for condition in self.conditions:
                if not condition.check(True):
                    return False
            
            for image in self.images:
                if image.check_unlock(False):
                    return True
            
            return False


    @renpy.pure
    class _m1_class_gallery__GalleryToggleSlideshow(Action, FieldEquality):
        identity_fields = ["gallery"]
        
        def __init__(self, gallery):
            self.gallery = gallery
        
        def __call__(self):
            self.gallery.slideshow = not self.gallery.slideshow
            renpy.restart_interaction()
        
        def get_selected(self):
            return self.gallery.slideshow


    @renpy.pure
    class _m1_class_gallery__GalleryAction(Action, FieldEquality):
        identity_fields = ["gallery"]
        equality_fields = ["index"]
        
        def __init__(self, gallery, index):
            self.gallery = gallery
            self.index = index
        
        def __call__(self):
            renpy.invoke_in_new_context(self.gallery.show, self.index)


    class LS_Gallery(object):
        """
    :doc: gallery class

    This class supports the creation of an image gallery by handling the
    locking of images, providing an action that can show one or more images,
    and a providing method that creates buttons that use that action.

    .. attribute:: transition

        The transition that is used when changing images.

    .. attribute:: locked_button

        The default displayable used by make_button for a locked button.

    .. attribute:: hover_border

        The default hover border used by make_button.

    .. attribute:: idle_border

        The default idle border used by make_button.

    .. attribute:: unlocked_advance

        If true, the gallery will only advance through unlocked images.

    .. attribute:: navigation

        If true, the gallery will display navigation and slideshow
        buttons on top of the images.

        To customize the look of the navigation, you may override the
        gallery_navigation screen. The default screen is defined in
        renpy/common/00gallery.rpy

    .. attribute:: span_buttons

        If true, the gallery will advance between buttons.

    .. attribute:: slideshow_delay

        The time it will take for the gallery to advance between images
        in slideshow mode.

    .. attribute:: image_screen = "_gallery"

        The screen that is used to show individual images in this gallery.
        This screen is supplied the following keyword arguments:

        `locked`
            True if the image is locked.
        `displayables`
            A list of transformed displayables that should be shown to the user.
        `index`
            A 1-based index of the image being shown.
        `count`
            The number of images attached to the current button.
        `gallery`
            The image gallery object.

        Additional arguments may be supplied by prefixing them with
        `show_` in calls to Gallery.image and Gallery.unlock image.

        The default screen is defined at the bottom of renpy/common/00gallery.rpy.
    """
        
        transition = None
        
        hover_border = None
        idle_border = None
        
        locked_button = None
        
        image_screen = "_gallery"
        
        def __init__(self):
            
            self.buttons = {}
            
            
            self.button_list = []
            
            self.button_ = None
            self.image_ = None
            
            self.unlockable = None
            
            self.unlocked_advance = False
            
            self.navigation = False
            
            self.span_buttons = False
            
            self.slideshow_delay = 5
            
            self.slideshow = False
            
            self.image_screen = "_gallery"
        
        def button(self, name):
            """
        :doc: gallery method

        Creates a new button, named `name`.

        `name`
            The name of the button being created.
        """
            
            button = _m1_class_gallery__GalleryButton(self, len(self.button_list))
            
            self.unlockable = button
            self.buttons[name] = button
            self.button_list.append(button)
            self.button_ = button
        
        def image(self, *displayables, **properties):
            """
        :doc: gallery method
        :name: image

        Adds a new image to the current button, where an image consists
        of one or more displayables.

        Properties beginning with `show_` have that prefix stripped off,
        and are passed to the gallery.image_screen screen as additional
        keyword arguments.
        """
            
            self.image_ = _m1_class_gallery__GalleryImage(self, displayables, **properties)
            self.button_.images.append(self.image_)
            self.unlockable = self.image_
        
        display = image
        
        def transform(self, *transforms):
            """
        :doc: gallery method

        Applies transforms to the last image registered. This should be
        called with the same number of transforms as the image has
        displayables. The transforms are applied to the corresponding
        displayables.

        If a transform is None, the default transform is used.
        """
            
            self.image_.transforms = transforms
        
        def unlock(self, *images):
            """
        :doc: gallery method

        A condition that takes one or more image names as argument, and
        is satisfied when all the named images have been seen by the
        player. The image names should be given as strings.
        """
            
            self.unlockable.conditions.append(_m1_class_gallery__GalleryUnlockCondition(images))
        
        def condition(self, expression):
            """
        :doc: gallery method

        A condition that is satisfied when an expression evaluates to true.

        `expression`
            A string giving a Python expression.
        """
            
            if not isinstance(expression, basestring):
                raise Exception(
                "Gallery condition must be a string containing an expression."
            )
            
            self.unlockable.conditions.append(_m1_class_gallery__GalleryArbitraryCondition(expression))
        
        def allprior(self):
            """
        :doc: gallery method

        A condition that is true if all prior images associated with the
        current button have been unlocked.
        """
            
            self.unlockable.conditions.append(_m1_class_gallery__GalleryAllPriorCondition())
        
        def unlock_image(self, *images, **properties):
            """
        :doc: gallery method

        A convenience method that is equivalent to calling image and unlock
        with the same parameters. (Keyword arguments beginning with ``show_`` are
        only passed to image.) This will cause an image to be displayed
        if it has been seen before.

        The images should be specified as strings giving image names.
        """
            
            self.image(*images, **properties)
            self.unlock(*images)
        
        def Action(self, name):
            """
        :doc: gallery method

        An action that displays the images associated with the given button
        name.
        """
            
            if name not in self.buttons:
                raise Exception(
                "{0!r} is not a button defined in this gallery.".format(name)
            )
            
            b = self.buttons[name]
            
            if b.check_unlock():
                return _m1_class_gallery__GalleryAction(self, b.index)
            else:
                return None
        
        def make_button(
        self,
        name,
        unlocked,
        locked=None,
        hover_border=None,
        idle_border=None,
        style=None,
        **properties,
    ):
            """
        :doc: gallery method

        This creates a button that displays the images associated with the given
        button name.

        `name`
            The name of the button that will be created.

        `unlocked`
            A displayable that is displayed for this button when it is
            unlocked.

        `locked`
            A displayable that is displayed for this button when it is
            locked. If None, the locked_button field of the gallery
            object is used instead.

        `hover_border`
            A displayable that is used to overlay this button when
            it is unlocked and has focus. If None, the hover_border
            field of the gallery object is used.

        `idle_border`
            A displayable that is used to overlay this button when
            it is unlocked but unfocused. If None, the idle_border
            field of the gallery object is used.

        `style`
            The style the button inherits from. When None, defaults
            to the "empty" style, so as not to inherit borders and
            so on.

        Additional keyword arguments become style properties of the
        created button object.
        """
            
            action = self.Action(name)
            
            if locked is None:
                locked = self.locked_button
            
            if hover_border is None:
                hover_border = self.hover_border
            
            if idle_border is None:
                idle_border = self.idle_border
            
            if style is None:
                if (config.script_version is not None) and (
                config.script_version <= (7, 0, 0)
            ):
                    style = "button"
                else:
                    style = "empty"
            
            return Button(
            action=action,
            child=unlocked,
            insensitive_child=locked,
            hover_foreground=hover_border,
            idle_foreground=idle_border,
            style=style,
            **properties,
        )
        
        def get_fraction(self, name, format="{seen}/{total}"):
            """
        :doc: gallery method

        Returns a text string giving the number of unlocked images and total number of images in the button
        named `name`.

        `format`
            A Python format string that's used to format the numbers. This has three values that
            can be substituted in:

            {seen}
                The number of images that have been seen.
            {total}
                The total number of images in the button.
            {locked}
                The number of images that are still locked.
        """
            
            seen = 0
            total = 0
            
            all_prior = True
            
            for button_img in self.buttons[name].images:
                total += 1
                if button_img.check_unlock(all_prior):
                    seen += 1
                else:
                    all_prior = False
            
            return format.format(seen=seen, total=total, locked=total - seen)
        
        def show(self, button=0, image=0):
            """
        Starts showing gallery images.

        `button`
            The index of the button to start showing.
        """
            
            
            
            all_images = []
            
            
            
            unlocked_images = []
            
            for bi, b in enumerate(self.button_list):
                all_unlocked = True
                
                for ii, button_img in enumerate(b.images):
                    all_images.append((bi, ii))
                    
                    unlocked = button_img.check_unlock(all_unlocked)
                    
                    if unlocked:
                        unlocked_images.append((bi, ii))
                    else:
                        all_unlocked = False
                        
                        if self.unlocked_advance and (button == bi) and (image == ii):
                            image += 1
            
            self.slideshow = False
            show_cg_options = True
            changed_attr = None
            options_page_number = 0
            current_bg = None
            
            while True:
                if button >= len(self.button_list):
                    break
                
                b = self.button_list[button]
                
                if image >= len(b.images):
                    break
                
                button_img = b.images[image]
                
                result = button_img.show(
                (button, image) not in unlocked_images,
                image,
                len(b.images),
                show_cg_options,
                changed_attr,
                options_page_number,
                current_bg,
            )
                
                if result is True:
                    continue
                
                
                if result == "return":
                    break
                
                
                
                if result == "hide_options":
                    show_cg_options = False
                elif result == "show_options":
                    show_cg_options = True
                elif len(result) == 2:
                    result_action, result_value = result
                    if result_action == "changed_options":
                        changed_attr = result_value
                    elif result_action == "page_options":
                        options_page_number = result_value
                    elif result_action == "changed_bg":
                        current_bg = result_value
                    pass
            renpy.transition(self.transition)
        
        def Return(self):
            """
        :doc: gallery method

        Stops displaying gallery images.
        """
            for k, patched_value in store.ORIGINAL_PATCHED_VALUES.items():
                k.__call__ = patched_value
            store.ORIGINAL_PATCHED_VALUES = dict()
            return ui.returns("return")
        
        def Next(self, unlocked=False):
            """
        :doc: gallery method

        Advances to the next image in the gallery.

        `unlocked`
            If true, only considers unlocked images.
        """
            
            if unlocked:
                return ui.returns("next_unlocked")
            else:
                return ui.returns("next")
        
        def Previous(self, unlocked=False):
            """
        :doc: gallery method

        Goes to the previous image in the gallery.

        `unlocked`
            If true, only considers unlocked images.
        """
            
            if unlocked:
                return ui.returns("previous_unlocked")
            else:
                return ui.returns("previous")
        
        def ToggleSlideshow(self):
            """
        :doc: gallery method

        Toggles slideshow mode.
        """
            return _m1_class_gallery__GalleryToggleSlideshow(self)



init 2 python:

    from collections import defaultdict

    re_ch_location = re.compile(r"(?:.+\/)?ch\/(.+)\/(ev2|st|st2)\/")
    sorted_images = defaultdict(dict)
    all_persons = {p.id for p in Person.all()}
    bg_list = list()
    for i in renpy.list_images():
        if i.startswith("bg "):
            if "tutorial" in i:
                continue
            bg_list.append(i)
            continue
        if isinstance(renpy.get_registered_image(i), LayeredImage):
            
            if i.endswith(" close"):
                continue
            if i.endswith(" smartphone"):
                continue
            if i.endswith("_talk"):
                continue
            if i.startswith("button"):
                continue
            if i.startswith("chibi"):
                continue
            if i.startswith("snow"):
                continue
            layered_obj = renpy.get_registered_image(i)
            all_filenames = set()
            for l_attr in layered_obj.layers:
                if hasattr(l_attr, "image"):
                    attribute_location = l_attr.image.visit()
                    if attribute_location:
                        if hasattr(attribute_location[0], "filename"):
                            ch_location = attribute_location[0].filename
                        elif isinstance(attribute_location[0], Transform):
                            ch_location = attribute_location[0].children
                            if ch_location and hasattr(ch_location[0], "filename"):
                                ch_location = ch_location[0].filename
                            else:
                                continue
                        else:
                            continue
                        if re_ch_location.match(ch_location):
                            ch_location = re_ch_location.match(ch_location).group(1)
                            ch_location = ch_location.replace("/", "_")
                            ch_location = ch_location.replace("_full", "")
                            all_filenames.add(ch_location)
            
            if len(all_filenames) == 1:
                sorted_images[list(all_filenames)[0]].update({i: (layered_obj, i)})
            else:
                pass

    for category, category_images in sorted_images.items():
        sorted_images[category] = dict(sorted(category_images.items()))


    def sort_images(image_object, images_list):
        npc = None
        img_attributes = {
        image_attribute.attribute for image_attribute in image_object.attributes
    }
        if {person} & img_attributes:
            del images_list[person][img_name]
            image_button = f"{img_name} {person}"
            npc = person
            images_list[person][img_name] = (image_object, image_button)
        else:
            random_npc = img_attributes & all_persons
            if random_npc:
                random_npc = renpy.random.choice(list(random_npc))
                del images_list[person][img_name]
                image_button = f"{img_name} {random_npc}"
                npc = random_npc
                images_list[person][img_name] = (image_object, image_button)
        return npc


    def gallery_compute(displayable):
        current_displayable = displayable
        image_name = " ".join(current_displayable.child.raw_child.name)
        layered_object = renpy.get_registered_image(image_name)
        return displayable, layered_object


    bg_list.sort()
    ls_gallery = LS_Gallery()
    tmp_dict = copy.deepcopy(sorted_images)

    for person, v in tmp_dict.items():
        for img_name, (img_object, img_button) in v.items():
            missing_npc = None
            
            
            
            
            if img_object.attribute_function:
                if isinstance(img_object.attribute_function, MultiPickers):
                    if not img_object.attribute_function.npcs:
                        missing_npc = sort_images(img_object, sorted_images)
                elif isinstance(img_object.attribute_function, Pickers):
                    if (
                    not hasattr(img_object.attribute_function, "kwargs")
                    or "npc" not in img_object.attribute_function.kwargs
                ):
                        missing_npc = sort_images(img_object, sorted_images)
            ls_gallery.button(img_name)
            ls_gallery.image(img_name, missing_npc=missing_npc)
            ls_gallery.unlock(img_name)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
