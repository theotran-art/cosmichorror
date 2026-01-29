label minigametut:
    scene bckgex
    "testing random things"
    call screen clickables

screen clickables:
    imagebutton:
        pos (162,800)
        auto "drawer_%s.png" action Jump("clicked")
    imagebutton:
        pos (476,507)
        auto "clothes_%s.png" action Jump("clicked")
    imagebutton:
        pos (1255,527)
        auto "laptop_%s.png" action Jump("clicked")
        
        hovered Show()

label clicked:
    "you clicked on something!"