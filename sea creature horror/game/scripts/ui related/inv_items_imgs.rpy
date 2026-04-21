screen inv_items_imgs:
    if showCargoBook:
        add Solid("#00000088")

        # Centered image
        add "images/items/cargo/book.png":
            xalign 0.5
            yalign 0.5

    if showItemPage:
        add Solid("#00000088")

        # Centered image
        add "images/items/cargo/page.png":
            xalign 0.5
            yalign 0.5

    if showItemPage1:
        add Solid("#00000088")

        # Centered image
        add "images/items/cargo/page1.png":
            xalign 0.5
            yalign 0.5

    if showItemPage2:
        add Solid("#00000088")

        # Centered image
        add "images/items/cargo/page2.png":
            xalign 0.5
            yalign 0.5

    if showItemKnife:
        add Solid("#00000088")

        # Centered image
        add "images/items/kitchen/knife.png":
            xalign 0.5
            yalign 0.5
    
    if showItemArm:
        add Solid("#00000088")

        # Centered image
        if kitchenArmCooked == True:
            add "images/items/.png":
                xalign 0.5
                yalign 0.5
        elif kitchenArmCut == True and kitchenArmCutBad == True:
            add "images/minigames/arm_assets/arm_messy/arm.png":
                xalign 0.5
                yalign 0.5
        elif kitchenArmCut == True and kitchenArmCutBad == False:
            add "images/minigames/arm_assets/arm_clean/arm.png":
                xalign 0.5
                yalign 0.5
        elif kitchenArmCooked == False and kitchenArmCut == False:
            add "images/minigames/arm_assets/arm_whole.png":
                xalign 0.5
                yalign 0.5
    
    if showItemSpices:
        add Solid("#00000088")

        # Centered image
        add "images/minigames/cooking/herb.png":
            xalign 0.5
            yalign 0.5

    if showItemKey:
        add Solid("#00000088")

        # Centered image
        add "images/items/kitchen/key.png":
            xalign 0.5
            yalign 0.5

    if showItemLighter:
        add Solid("#00000088")

        # Centered image
        add "images/items/moonpool/lighter.png":
            xalign 0.5
            yalign 0.5
    
    if showItemSpecimen:
        add Solid("#00000088")

        # Centered image
        add "images/items/moonpool/specimen.png":
            xalign 0.5
            yalign 0.5

    if showItemDiagram:
        add Solid("#00000088")

        # Centered image
        add "images/items/moonpool/diagram.png":
            xalign 0.5
            yalign 0.5

    if showItemDiagnosis:
        add Solid("#00000088")

        # Centered image
        add "images/items/moonpool/diagnosis.png":
            xalign 0.5
            yalign 0.5