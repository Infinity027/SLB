screen warning_gallery():
    zorder 50
    frame:
        background "gui/main/bg.png"
        add "ch/bree/st/bree_smartphone.webp" xalign 0.25 yalign 0.20
        add "ch/mike/st/mike_smartphone.webp" xalign 0.75 yalign 0.20
        vbox:
            xmaximum 960
            xalign 0.5
            yalign 0.7
            text "" size 24 outlines [(2, "#FF0000")] color "#ffffff" xalign 0.5
            text "Small warning!" size 24 outlines [(1, "#FF0000")] color "#ffffff"
            text "The gallery is in an experimental state." size 24 outlines [(1, "#FF0000")] color "#ffffff"
            text "You will encounter bugs and issues." size 24 outlines [(1, "#FF0000")] color "#ffffff"
            text "Reporting them will help us to improve the gallery :)" size 24 outlines [(1, "#FF0000")] color "#ffffff"
            text "" size 24 outlines [(2, "#FF0000")] color "#ffffff" xalign 0.5
            vbox:
                xalign 0.5
                textbutton "I understand" action [SetVariable("GALLERY_WARNING", True), Hide("warning_gallery"), ShowMenu("main_gallery")] style "main_menu_button"

screen main_gallery():
    key ["K_ESCAPE", "mouseup_3", "pad_b_press"] action [Hide("main_gallery"), Return()]
    zorder 50 tag menu


    add "gui/main/bg.png"
    frame:
        background Frame("gui/textbox.png", Borders(20, 20, 20, 20))
        has hbox
        xsize 1280
        spacing 15
        viewport id "gallery_person":
            xsize 280
            draggable True
            mousewheel True
            scrollbars "vertical"
            has vbox spacing 1
            for person in sorted(sorted_images):
                $ person_display = " ".join(person.capitalize().split("_"))
                textbutton person_display text_xalign 0.0 text_xoffset 15 style "gallery_button" action [SensitiveIf(GALLERY_ID != person), SetVariable("GALLERY_ID", person)]
            null height 2

        $ grid_content = len(sorted_images[GALLERY_ID]) + 1

        $ grid_columns = 4
        $ grid_rows = ceil(grid_content / grid_columns)
        $ empty_boxes = (grid_columns * grid_rows) - len(sorted_images[GALLERY_ID])
        vpgrid id "gallery_content":
            cols grid_columns
            spacing 15
            xspacing 32
            draggable True
            mousewheel True
            yfill True
            xfill True
            xsize 1000
            child_size (210, 215)
            scrollbars "vertical"
            for img_name, (_, img_button) in sorted_images[GALLERY_ID].items():
                $ button_displayable = Transform(Transform(img_button, size=(180, 101), fit="cover"), crop=(0, 0, 180, 101))
                hbox:
                    yfill True
                    vbox:
                        xsize 210
                        ysize 215
                        add ls_gallery.make_button(img_name, button_displayable, Transform(button_displayable, matrixcolor=SaturationMatrix(0), blur=20), xalign=0.5, yalign=0.5)
                        text img_name.capitalize() style "gallery_button_text"
            textbutton "Return" yalign 0.25 action [Hide("main_gallery"), Return()] style "gallery_button"

screen _gallery(locked, displayable, gallery, **properties):
    add displayable
    key ["K_ESCAPE", "mouseup_3", "pad_b_press"] action gallery.Return()

screen hidden_cg_options():
    zorder 20
    textbutton "<<" action [Return('show_options')] style "gallery_navigation_button" xalign 0.99

screen cg_options(layered_obj, image_components, page_number, current_bg):
    $ page_max = 0
    $ group_components = dict()
    $ standalone_components = dict()
    $ has_bg = set()
    for img_component in image_components.values():
        if img_component.component_type == "group":
            $ group_components[img_component.name] = img_component
            if img_component.name in ["bg", "background"]:
                $ has_bg.add(img_component.name)
        elif img_component.component_type == "standalone":
            $ standalone_components[img_component.name] = img_component
        elif img_component.component_type == "always" and {"bg", "background"} & set(img_component.name.split('_')):
            $ has_bg.add(img_component.name)
    if standalone_components:
        $ page_max += 1
    if not has_bg:
        $ page_max += 1
    zorder 20
    frame:
        xsize 300
        xalign 1.0
        background Frame("gui/textbox.png", Borders(1, 1, 1, 1))
        has vbox
        xfill True
        xalign 0.5
        spacing 5
        hbox:
            xfill True
            textbutton ">>" action [Return('hide_options')] style "gallery_navigation_button" xalign 0.0 yalign 0.5
            textbutton "Return" action [Return("return")] style "gallery_button" xsize 150
            hbox:
                xalign 1.0
                yalign 0.5
                textbutton _("<") action [SensitiveIf(page_number > 0), Return(('page_options', page_number-1))] style "gallery_navigation_button"
                textbutton _(">") action [SensitiveIf(page_number < page_max), Return(('page_options', page_number+1))] style "gallery_navigation_button"
        hbox:
            xfill True
            text f"{layered_obj.name.replace('_', ' ').capitalize()}" style "gallery_title" xalign 0.5
        hbox:
            viewport id "groups_cg_options":
                draggable True
                mousewheel True
                has vbox
                spacing 5
                xfill True
                if page_number == 0:
                    for img_component_name, img_component in group_components.items():
                        $ currently_shown = img_component.value
                        $ previous_available_value = find_prev(currently_shown, sorted(list(img_component.available_values)))
                        $ next_available_value = find_next(currently_shown, sorted(list(img_component.available_values)))
                        hbox:
                            xfill True
                            if img_component.default_value and not img_component.linked_component:
                                textbutton _(f"{img_component_name.replace('_', ' ').capitalize()}") style "gallery_group_with_default_button" text_xpos 0.15 text_xanchor 0.0
                            elif img_component.linked_component:
                                textbutton _(f"{img_component_name.replace('_', ' ').capitalize()}") style "gallery_group_button" text_xpos 0.15 text_xanchor 0.0 action [SensitiveIf(img_component.available_for_interaction), ToggleField(img_component, "to_display", true_value=True, false_value=False), ToggleField(standalone_components.get(img_component_name), "to_display", true_value=True, false_value=False), Return(('changed_options', (img_component.id, not img_component.to_display, currently_shown))) ]
                            else:
                                textbutton _(f"{img_component_name.replace('_', ' ').capitalize()}") style "gallery_group_button" text_xpos 0.15 text_xanchor 0.0 action [SensitiveIf(img_component.available_for_interaction), ToggleField(img_component, "to_display", true_value=True, false_value=False), Return(('changed_options', (img_component.id, not img_component.to_display, currently_shown))) ]
                        hbox:
                            spacing 2
                            xfill True
                            textbutton _("<") style "gallery_button" text_yalign 0.63 ysize 20 xsize 30 xalign 0.0 action [SetField(img_component, "value", previous_available_value), Return(('changed_options', (img_component.id, previous_available_value, currently_shown)))]
                            text currently_shown yalign 0.65 style "gallery_button_text"
                            textbutton _(">") style "gallery_button" text_yalign 0.63 ysize 20 xsize 30 xalign 1.0 action [SetField(img_component, "value", next_available_value), Return(('changed_options', (img_component.id, next_available_value, currently_shown)))]
                elif page_number == 1 and standalone_components:
                    for img_component_name, img_component in standalone_components.items():
                        hbox:
                            xalign 0.5
                            xfill True
                            if img_component.linked_component:
                                textbutton img_component_name.replace('_', ' ').capitalize() style "gallery_button" xminimum 200 action [ToggleField(img_component, "to_display", true_value=True, false_value=False), ToggleField(group_components[img_component_name], "to_display", true_value=True, false_value=False), Return(('changed_options', (img_component_name, not img_component.to_display, img_component.to_display)))]
                            else:
                                textbutton img_component_name.replace('_', ' ').capitalize() style "gallery_button" xminimum 200 action [ToggleField(img_component, "to_display", true_value=True, false_value=False), Return(('changed_options', (img_component_name, not img_component.to_display, img_component.to_display)))]
                else:
                    if not current_bg:
                        $ current_bg = bg_list[0]
                    $ previous_available_bg = find_prev(current_bg, bg_list)
                    $ next_available_bg = find_next(current_bg, bg_list)
                    hbox:
                        xfill True
                        text "Background" style "gallery_title" xalign 0.5
                    hbox:
                        spacing 2
                        xfill True
                        textbutton _("<") style "gallery_button" text_yalign 0.63 ysize 20 xsize 30 xalign 0.0 action [Return(('changed_bg', previous_available_bg))]
                        text _(f"{current_bg.replace('bg ', '')}") yalign 0.65 style "gallery_button_text"
                        textbutton _(">") style "gallery_button" text_yalign 0.63 ysize 20 xsize 30 xalign 1.0 action [Return(('changed_bg', next_available_bg))]
            vbar value YScrollValue("groups_cg_options") unscrollable "hide" style "gallery_scroll"

style gallery_group_with_default_button is button:
    background "gui/gallery/gallerygroup_empty.png"
    xfill True
    xalign 0.0
    xminimum 275

style gallery_group_with_default_button_text is text:
    color "#ffffff"
    font "palanquin_medium"
    yalign 0.5
    xpos 15
    size 20


style gallery_group_button is button:
    idle_background "gui/phone/empty_idle.png"
    hover_background "gui/phone/empty_hover.png"
    insensitive_background "gui/phone/empty_insensitive.png"
    selected_background "gui/phone/empty_hover.png"
    selected_hover_background "gui/phone/empty_idle.png"
    selected_insensitive_background "gui/phone/empty_insensitive.png"
    xfill True
    xalign 0.0
    xminimum 275

style gallery_group_button_text is text:
    color "#ffffff"
    font "palanquin_medium"
    yalign 0.5
    xpos 15
    size 20

style gallery_button is button:
    idle_background Frame("gui/button_idle.png", Borders(5, 5, 5, 5))
    hover_background Frame("gui/button_hover.png", Borders(5, 5, 5, 5))
    insensitive_background Frame("gui/button_insensitive.png", Borders(5, 5, 5, 5))
    selected_background Frame("gui/button_hover.png", Borders(5, 5, 5, 5))
    selected_hover_background Frame("gui/button_idle.png", Borders(5, 5, 5, 5))
    xfill True
    yalign 0.5
    xalign 0.5

style gallery_button_text is text:
    color "#ffffff"
    font "palanquin_medium"
    yalign 0.5
    xalign 0.5
    size 20

style gallery_title is text:
    font "palanquin_medium"
    size 30
    color "#ffffff"

style gallery_navigation_button is button:
    idle_background Frame("gui/phone/ico_phone_idle.png")
    hover_background Frame("gui/phone/ico_phone_hover.png")
    insensitive_background Frame("gui/phone/ico_phone_insensitive.png")
    selected_background Frame("gui/phone/ico_phone_hover.png")
    selected_hover_background Frame("gui/phone/ico_phone_idle.png")
    xsize 30
    ysize 30

style gallery_navigation_button_text is text:
    color "#ffffff"
    font "palanquin_medium"
    size 15
    yalign 0.7
    xalign 0.5

style gallery_scroll is vbar:
    left_bar "gui/inv/vertical_idle_bar_long.png"
    right_bar "gui/inv/vertical_empty_bar_long.png"
    thumb "gui/inv/vertical_idle_thumb.png"
    xanchor 1.0
    xalign 1.0
    bar_invert True
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
