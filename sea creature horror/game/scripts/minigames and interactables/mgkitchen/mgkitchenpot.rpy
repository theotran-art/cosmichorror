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

    call screen mgkitchen_cook

    $ armpieces = len([i for i in placed_items if i in ["arm piece", "arm piece2"]])
    $ spices = placed_items.count("spices")

    #t "you added [draggable] into [droppable]"

    call mgarm_check

label mgarm_check:
    #image goodArmStew = ".png"
    #image badArmStew = ".png"

    if armpieces == 2 and spices == 1 and kitchenArmCutBad == False: #correct
        t "After putting all the ingredients in, you let it simmer for a while."
        t "Once the color of the water has turned murky, you find a bowl to serve the soup into."
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
    text "Put all the ingredients into the pot.":
        pos (70, 800)

    draggroup:
        drag:
            drag_name "pot"
            xpos 550
            ypos 600
            #child ".png" #the image of the pot
            text "POT"
            droppable True
            draggable False
        if "arm piece" not in placed_items:
            drag:
                drag_name "arm piece"
                xpos 300
                ypos 100
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
                ypos 120
                #child ".png" #the image of the pot
                text "arm2"
                draggable True
                droppable False
                dragged drag_placed
                drag_raise True
        if "spices" not in placed_items:
            drag:
                drag_name "spices"
                xpos 1250
                ypos 150
                #child ".png" #the image of the pot
                text "spices"
                draggable True
                droppable False
                dragged drag_placed
                drag_raise True