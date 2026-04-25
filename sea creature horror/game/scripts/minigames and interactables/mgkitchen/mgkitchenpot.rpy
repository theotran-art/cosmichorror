init python:
    def drag_placed(drags, drop):
        if not drop:
            return

        d = drags[0].drag_name

        if drop.drag_name == "pot" and d not in store.placed_items:
            store.placed_items.append(d)

        return True

default placed_items = []
default draggable = None
default droppable = None
default armpieces = 0
default spices = 0

label mgkitchen_pot:
    $hide_inventory = True
    call screen mgkitchen_cook

    $ armpieces = len([i for i in placed_items if i in ["arm piece", "arm piece2", "arm piece3", "arm piece4"]])
    $ spices = placed_items.count("spices")

    #t "you added [draggable] into [droppable]"

    call mgarm_check

label mgarm_check:
    #image goodArmStew = ".png"
    #image badArmStew = ".png"
    
    if armpieces == 4 and spices == 1 and kitchenArmCutBad == False: #correct 
        show screen mgkitchen_cook_notfinished
        t "After putting all the ingredients in, you let it simmer for a while."
        show screen mgkitchen_cook_finished with fade
        hide screen mgkitchen_cook_notfinished
        t "Once the color of the water has turned murky, you find a bowl to serve the soup into."
        hide screen mgkitchen_cook_finished 
        $ kitchenArmCooked = True
        $ kitchenSpicesUsed = True
        $ showItemArm = True
        $ renpy.restart_interaction()
        show screen inv_items_imgs with fade
        t "Despite your unfamiliarity of ingredients of this nature, you feel like you did a good job."
        t "You hope that your efforts will be acceptable to the cultist."
        $ showItemArm = False
        jump kitchen
    elif armpieces == 4 and spices == 1 and kitchenArmCutBad == True:
        show screen mgkitchen_cook_notfinished
        t "After putting all the ingredients in, you let it simmer for a while."
        show screen mgkitchen_cook_finished with fade
        hide screen mgkitchen_cook_notfinished
        t "Once the color of the water has turned murky, you find a bowl to serve the soup into."
        hide screen mgkitchen_cook_finished 
        $ kitchenArmCooked = True
        $ kitchenArmCookedBad = True
        $ kitchenSpicesUsed = True
        $ showItemArm = True
        $ renpy.restart_interaction()
        show screen inv_items_imgs with fade
        t "Because of your unfamiliarity of ingredients of this nature, it doesn't look very good. It seems that your sloppy attempts at cutting the arm has made the overall dish look very messy."
        t "You hope that your efforts will be acceptable to the cultist."
        $ showItemArm = False
        jump kitchen
    else:
        jump mgkitchen_pot


screen mgkitchen_cook:
    #add ".png" #background

    #instructions

    draggroup:
        drag:
            drag_name "pot"
            xalign 0.99
            yalign 0.99
            #child ".png" #the image of the pot
            child "images/minigames/cooking/pot/pot (back).PNG"
            #text "pot"
            droppable True
            draggable False
        if "arm piece" not in placed_items:
            if kitchenArmCutBad == True:
                drag:
                    drag_name "arm piece"
                    xpos 20
                    ypos 200
                    child "images/minigames/arm_assets/arm_messy/arm_1.png"
                    draggable True
                    droppable False
                    dragged drag_placed
                    drag_raise True
            else:
                drag:
                    drag_name "arm piece"
                    xpos 20
                    ypos 200
                    child "images/minigames/arm_assets/arm_clean/arm_1.png" 
                    draggable True
                    droppable False
                    dragged drag_placed
                    drag_raise True
        if "arm piece2" not in placed_items:
            if kitchenArmCutBad == True:
                drag:
                    drag_name "arm piece2"
                    xpos 280
                    ypos 200
                    child "images/minigames/arm_assets/arm_messy/arm_2.png"
                    draggable True
                    droppable False
                    dragged drag_placed
                    drag_raise True
            else:
                drag:
                    drag_name "arm piece2"
                    xpos 280
                    ypos 200
                    child "images/minigames/arm_assets/arm_clean/arm_2.png" 
                    draggable True
                    droppable False
                    dragged drag_placed
                    drag_raise True
        if "arm piece3" not in placed_items:
            if kitchenArmCutBad == True:
                drag:
                    drag_name "arm piece3"
                    xpos 730
                    ypos 200
                    child "images/minigames/arm_assets/arm_messy/arm_3.png"
                    draggable True
                    droppable False
                    dragged drag_placed
                    drag_raise True
            else:
                drag:
                    drag_name "arm piece3"
                    xpos 730
                    ypos 200
                    child "images/minigames/arm_assets/arm_clean/arm_3.png" 
                    draggable True
                    droppable False
                    dragged drag_placed
                    drag_raise True
        if "arm piece4" not in placed_items:
            if kitchenArmCutBad == True:
                drag:
                    drag_name "arm piece4"
                    xpos 1050
                    ypos 200
                    child "images/minigames/arm_assets/arm_messy/arm_4.png"
                    draggable True
                    droppable False
                    dragged drag_placed
                    drag_raise True
            else:
                drag:
                    drag_name "arm piece4"
                    xpos 1050
                    ypos 200
                    child "images/minigames/arm_assets/arm_clean/arm_4.png" 
                    draggable True
                    droppable False
                    dragged drag_placed
                    drag_raise True
        if "spices" not in placed_items:
            drag:
                drag_name "spices"
                xpos 1600
                ypos 150
                child "images/minigames/cooking/herb.png" #the image of the pot
                draggable True
                droppable False
                dragged drag_placed
                drag_raise True
    
    add "images/minigames/cooking/pot/pot water (clear).PNG":
        xalign 0.99
        yalign 0.99
        
    add "images/minigames/cooking/pot/pot (front).png":
        xalign 0.99
        yalign 0.99

    text "Put all the ingredients into the pot.":
        xalign 0.5
        yalign 0.13
        font "fonts/fisherman_2/Fisherman-Regular.otf"
        size 50

screen mgkitchen_cook_notfinished:
    add "images/minigames/cooking/pot/pot (back).png":
        xalign 0.99
        yalign 0.99

    add "images/minigames/cooking/pot/pot water (clear).PNG":
        xalign 0.99
        yalign 0.99
        
    add "images/minigames/cooking/pot/pot (front).png":
        xalign 0.99
        yalign 0.99

screen mgkitchen_cook_finished:
    tag mgkitchen_cook_finished

    add "images/minigames/cooking/pot/pot (back).png":
        xalign 0.99
        yalign 0.99

    add "images/minigames/cooking/pot/pot water (murky).PNG":
        xalign 0.99
        yalign 0.99
        
    add "images/minigames/cooking/pot/pot (front).png":
        xalign 0.99
        yalign 0.99
