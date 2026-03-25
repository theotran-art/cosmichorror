init python:
    def dragged_func(drags, drop):
        if not drop:
            return

        dragged = drags[0]

        if dragged.drag_name == "dragpage1" and drop.drag_name == "dragpage2":
            return True

screen mg_kitchen_arm_cook:
    draggroup:
        #hag piece
        drag:
            xalign 0.5
            yalign 0.5
            drag_raise True
            draggable False
            droppable True
            drag_name "dragpage2"
            dragged dragged_func
            #image "images/items/cargo/page2.png"
            text "arm" size 50
        #book piece
        drag:
            xpos 0.1
            ypos 0.1
            drag_raise True
            draggable True
            drag_name "dragpage1"
            dragged dragged_func
            dropped Return(True)
            #image "images/items/cargo/page1.png"
            text "pot" size 50

label mg_kitchen_arm_cook_finished:
    hide screen mg_kitchen_arm_cook
    t "You piece the two sections together."
    
    jump kitchen
