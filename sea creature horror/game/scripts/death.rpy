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
        show black bckgd onlayer master with fade
        hide cargoRoom
        "You died."
        show cargoRoom onlayer background with fade
        hide black bckgd
        hide screen suspicion_overlay
        $hagsus = 0
        jump cargo
    if hagsus == 2 and phag == True:
        t "After you finish speaking, you feel a sharp pain in your head."
        show black bckgd onlayer master with fade
        show screen parasitedeath1 with dissolve
        hide cargoRoom
        "You died."
        show cargoRoom onlayer background with fade
        hide screen parasitedeath1
        hide black bckgd
        hide screen suspicion_overlay
        $hagsus = 0
        jump cargo
    if cansus == 2:
        c "You've disappointed me, little ghost."
        show black bckgd onlayer master with fade
        hide kitchenRoom
        "You died."
        show kitchenRoom onlayer background with fade
        hide black bckgd
        hide screen suspicion_overlay
        $cansus = 0
        jump kitchen
    if cann_lose == True:
        t "After failing to defend yourself, you feel his teeth sink into your neck."
        t "You fall to the ground grasping at your throat in agony."
        t "Your vision starts to blur."
        c "I didn't take you for a liar, little ghost."
        show black bckgd onlayer master with fade
        hide kitchenRoom
        "You died."
        show kitchenRoom onlayer background with fade
        hide black bckgd
        hide screen suspicion_overlay
        $cansus = 0
        jump kitchen
