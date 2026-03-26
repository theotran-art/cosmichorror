#image pdeathhag:
    #"images/death/pdeath1.png"
    #pause 2.0
    #"images/death/pdeath2.png"

#screen pdeathhagscreen:
    #add "pdeathhag"


image parasiteboom:
    "images/death/bloodsplat.png"
    pause 2.0

screen parasitedeath1:
    add "parasiteboom"

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
        t "After you finish speaking, you feel a sharp pain in your head."
        show black bckgd onlayer master
        show screen parasitedeath1 with dissolve
        hide cargoRoom
        "You died."
        show cargoRoom onlayer background
        hide screen parasitedeath1
        hide black bckgd
        hide screen suspicion_overlay
        $hagsus = 0
        jump cargo
    if cansus == 2:
        show black bckgd
        "cannibal killed u"
        $cansus = 0
        hide black bckgd
        hide screen suspicion_overlay
        jump kitchen
    if cann_lose == True:
        show black bckgd
        "cannibal killed u"
        $cansus = 0
        hide black bckgd
        hide screen suspicion_overlay
        jump kitchen
