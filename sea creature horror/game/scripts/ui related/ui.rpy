init python:
    def allow_edge_scroll():
        x, y = renpy.get_mouse_pos()
        return x < 1620 

screen uiWindow:
    zorder 0
    add "gui/customui/uioverlay.png"

    if settingsClicked == False:
        imagebutton: #settings
            pos (1755,51) #where it appears on the screen
            auto "gui/customui/settings_%s.png" action SetVariable("settingsClicked", True), Show("uiSettings", layer="ui")
    elif settingsClicked == True:
        add "gui/customui/settings_hover.png":
            pos (1755,51) #where it appears on the screen
    
    if item_page == False:
        add "gui/customui/brain1.png":
            pos (1723,895)
    if item_page == True:
        add "gui/customui/brain2.png":
            pos (1723,895)
    if item_knife == True:
        add "gui/customui/brain3.png":
            pos (1723,895)
    if item_lighter == True:
        add "gui/customui/brain4.png":
            pos (1723,895)
    fixed at inventory_fade(not hide_inventory):
        use inventoryView
        #if inventory_open == False:
            #add "gui/customui/inventory.png":
                #pos (1703,175)
        #if inventory_open == False:
            #textbutton "{size=28}Inventory":
                #pos (1737,192)
                #action Show("inventoryView"), SetVariable("inventory_open", True), SetVariable("cargo_buttons_enabled", False), SetVariable("cargo_scroll_enabled", False)
transform fade_in:
    alpha 0.0
    linear 0.3 alpha 1.0
    
screen uiSettings:
    modal True

    $room_scroll_enabled = False

    add Solid("#00000050")

    hbox:
        xalign 0.85
        yalign 0.075
        spacing 25
    
        textbutton _("History") action ShowMenu("history"):
            text_font "fonts/fisherman_2/Fisherman-Regular.otf"
            text_color "#7eb4bf"
            text_hover_color "#ffffff"
            text_outlines [(3, "#32464e", 1, 1)]

        if characterTalk == False:
            textbutton _("Save") action ShowMenu("save"):
                text_font "fonts/fisherman_2/Fisherman-Regular.otf"
                text_color "#7eb4bf"
                text_hover_color "#ffffff"
                text_outlines [(3, "#32464e", 1, 1)]

        textbutton _("Load") action ShowMenu("load"):
            text_font "fonts/fisherman_2/Fisherman-Regular.otf"
            text_color "#7eb4bf"
            text_hover_color "#ffffff"
            text_outlines [(3, "#32464e", 1, 1)]

        textbutton _("Preferences") action ShowMenu("preferences"):
            text_font "fonts/fisherman_2/Fisherman-Regular.otf"
            text_color "#7eb4bf"
            text_hover_color "#ffffff"
            text_outlines [(3, "#32464e", 1, 1)]

        if characterTalk == False:
            textbutton "Return":
                text_font "fonts/fisherman_2/Fisherman-Regular.otf"
                text_color "#7eb4bf"
                text_hover_color "#ffffff"
                text_outlines [(3, "#32464e", 1, 1)]
                action SetVariable("settingsClicked", False), Hide("uiSettings")
        elif characterTalk == True:
            textbutton "Return":
                text_font "fonts/fisherman_2/Fisherman-Regular.otf"
                text_color "#7eb4bf"
                text_hover_color "#ffffff"
                text_outlines [(3, "#32464e", 1, 1)]
                action SetVariable("settingsClicked", False), Hide("uiSettings")