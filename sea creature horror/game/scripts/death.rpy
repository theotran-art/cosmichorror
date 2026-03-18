image pdeathhag:
    "images/death/pdeath1.png"
    pause 2.0
    "images/death/pdeath2.png"

screen pdeathhagscreen:
    add "pdeathhag"

label death:
    if hagsus == 2 and phag == False:
        h "\"You scheming little traitor. You don't even deserve to lay your heretic eyes upon her...\""
        hide screen cargoRoom
        show black bckgd
        "You died."
        $hagsus = 0
        jump cargo
    if hagsus == 2 and phag == True:
        hide screen cargoRoom
        show black bckgd
        show screen pdeathhagscreen
        t "You feel a sharp pain in your head."
        "You died."
        $hagsus = 0
        jump cargo
    if cann_lose == True:
        show black bckgd
        "cannibal killed u"
        jump kitchen

        
