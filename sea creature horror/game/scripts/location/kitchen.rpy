label kitchenEnter:
    hide screen suspicion_overlay

label kitchen:
    #variable stuff
    $locationTracker = "kitchen"
    
    #screen transitions
    show screen kitchenRoom onlayer master
    $kitchen_buttons_enabled = False
    show screen kitchenRoom onlayer master
    $hide_inventory = False
    show screen uiWindow onlayer ui with fade

    #persistent parasite quest
    if item_knife == False:
        p2 "YOU NEED HIS BLADE."
    
    #reset sus overlay
    #if item_knife == True and hagsus >= 1:
        #hide screen suspicion_overlay with fade
        
    #loop for point and click
    #$kitchen_scroll_enabled = True
    #label pauseKitchen:
        #window hide
        #$kitchen_buttons_enabled = True
        #pause
        #jump pauseKitchen
    #window auto 

    #TEMP MENU FOR ACESSS
    menu:
        "Talk to Cannibal":
            jump cannibaltalk
        "Cutting board":
            jump kitchenCuttingBoard
        "Pot":
            jump kitchenPot
        "Cabinets":
            jump kitchenCabinet
        "Bodies":
            jump kitchenBodies
        "Door":
            jump kitchenDoor

screen kitchenRoom:
    #pannable view of room
    viewport id "kitchenScene":
        area (0, 0, 1920, 1080) #size of screen (leave the same)
        child_size (1920, 1080) #change based on image size

        if kitchen_scroll_enabled:
            edgescroll (150, 1400) #how fast the scrolling is (horizontal_speed, vertical_speed)
        else: 
            edgescroll (0,0)
 
        add "images/backgrounds/kitchen.png" #name of the background image
        
        #if kitchen_buttons_enabled == True:
            #imagebutton: #for 
                #pos (340,945) #where it appears on the screen
                #auto "images/items/kitchen/_%s.png" action Hide("inventory"), Jump("kitchenA")
            #add more imgbutt if needed

    #IMAGES THAT SHOW UP AFTER CLICKING AN ITEM (CLOSE UP)
    #if showKitchenITEM:
        #add Solid("#00000088")

        # Centered image
        #add "images/items/kitchen/.png":
            #xalign 0.5
            #yalign 0.5


#writing for clickable items
label kitchenDoor:
    $kitchen_scroll_enabled = False
    $kitchen_buttons_enabled = False
    if kitchenDoorKey == False:
        t "It's locked."
        jump kitchen
    elif kitchenDoorKey == True:
        t "A locked door, for which you have the key. Enter?"
        menu:
            "Enter.":
                jump moonpoolEnter
            "Turn away.":
                jump kitchen

label kitchenCuttingBoard:
    $kitchen_scroll_enabled = False
    $kitchen_buttons_enabled = False
    if kitchenArm == False:
        t "A small wooden cutting board with countless knife marks in it. You're not sure who's blood stains the surface, and you're not sure you want to."
        jump kitchen
    elif kitchenArm == True and kitchenArmCut == False:
        t "A cutting board. You can use this to cut the arm into smaller pieces."
        menu:
            "Use the cutting board.":
                jump mgKitchenArmCut
    elif kitchenArm == True and kitchenArmCut == True and kitchenArmCooked == False:
        t "You've mutilated the arm plenty. It should be able to be cooked at this point."
        jump kitchen
    else:
        t "A small wooden cutting board with countless knife marks in it."
        jump kitchen

label kitchenPot:
    $kitchen_scroll_enabled = False
    $kitchen_buttons_enabled = False
    t "WIP"
    jump kitchen

label kitchenCabinet:
    $kitchen_scroll_enabled = False
    $kitchen_buttons_enabled = False
    t "They're full of dead fish. It smells like nothing you've ever experienced. You've never had a gag reflex, but you seem to have found one."
    if kitchenSpices == False:
        t "A small rack of spices and herbs sits on the lowermost shelf."
        menu:
            "Take spices and herbs.":
                $kitchenSpices = True
                jump kitchen
    elif kitchenSpices == True:
        t "A small rack of spices and herbs sits on the lowermost shelf."
        t "You've already taken some."
        jump kitchen

label kitchenBodies:
    $kitchen_scroll_enabled = False
    $kitchen_buttons_enabled = False
    t "More bodies. These seem in a far worse shape than the others."
    t "Is he... eating them?"
    jump kitchen
