label kitchenEnter:
    hide screen suspicion_overlay

label kitchen:
    $kitchen_buttons_enabled = False

    #show screen kitchenRoom

    if item_knife == False:
        p1 "YOU NEED HIS HOLY BLADE." #i wrote this, replace with aidan's writing
        
    #TEMP MENU FOR ACESSS
    menu:
        "Talk to Cannibal":
            jump cannibaltalk
    #$kitchen_scroll_enabled = True
    #label pauseKitchen:
        #window hide
        #$kitchen_buttons_enabled = True
        #show screen inventory 
        #pause
        #jump pauseKitchen
    #window auto

#screen kitchenRoom:
    #pannable view of room
    #viewport id "kitchenScene":
        #area (0, 0, 1920, 1080) #size of screen (leave the same)
        #child_size (1920, 1080) #change based on image size

        #if kitchen_scroll_enabled:
            #edgescroll (150, 1400) #how fast the scrolling is (horizontal_speed, vertical_speed)
        #else: 
            #edgescroll (0,0)
 
        #add "images/backgrounds/kitchen.png" #name of the background image
        
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
    
label kitchenItemName:
    $kitchen_scroll_enabled = False
    $kitchen_buttons_enabled = False
    t "WIP"
    jump kitchen


label kitchenDoor:
    $kitchen_scroll_enabled = False
    $kitchen_buttons_enabled = False
    if page_combined == False and item_page_1 == False or item_page_2 == False:
        t "You should probably try and gather what you can from this room first."
        jump kitchen
    if page_combined == False and item_page_1 == True and item_page_2 == True:
        t "You have what you need, but you should repair the page first."
        jump kitchen
    #if ITEM == True:
        t "An inconspicuous door. Should you enter?"
        menu:
            "Enter.":
                jump moonpoolEnter
            "Turn away.":
                jump kitchen