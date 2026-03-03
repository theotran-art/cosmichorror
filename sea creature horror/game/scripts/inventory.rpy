screen inventory():
    textbutton "Inventory":
        action Show("inventoryView"), Hide("inventory"), SetVariable("cargo_buttons_enabled", False), SetVariable("cargo_scroll_enabled", False)

screen inventoryView():
    tag menu  # prevents stacking with other menus

    modal True

    frame:
        align (0.01, 0.01)
        padding (30, 30)

        vbox:
            spacing 15
            text "Inventory"

            #page
            if item_page == True: #THIS IS COMPLETED PAGE
                textbutton "Page":
                    action Hide("inventoryView"), Show("inventory"), Jump("examinePage")
            if item_page_1 == True and page_combined == False:
                textbutton "Ripped page from book":
                    action Hide("inventoryView"), Show("inventory"), Jump("examinePage1")
            if item_page_2 == True and page_combined == False:
                textbutton "Ripped page from cultist":
                    action Hide("inventoryView"), Show("inventory"), Jump("examinePage2")
            #knife
            if item_knife == True:
                textbutton "Knife":
                    action Hide("inventoryView"), Show("inventory"), Jump("examineKnife")
            #lighter
            if item_lighter == True:
                textbutton "Lighter":
                    action Hide("inventoryView"), Show("inventory"), Jump("examineLighter")
            textbutton "Close":
                action Hide("inventoryView"), Show("inventory"), SetVariable("cargo_buttons_enabled", True), SetVariable("cargo_scroll_enabled", True)

label examinePage: #THIS IS COMPLETED PAGE
    $showItemPage = True
    t "You have a page that reads out the passage:"
    "\"O Mother of the Great Deep, we sever our love to our flesh to offer it to you alone, flaying our imperfect forms as penance for the circumstances of our births.\""
    "\"Accept our emaciated bodies and deliver us, for we yearn to be entangled in your cold embrace as the children of your new earth.\""
    $showItemPage = False
    jump cargo

label examinePage1: 
    $showItemPage = True
    t "You have a ripped page that reads out the passage:"
    "\"-iver us, for we yearn to be entangled in your cold emabrace as the children of your new earth.\""
    if item_page_2 == True:
        menu:
            "Combine the ripped pages.":
                $item_page = True
                "You piece the two sections together."
                $page_combined = True
    $showItemPage = False
    jump cargo

label examinePage2: 
    $showItemPage = True
    t "You have a ripped page that reads out the passage:"
    "\"O Mother of the Great Deep, we sever our love to our flesh to offer it to you alone, flaying our imperfect forms as penance for the circumstances of our births.\""
    "\"Accept our emaciated bodies and del-\""
    if item_page_1 == True:
        menu:
            "Combine the ripped pages.":
                $item_page = True
                "You piece the two sections together."
                $page_combined = True
    $showItemPage = False
    jump cargo

label examineKnife:
    t "You have the knife."
    jump cargo

label examineLighter:
    t "You have the page."
    jump cargo