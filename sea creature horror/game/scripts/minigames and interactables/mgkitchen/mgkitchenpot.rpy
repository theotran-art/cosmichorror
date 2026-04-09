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

    $ armpieces = len([i for i in placed_items if i in ["arm piece", "arm piece2"]])
    $ spices = placed_items.count("spices")

    #t "you added [draggable] into [droppable]"

    call mgarm_check

label mgarm_check:
    #image goodArmStew = ".png"
    #image badArmStew = ".png"

    if armpieces == 2 and spices == 1 and kitchenArmCutBad == False: #correct 
        show screen mgkitchen_cook_notfinished
        t "After putting all the ingredients in, you let it simmer for a while."

        show screen mgkitchen_cook_finished with fade
        hide screen mgkitchen_cook_notfinished

        t "Once the color of the water has turned murky, you find a bowl to serve the soup into."

        hide screen mgkitchen_cook_finished with fade

        #show goodArmStew
        t "Despite your unfamiliarity of ingredients of this nature, you feel like you did a good job."
        $ kitchenArmCooked = True
        jump kitchen
    elif armpieces == 2 and spices == 1 and kitchenArmCutBad == True:
        t "After putting all the ingredients in, you let it simmer for a while."
        t "Once the color of the water has turned murky, you find a bowl to serve the soup into."
        #show badArmStew
        t "Because of your unfamiliarity of ingredients of this nature, it doesn't look very good. It seems that your sloppy attempts at cutting the arm has made the overall dish look very messy."
        t "You hope that your efforts will be acceptable to the cultist."
        $ kitchenArmCooked = True
        $ kitchenArmCookedBad = True
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
            drag:
                drag_name "arm piece"
                xpos 300
                ypos 200
                #child ".png" #the image of the pot
                text "arm1"
                draggable True
                droppable False
                dragged drag_placed
                drag_raise True
        if "arm piece2" not in placed_items:
            drag:
                drag_name "arm piece2"
                xpos 750
                ypos 220
                #child ".png" #the image of the pot
                text "arm2"
                draggable True
                droppable False
                dragged drag_placed
                drag_raise True
        if "spices" not in placed_items:
            drag:
                drag_name "spices"
                xpos 1450
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
        yalign 0.10 
        font "fonts/fisherman_2/Fisherman-Regular.otf"
        size 60

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
