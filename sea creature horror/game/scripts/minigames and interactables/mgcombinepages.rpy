init python:
    def dragged_func(drags, drop):
        if not drop:
            return

        dragged = drags[0]

        if dragged.drag_name == "dragpage1" and drop.drag_name == "dragpage2":
            return True

screen combine_pages:
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
            image "images/items/cargo/page2.png"
        #book piece
        drag:
            xpos 0.1
            ypos 0.1
            drag_raise True
            draggable True
            drag_name "dragpage1"
            dragged dragged_func
            dropped Return(True)
            image "images/items/cargo/page1.png"

label combinePagesFinished:
    hide screen combine_pages
    $showItemPage1 = False
    $showItemPage2 = False
    $showItemPage = True
    $item_page = True
    "You piece the two sections together."
    $page_combined = True
    $showItemPage = False
    jump cargo
