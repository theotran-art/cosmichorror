


transform inventory_fade(showing): # transition for inventory fade
    linear 0.25 alpha (1.0 if showing else 0.0)

screen inventoryView():
    tag menu  # prevents stacking with other menus

    modal True

    on "show":
        at fade_in

    add "gui/customui/inventory.png":
        xalign 1.0
        yalign 0.0
        xoffset 6
        yoffset 175


    vbox:
        xalign 1.0
        yalign 0.0
        xoffset -37
        yoffset 205
        text "Inventory" size 28 font "fonts/fisherman_2/Fisherman-Regular.otf" color "#3d707a"

    #CARGO
        #page
        if item_page == True: #THIS IS COMPLETED PAGE
            imagebutton:
                auto "images/inv_items/page_%s.png"
                xalign 0.5  

            #textbutton "Page":
                #text_size 24
                #text_font "fonts/Sedan_SC/SedanSC-Regular.ttf"
                #text_hover_color "#ffffff"
                #text_color "#b4dee6"

                action [
                    Hide("inventoryView"),
                    SetVariable("inventory_open", False),
                    Jump("examinePage")
                ]

                at transform:
                    xysize (90, 90)
        if item_page_1 == True and page_combined == False:
            imagebutton:
                auto "images/inv_items/page1_%s.png"
                xalign 0.5
                
            #textbutton "Ripped page from book":
                #text_size 24
                #text_font "fonts/Sedan_SC/SedanSC-Regular.ttf"
                #text_hover_color "#ffffff"
                #text_color "#b4dee6"

                action [
                    Hide("inventoryView"),
                    SetVariable("inventory_open", False),
                    Jump("examinePage1")
                ]

                at transform:
                    xysize (90, 90)
        if item_page_2 == True and page_combined == False:
            imagebutton:
                auto "images/inv_items/page2_%s.png"
                xalign 0.5

            #textbutton "Ripped page from cultist":
                #text_size 24
                #text_font "fonts/Sedan_SC/SedanSC-Regular.ttf"
                #text_hover_color "#ffffff"
                #text_color "#b4dee6"

                action [
                    Hide("inventoryView"),
                    SetVariable("inventory_open", False),
                    Jump("examinePage2")
                ]

                at transform:
                    xysize (90, 90)
    #KITCHEN
        #knife
        if item_knife == True:
            imagebutton:
                auto "images/inv_items/knife_%s.png"
                xalign 0.5

            #textbutton "Knife":
                #text_size 24
                #text_font "fonts/Sedan_SC/SedanSC-Regular.ttf"
                #text_hover_color "#ffffff"
                #text_color "#b4dee6"

                action [
                    Hide("inventoryView"),
                    SetVariable("inventory_open", False),
                    Jump("examineKnife")
                ]

                at transform:
                    xysize (90, 90)
        #arm
        if kitchenArm == True and kitchenStew == False:
            if kitchenArmCooked == True:
            #imagebutton:
                #auto "images/inv_items/_%s.png"
                #xalign 0.5

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

                    at transform:
                        xysize (90, 90)
            else:
                #imagebutton:
                    #auto "images/inv_items/_%s.png"
                    #xalign 0.5
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

                    at transform:
                        xysize (90, 90)
        #spices
        if kitchenSpices == True:
            imagebutton:
                auto "images/inv_items/herb_%s.png"
                xalign 0.5

            #textbutton "Spices and herbs":
                #text_size 24
                #text_font "fonts/Sedan_SC/SedanSC-Regular.ttf"
                #text_hover_color "#ffffff"
                #text_color "#b4dee6"

                action [
                    Hide("inventoryView"),
                    SetVariable("inventory_open", False),
                    Jump("examineSpices")
                ]

                at transform:
                    xysize (90, 90)
            #key
            if kitchenDoorKey == True:
                #auto "images/inv_items/_%s.png"
                #xalign 0.5

                textbutton "Key":
                    text_size 24
                    text_font "fonts/Sedan_SC/SedanSC-Regular.ttf"
                    text_hover_color "#ffffff"
                    text_color "#b4dee6"

                    action [
                        Hide("inventoryView"),
                        SetVariable("inventory_open", False),
                        Jump("examineKey")
                    ]

                    at transform:
                        xysize (90, 90)

    #MOONPOOL
        #lighter
        if item_lighter == True:
            imagebutton:
                auto "images/inv_items/lighter_%s.png"
                xalign 0.5

            #textbutton "Lighter":
                #text_size 24
                #text_font "fonts/Sedan_SC/SedanSC-Regular.ttf"
                #text_hover_color "#ffffff"
                #text_color "#b4dee6"

                action [
                    Hide("inventoryView"),
                    SetVariable("inventory_open", False),
                    Jump("examineLighter")
                ]

                at transform:
                    xysize (90, 90)
        #close inventory
        #textbutton "{size=22}Close":
            #action Hide("inventoryView"), SetVariable("inventory_open", False), SetVariable("cargo_buttons_enabled", True), SetVariable("cargo_scroll_enabled", True)

label examinePage: #THIS IS COMPLETED PAGE\
    show screen inv_items_imgs
    $hide_inventory = True
    $room_buttons_enabled = False
    $room_scroll_enabled = False
    $showItemPage = True
    t "You have the page." 
    t "It reads out the passage:"
    "\"O Mother of the Great Deep, we sever our love to our flesh to offer it to you alone, flaying our imperfect forms as penance for the circumstances of our births.\""
    "\"Accept our emaciated bodies and deliver us, for we yearn to be entangled in your cold embrace as the children of your new earth.\""
    $showItemPage = False
    hide screen inv_items_imgs
    jump expression locationTracker

label examinePage1: 
    show screen inv_items_imgs
    $hide_inventory = True
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
    hide screen inv_items_imgs
    jump expression locationTracker

label examinePage2: 
    show screen inv_items_imgs
    $hide_inventory = True
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
    hide screen inv_items_imgs
    jump expression locationTracker

label examineKnife:
    show screen inv_items_imgs
    $hide_inventory = True
    $room_buttons_enabled = False
    $room_scroll_enabled = False
    $showItemKnife = True
    t "You have the knife."
    $showItemKnife = False
    hide screen inv_items_imgs
    jump expression locationTracker

label examineArm:
    show screen inv_items_imgs
    $hide_inventory = True
    $room_buttons_enabled = False
    $room_scroll_enabled = False
    $showItemArm = True
    if kitchenArmCooked == True:
        t "You have a bowl of arm stew."
    elif kitchenArmCut == True:
        t "You have a severed arm that has been cut into smaller pieces."
    elif kitchenArmCooked == False and kitchenArmCut == False:
        t "You have a severed arm."
    $showItemArm = False
    hide screen inv_items_imgs
    jump expression locationTracker

label examineSpices:
    show screen inv_items_imgs
    $hide_inventory = True
    $room_buttons_enabled = False
    $room_scroll_enabled = False
    $showItemSpices = True
    t "You have a sprig of an herb used for seasoning."
    $showItemSpices = False
    hide screen inv_items_imgs
    jump expression locationTracker

label examineKey:
    show screen inv_items_imgs
    $hide_inventory = True
    $room_buttons_enabled = False
    $room_scroll_enabled = False
    $showItemKey = True
    t "You have a key. It likely opens the door next to the cultist."
    $showItemKey = False
    hide screen inv_items_imgs
    jump expression locationTracker

label examineLighter:
    show screen inv_items_imgs
    $hide_inventory = True
    $room_buttons_enabled = False
    $room_scroll_enabled = False
    $showItemLighter = True
    t "You have the lighter."
    $showItemLighter = False
    hide screen inv_items_imgs
    jump expression locationTracker