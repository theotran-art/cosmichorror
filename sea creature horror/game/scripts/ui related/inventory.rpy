


transform inventory_fade(showing): # transition for inventory fade
    linear 0.25 alpha (1.0 if showing else 0.0)

screen inventoryView():
    tag menu  # prevents stacking with other menus

    modal True

    on "show":
        at fade_in
    fixed:
        xalign 1.0
        yalign 0.0
        xoffset 6
        yoffset 175

        add "gui/customui/inventory.png":
            xalign 1.0
            yalign 0.0

        vbox:
            xalign 0.9755
            yalign 0.025
            spacing 8
            xmaximum 140
            text "Inventory" size 28 font "fonts/fisherman_2/Fisherman-Regular.otf" color "#3d707a"

        #CARGO
            #page
            if item_page == True: #THIS IS COMPLETED PAGE
                textbutton "Page":
                    text_size 24
                    text_font "fonts/Sedan_SC/SedanSC-Regular.ttf"
                    text_hover_color "#ffffff"
                    text_color "#b4dee6"

                    action [
                        Hide("inventoryView"),
                        SetVariable("inventory_open", False),
                        Jump("examinePage")
                    ]
            if item_page_1 and not page_combined:
                textbutton "Ripped page from book":
                    text_size 24
                    text_font "fonts/Sedan_SC/SedanSC-Regular.ttf"
                    text_hover_color "#ffffff"
                    text_color "#b4dee6"

                    action [
                        Hide("inventoryView"),
                        SetVariable("inventory_open", False),
                        Jump("examinePage1")
                    ]
            if item_page_2 and not page_combined:
                textbutton "Ripped page from cultist":
                    text_size 24
                    text_font "fonts/Sedan_SC/SedanSC-Regular.ttf"
                    text_hover_color "#ffffff"
                    text_color "#b4dee6"

                    action [
                        Hide("inventoryView"),
                        SetVariable("inventory_open", False),
                        Jump("examinePage2")
                    ]
        #KITCHEN
            #knife
            if item_knife:
                textbutton "Knife":
                    text_size 24
                    text_font "fonts/Sedan_SC/SedanSC-Regular.ttf"
                    text_hover_color "#ffffff"
                    text_color "#b4dee6"

                    action [
                        Hide("inventoryView"),
                        SetVariable("inventory_open", False),
                        Jump("examineKnife")
                    ]
            #arm
            if kitchenArm and kitchenArmCooked:
                textbutton "Arm stew":
                    text_size 24
                    text_font "fonts/Sedan_SC/SedanSC-Regular.ttf"
                    text_hover_color "#ffffff"
                    text_color "#b4dee6"

                    action [
                        Hide("inventoryView"),
                        SetVariable("inventory_open", False),
                        Jump("examineArm")
                    ]
            elif kitchenArm:
                textbutton "Severed arm":
                    text_size 24
                    text_font "fonts/Sedan_SC/SedanSC-Regular.ttf"
                    text_hover_color "#ffffff"
                    text_color "#b4dee6"

                    action [
                        Hide("inventoryView"),
                        SetVariable("inventory_open", False),
                        Jump("examineArm")
                    ]
            #spices
            if kitchenSpices:
                textbutton "Spices and herbs":
                    text_size 24
                    text_font "fonts/Sedan_SC/SedanSC-Regular.ttf"
                    text_hover_color "#ffffff"
                    text_color "#b4dee6"

                    action [
                        Hide("inventoryView"),
                        SetVariable("inventory_open", False),
                        Jump("examineSpices")
                    ]
        #MOONPOOL
            #lighter
            if item_lighter:
                textbutton "Lighter":
                    text_size 24
                    text_font "fonts/Sedan_SC/SedanSC-Regular.ttf"
                    text_hover_color "#ffffff"
                    text_color "#b4dee6"

                    action [
                        Hide("inventoryView"),
                        SetVariable("inventory_open", False),
                        Jump("examineLighter")
                    ]
            #close inventory
            #textbutton "{size=22}Close":
                #action Hide("inventoryView"), SetVariable("inventory_open", False), SetVariable("cargo_buttons_enabled", True), SetVariable("cargo_scroll_enabled", True)

label examinePage: #THIS IS COMPLETED PAGE
    $room_buttons_enabled = False
    $room_scroll_enabled = False
    $showItemPage = True
    t "You have a page that reads out the passage:"
    "\"O Mother of the Great Deep, we sever our love to our flesh to offer it to you alone, flaying our imperfect forms as penance for the circumstances of our births.\""
    "\"Accept our emaciated bodies and deliver us, for we yearn to be entangled in your cold embrace as the children of your new earth.\""
    $showItemPage = False
    jump expression locationTracker

label examinePage1: 
    $room_buttons_enabled = False
    $room_scroll_enabled = False
    $showItemPage1 = True
    t "You have a ripped page that reads out the passage:"
    "\"-iver us, for we yearn to be entangled in your cold embrace as the children of your new earth.\""
    if item_page_2 == True:
        menu:
            "Combine the ripped pages.":
                $showItemPage1 = False
                $cargo_buttons_enabled = False 
                $cargo_scroll_enabled = False
                #show screen combine_pages
                $ result = renpy.call_screen("combine_pages")
                if result:
                    jump combinePagesFinished
                $ renpy.pause()
    $showItemPage1 = False
    jump expression locationTracker

label examinePage2: 
    $room_buttons_enabled = False 
    $room_scroll_enabled = False
    $showItemPage2 = True
    t "You have a ripped page that reads out the passage:"
    "\"O Mother of the Great Deep, we sever our love to our flesh to offer it to you alone, flaying our imperfect forms as penance for the circumstances of our births.\""
    "\"Accept our emaciated bodies and del-\""
    if item_page_1 == True:
        menu:
            "Combine the ripped pages.":
                $showItemPage2 = False
                $cargo_buttons_enabled = False 
                $cargo_scroll_enabled = False
                #show screen combine_pages
                $ result = renpy.call_screen("combine_pages")
                if result:
                    jump combinePagesFinished
                $ renpy.pause()
    $showItemPage2 = False
    jump expression locationTracker

label examineKnife:
    $room_buttons_enabled = False
    $room_scroll_enabled = False
    t "You have the knife."
    jump expression locationTracker

label examineArm:
    $room_buttons_enabled = False
    $room_scroll_enabled = False
    if kitchenArmCooked == False and kitchenArmCut == False:
        t "You have a severed arm."
    elif kitchenArmCut == True:
        t "You have a severed arm that has been cut into smaller pieces."
    elif kitchenArmCooked == True:
        t "You have a pot with arm stew."
    jump expression locationTracker

label examineSpices:
    $room_buttons_enabled = False
    $room_scroll_enabled = False
    t "You have a few containers filled with various spices and herbs used for seasoning."
    jump expression locationTracker

label examineLighter:
    $room_buttons_enabled = False
    $room_scroll_enabled = False
    t "You have the lighter."
    jump expression locationTracker