screen inventoryView():
    layer "ui"
    tag menu  # prevents stacking with other menus

    modal True

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
            text "Inventory" size 28

            #page
            if item_page == True: #THIS IS COMPLETED PAGE
                textbutton "{size=20}Page":
                    action Hide("inventoryView"), SetVariable("inventory_open", False), Jump("examinePage")
            if item_page_1 == True and page_combined == False:
                textbutton "{size=20}Ripped page from book":
                    action Hide("inventoryView"), SetVariable("inventory_open", False), Jump("examinePage1")
            if item_page_2 == True and page_combined == False:
                textbutton "{size=20}Ripped page from cultist":
                    action Hide("inventoryView"), SetVariable("inventory_open", False), Jump("examinePage2")
            #knife
            if item_knife == True:
                textbutton "{size=20}Knife":
                    action Hide("inventoryView"), SetVariable("inventory_open", False), Jump("examineKnife")
            #lighter
            if item_lighter == True:
                textbutton "{size=20}Lighter":
                    action Hide("inventoryView"), SetVariable("inventory_open", False), Jump("examineLighter")
            textbutton "{size=22}Close":
                action Hide("inventoryView"), SetVariable("inventory_open", False), SetVariable("cargo_buttons_enabled", True), SetVariable("cargo_scroll_enabled", True)

label examinePage: #THIS IS COMPLETED PAGE
    $showItemPage = True
    t "You have a page that reads out the passage:"
    "\"O Mother of the Great Deep, we sever our love to our flesh to offer it to you alone, flaying our imperfect forms as penance for the circumstances of our births.\""
    "\"Accept our emaciated bodies and deliver us, for we yearn to be entangled in your cold embrace as the children of your new earth.\""
    $showItemPage = False
    jump cargo

label examinePage1: 
    $showItemPage1 = True
    t "You have a ripped page that reads out the passage:"
    "\"-iver us, for we yearn to be entangled in your cold emabrace as the children of your new earth.\""
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
    jump cargo

label examinePage2: 
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
    jump cargo

label examineKnife:
    t "You have the knife."
    jump cargo

label examineLighter:
    t "You have the page."
    jump cargo