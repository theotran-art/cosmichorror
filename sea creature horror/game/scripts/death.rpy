image pdeathhag:
    "images/death/pdeath1.png"
    pause 2.0
    "images/death/pdeath2.png"

screen pdeathhagscreen:
    add "pdeathhag"

label death:
    if hagsus == 2 and phag == False:
        h "\"You scheming little traitor. You don't even deserve to lay your heretic eyes upon her...\""
        show black bckgd onlayer master
        hide cargoRoom
        "You died."
        show cargoRoom onlayer background
        hide black bckgd
        hide screen suspicion_overlay
        $hagsus = 0
        jump cargo
    if hagsus == 2 and phag == True:
        show black bckgd onlayer master
        show screen pdeathhagscreen
        hide cargoRoom
        t "You feel a sharp pain in your head."
        "You died."
        show cargoRoom onlayer background
        hide black bckgd
        hide screen suspicion_overlay
        $hagsus = 0
        jump cargo
    if cann_lose == True:
        show black bckgd
        "cannibal killed u"
        $cansus = 0
        hide black bckgd
        hide screen suspicion_overlay
        $hagsus = 0
        jump kitchen

        
