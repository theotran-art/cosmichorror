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

            # KEY
            if item_page == True:
                textbutton "Page":
                    action Jump("examinePage")
            textbutton "Close":
                action Hide("inventoryView"), Show("inventory")

label examinePage:
    "You have the page."
    jump cargo