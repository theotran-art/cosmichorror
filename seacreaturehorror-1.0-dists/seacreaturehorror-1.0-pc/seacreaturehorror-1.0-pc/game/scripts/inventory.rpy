screen inventory():
    textbutton "Inventory":
        action Show("inventoryView"), Hide("inventory")

screen inventoryView():
    tag menu  # prevents stacking with other menus

    modal True

    frame:
        align (0.5, 0.5)
        padding (30, 30)

        vbox:
            spacing 15
            text "Inventory"

            #page
            if item_page == True:
                textbutton "Page":
                    action Hide("inventoryView"), Show("inventory"), Jump("examinePage")
            #knife
            if item_knife == True:
                textbutton "Knife":
                    action Hide("inventoryView"), Show("inventory"), Jump("examineKnife")
            #lighter
            if item_lighter == True:
                textbutton "Lighter":
                    action Hide("inventoryView"), Show("inventory"), Jump("examineLighter")
            textbutton "Close":
                action Hide("inventoryView"), Show("inventory")

label examinePage:
    t "You have a page that reads out the passage:"
    "\"O Mother of the Great Deep, we sever our love to our flesh to offer it to you alone, flaying our imperfect forms as penance for the circumstances of our births.\""
    "\"Accept our immaciated bodies and deliver us, for we yearn to be entangled in your cold embrace as the children of your new earth.\""
    jump cargo

label examineKnife:
    t "You have the knife."
    jump cargo

label examineLighter:
    t "You have the page."
    jump cargo