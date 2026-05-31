init -19:

    define STORIES = {}
    define STORY_PARTICIPANTS = {}






    default DATA_STORIES = {}


    define storytracker = StoryTracker()
    $ storytracker.load()

screen story_tracker():
    key ["K_ESCAPE", "mouseup_3", "pad_b_press"] action Hide("story_tracker")
    on "show" action Hide("smartphone")

    default tracker_type = StoryStatus.ACTIVE
    default tracker_story = None
    default tracker_filter = "all"
    default enable_spoilers = False
    default spoilers_hints = None
    default spoilers_height = 120
    default spoilers_width = 120

    $ participants, stories, tracker_story = storytracker.for_ui(tracker_filter, tracker_type, tracker_story)
    $ generic_stories = {k:v for k,v in stories.items() if v._type == "generic"}
    $ harems_stories = {k:v for k,v in stories.items() if v._type == "harem"}
    $ npc_stories = {k:v for k,v in stories.items() if v._type == "npc"}
    $ filters = {"all": "All", "harem": "Harems", "generic": "Generic"}
    $ filters.update(participants)

    style_prefix "story"
    vbox:
        xysize (1230, 600)
        pos (25, 110)
        frame:
            xysize (1230, 600)
            xpadding 5
            frame:
                style_prefix "story_title"
                pos -20,-20
                label "STORY TRACKER"
            vbox:
                frame style "invisible_frame":
                    xysize (1200, 47)
                    align (0.5, 0.5)
                    style_prefix "story_type"
                    textbutton f"Filter: {filters[tracker_filter]}":
                        align (0.5, 0.5)
                        action CaptureFocus("filter_dropdown")
                    hbox:
                        spacing 4
                        align (0.99, 0.5)
                        textbutton _("Spoilers") selected enable_spoilers tooltip "Enable/Disable tooltip for the story steps.\nClick on the step with a 👁️ to see the hints." action ToggleLocalVariable("enable_spoilers", true_value=True, false_value=False)
                        textbutton _("Active") tooltip "Show the ongoing step." action [SensitiveIf(tracker_type != StoryStatus.ACTIVE), SetScreenVariable("tracker_type", StoryStatus.ACTIVE)]
                        textbutton _("Completed") tooltip "Show the completed step." action [SensitiveIf(tracker_type != StoryStatus.COMPLETED), SetScreenVariable("tracker_type", StoryStatus.COMPLETED)]

                frame:
                    xysize (1230, 15)
                    xpos -4
                    background Line("#006284", (0, 0), (1230, 0), 5)
                hbox:
                    viewport id "story_stories":
                        if tracker_filter == True:
                            xpos -600
                        xysize (280, 505)
                        draggable True
                        mousewheel True
                        vbox spacing 1:
                            if generic_stories:
                                textbutton "Generic"
                                for key, story in generic_stories.items():
                                    button:
                                        hbox:
                                            if story.complete and story.status_icon != "None":
                                                add "gui/icons/icon_[story.status_icon].png" xysize (25, 25) yalign 0.5
                                            else:
                                                null width 30
                                            text text_tag_resize(story.name, 270)
                                        action [SelectedIf(tracker_story == key), SetScreenVariable("tracker_story", key)]
                            if npc_stories:
                                textbutton "Npc"
                                for key, story in npc_stories.items():
                                    button:
                                        hbox:
                                            if story.complete and story.status_icon != "None":
                                                add "gui/icons/icon_[story.status_icon].png" xysize (25, 25) yalign 0.5
                                            else:
                                                null width 30
                                            text text_tag_resize(story.name, 270)
                                        action [SelectedIf(tracker_story == key), SetScreenVariable("tracker_story", key)]
                            if harems_stories:
                                textbutton "Harems"
                                for key, story in harems_stories.items():
                                    button:
                                        hbox:
                                            if story.complete and story.status_icon != "None":
                                                add "gui/icons/icon_[story.status_icon].png" xysize (25, 25) yalign 0.5
                                            else:
                                                null width 30
                                            text text_tag_resize(story.name, 270)
                                        action [SelectedIf(tracker_story == key), SetScreenVariable("tracker_story", key)]
                            null height 2
                    vbar value YScrollValue("story_stories") xmaximum 11 unscrollable "hide" alt "scroll "
                    viewport id "story_description_text":
                        draggable True
                        mousewheel True
                        xsize 890
                        has vbox
                        style_prefix "story_description"
                        if not tracker_story in stories:
                            text "There are no stories to show"
                        else:
                            $ current_story = stories[tracker_story]
                            $ extra_data = None
                            if enable_spoilers and current_story.extra_data:
                                $ extra_data = [f"{k.capitalize()}: {safe_eval(v)}\n" for k,v in current_story.extra_data.items()]
                            hbox:
                                style_prefix "story_title"
                                spacing 10
                                textbutton current_story.name:
                                    alt current_story.name
                                    if extra_data:
                                        action [CaptureFocus("spoilers"), SetScreenVariable("spoilers_hints", extra_data)]
                                    else:
                                        tooltip ""
                                        action NullAction
                                if hasattr(current_story, 'wiki_link') and current_story.wiki_link:
                                    textbutton "{size=25}🔗{/size}":
                                        action OpenURL(current_story.wiki_link)

                            null height 10
                            text current_story.desc alt ""
                            if tracker_type == StoryStatus.COMPLETED:
                                null height 10
                                text "Outcome" alt "" style_prefix "story_title"
                                null height 10
                                text current_story[current_story.outcome].description alt ""
                            null height 20
                            for step in current_story.steps.values():
                                if not step.inactive and not step.hide:
                                    $ step_self_voicing = ""
                                    $ desc = step.desc if not step.optional else f"OPTIONAL: {step.desc}"
                                    $ hints = None
                                    if enable_spoilers and ((step.active and tracker_type == StoryStatus.ACTIVE) or config.developer) and hasattr(step, 'related_event') and step.related_event:
                                        if BaseEvent.find(step.related_event):
                                            $ hints = BaseEvent.find(step.related_event).examine_ui()
                                        elif BaseActivity.find(step.related_event):
                                            $ hints = BaseActivity.find(step.related_event).examine_ui()
                                        elif TalkSubject.find(step.related_event):
                                            $ hints = TalkSubject.find(step.related_event).examine_ui()
                                        if hints:
                                            $ desc = f"👁️ {desc}"
                                    hbox:
                                        fixed:
                                            style_prefix "story_description_icon"
                                            if step.percentage and step.active:
                                                bar value step.percentage_for_ui range 100 ysize 32 xsize 95
                                                text f"{step.percentage_for_ui}%" alt ""
                                                $ step_self_voicing = f"active: {step.percentage_for_ui}% {desc}"
                                            elif step.status_icon != "None":
                                                text "{image=gui/icons/icon_[step.status_icon].png}" alt ""
                                                $ step_self_voicing = f"{story_step_alt(step.status_icon)}: {desc}"
                                            else:
                                                null height 25

                                        textbutton desc:
                                            if hints:
                                                action [CaptureFocus("spoilers"), SetScreenVariable("spoilers_hints", hints)]
                                            else:
                                                action NullAction
                                                tooltip ""
                                            alt step_self_voicing
                        null height 20

                    vbar value YScrollValue("story_description_text") unscrollable "hide" alt "scroll "

    if GetFocusRect("filter_dropdown"):
        dismiss action ClearFocus("filter_dropdown")

        nearrect:
            focus "filter_dropdown"
            style_prefix "story_select"
            has frame
            align (0.5, 0.5)
            modal True
            xysize (200, 300)
            frame style "invisible_frame":
                align (0.5, 0.5)
                xmaximum 180
                ymaximum 280
                viewport id "filter_drop":
                    draggable True
                    mousewheel True

                    has vbox
                    for filterid, filtername in filters.items():
                        textbutton filtername:
                            action [SetScreenVariable("tracker_filter", filterid), ClearFocus("filter_dropdown")]
                            xanchor 5

                vbar value YScrollValue("filter_drop") left_bar "gui/inv/vertical_idle_bar_small.png" thumb "gui/inv/vertical_idle_thumb.png" right_bar "gui/inv/vertical_idle_bar_small.png" align (0.97, 0.5) ysize 250 thumb_offset 10 top_gutter 10.5 bottom_gutter 10.5 unscrollable "hide" alt "scroll "

    $ tooltip = GetTooltip()
    if tooltip:
        nearrect:
            focus "tooltip"
            preferred_side "right"
            style_prefix "tooltips"

            has frame
            align (0.5, 0.4)
            ymaximum 650
            xpadding 20
            text tooltip substitute False yalign 0.05 alt ""


    if GetFocusRect("spoilers"):
        dismiss action [ClearFocus("spoilers"), SetScreenVariable("spoilers_hints", None)]
        if spoilers_hints:
            $ spoilers_width = int(max([get_string_size_in_pixel(s, style.tooltips_text.font, style.item_frame_message_text.size)[0] for s in spoilers_hints])) + 1
            $ spoilers_height = len(spoilers_hints) * 25
            nearrect:
                rect (450, 320, 25, 25)
                preferred_side "right"
                style_prefix "tooltips"

                has frame
                modal True
                xmaximum 800
                if spoilers_height < 625:
                    align (0.5, 0.5)
                    xsize spoilers_width + 30
                    vbox:
                        xmaximum 780
                        for spoiler in spoilers_hints:
                            text spoiler substitute False align (0.0, 0.05) alt ""
                else:
                    align (0.5, 0.4)
                    xsize spoilers_width + 35
                    ysize 625
                    viewport id "spoilers_vp":
                        draggable True
                        mousewheel True
                        scrollbars "vertical"
                        vscrollbar_base_bar Frame("gui/inv/vertical_idle_bar_long.png")
                        vscrollbar_thumb "gui/inv/vertical_idle_thumb.png"
                        has vbox
                        xmaximum 780
                        for spoiler in spoilers_hints:
                            text spoiler substitute True align (0.0, 0.05) alt ""
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
