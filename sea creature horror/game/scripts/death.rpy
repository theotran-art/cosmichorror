#image pdeathhag:
    #"images/death/pdeath1.png"
    #pause 2.0
    #"images/death/pdeath2.png"

#screen pdeathhagscreen:
    #add "pdeathhag"

# Fade to black

image parasiteboom:
    "images/death/bloodsplat.png"
    pause 2.0

screen parasitedeath1:
    add "parasiteboom"

label death:
    if skesus == 2:
        s "It's a shame you're too far gone under its influence."
        s "At least you'll be able to give me a developed parasite to turn in for evidence."
        t "She darts forward, and you feel a needle sink into your skin."
        hide screen suspicion_overlay
        hide screen moonpoolRoom 
        show expression Solid("#000") as fade_black onlayer master with fade
        "You died."
        hide screen moonpoolRoom
        show screen moonpoolRoom onlayer master
        hide fade_black with fade
        $skesus = 0
        jump moonpool
    if hagsus == 2 and phag == False:
        h "\"You scheming little traitor. You don't even deserve to lay your heretic eyes upon her...\""
        hide screen suspicion_overlay
        hide screen cargoRoom 
        show expression Solid("#000") as fade_black onlayer master with fade
        "You died."
        hide screen cargoRoom
        show screen cargoRoom onlayer master
        hide fade_black with fade
        $hagsus = 0
        jump cargo
    if hagsus == 2 and phag == True:
        t "After you finish speaking, you feel a sharp pain in your head."
        hide screen suspicion_overlay
        hide screen cargoRoom 
        show expression Solid("#000") as fade_black onlayer master with fade
        "You died."
        hide screen cargoRoom
        show screen cargoRoom onlayer master
        hide fade_black with fade
        $hagsus = 0
        jump cargo
    if cansus == 2:
        c "You've disappointed me, little ghost."
        hide screen suspicion_overlay
        hide screen kitchenRoom 
        "You died."
        hide screen kitchenRoom
        show screen kitchenRoom onlayer master
        hide fade_black with fade
        $cansus = 0
        jump kitchen
    if cann_lose == True:
        t "After failing to defend yourself, you feel his teeth sink into your neck."
        t "You fall to the ground grasping at your throat in agony."
        t "Your vision starts to blur."
        c "I didn't take you for a liar, little ghost."
        hide screen suspicion_overlay
        hide screen kitchenRoom 
        "You died."
        hide screen kitchenRoom
        show screen kitchenRoom onlayer master
        hide fade_black with fade
        $cansus = 0
        jump kitchen
