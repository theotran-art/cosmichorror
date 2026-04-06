label cargoEnter:
    play music "music/bgm.wav" fadein 3.0

label cargo:

    #variable reset incase of bugs
    $characterTalk = False
    $showItemPage = False
    $showItemPage1 = False
    $showItemPage2 = False
    $locationTracker = "cargo"

    #screen transitions
    $room_buttons_enabled = False
    $hide_inventory = False
    show screen cargoRoom onlayer master

    #persistent parasite quest
    if (item_page_1 == False or item_page_2 == False) and item_page == False:
        p1 "YOU NEED HER HOLY TEXT."
    elif item_page_1 == True and item_page_2 == True and page_combined == False and item_page == False:
        p1 "REPAIR THE TEXT."
        
    #reset sus overlay
    if item_page == True and hagsus >= 1:
        hide screen suspicion_overlay with fade

    #loop for point and click
    $room_scroll_enabled = True
    label pauseCargo:
        window hide
        $room_buttons_enabled = True
        pause
        jump pauseCargo
    window auto 

#CARGO SCREENS/IMAGE BUTTONS

screen cargoRoom:
    #pannable view of room
    viewport id "cargoScene":
        area (0, 0, 1920, 1080) #size of screen (leave the same)
        child_size (5497, 1620) #change based on image size
        add "images/backgrounds/cargo.png" #name of the background image

        if room_scroll_enabled == True and locationTracker == "cargo" and allow_edge_scroll():
            edgescroll (150, 1400) #how fast the scrolling is (horizontal_speed, vertical_speed)
        else: 
            edgescroll (0,0)
        
        if room_buttons_enabled == True and locationTracker == "cargo":
            imagebutton: #for dead bodies
                pos (340,945) #where it appears on the screen
                auto "images/items/cargo/bodies_%s.png" action SetVariable("hide_inventory", True), Jump("cargoDeadBodies")
            #imagebutton: #for crates
                #pos (3000,600) #where it appears on the screen
                #auto "images/items/cargo/crates_%s.png" action Jump("cargoCrates")
            imagebutton: #for the window
                pos (874,371)
                auto "images/items/cargo/window_%s.png" action SetVariable("hide_inventory", True), Jump("cargoWindow")    
            imagebutton: #for the cargo door
                pos (4700,130)
                auto "images/items/cargo/door_%s.png" action SetVariable("hide_inventory", True), Jump ("cargoDoor")
            imagebutton: #for statuette
                pos (2352,994) #where it appears on the screen
                auto "images/items/cargo/figurine_%s.png" action SetVariable("hide_inventory", True), Jump("cargoStatuette")
            imagebutton: #for book
                pos (2937,800) #where it appears on the screen
                auto "images/items/cargo/book_%s.png" action SetVariable("hide_inventory", True), Jump("cargoBook")
            #imagebutton: #for pendant
                #pos (0,0) #where it appears on the screen
                #auto "images/items/_%s.png" action Jump("cargoPendant")
            imagebutton: #for poster
                pos (2375,190) #where it appears on the screen
                auto "images/items/cargo/poster1_%s.png" action SetVariable("hide_inventory", True), Jump("cargoPoster")
            imagebutton: #for poster2
                pos (1729,226) #where it appears on the screen
                auto "images/items/cargo/poster2_%s.png" action SetVariable("hide_inventory", True), Jump("cargoPoster") 
            imagebutton: #for the Hag
                pos (4080,750) #where it appears on the screen
                auto "images/sprites/hag_%s.png" action SetVariable("hide_inventory", True), Jump("hagtalk")

    #IMAGES THAT SHOW UP AFTER CLICKING AN ITEM (CLOSE UP)
    if showCargoBook:
        add Solid("#00000088")

        # Centered image
        add "images/items/cargo/book.png":
            xalign 0.5
            yalign 0.5

    if showItemPage:
        add Solid("#00000088")

        # Centered image
        add "images/items/cargo/page.png":
            xalign 0.5
            yalign 0.5
    
    if showItemPage1:
        add Solid("#00000088")

        # Centered image
        add "images/items/cargo/page1.png":
            xalign 0.5
            yalign 0.5
    
    if showItemPage2:
        add Solid("#00000088")

        # Centered image
        add "images/items/cargo/page2.png":
            xalign 0.5
            yalign 0.5

image windowCargoCloseup:
    "images/backgrounds/windowCargoCloseup.png"

image windowCargo:
    "images/backgrounds/windowCargo.png"

#imagebutton: #make sure the image has normal and _hover 
            #pos (0,0) #where it appears on the screen
            #auto "_%s.png" action Jump("") #auto "IMAGE NAME OF CLICKABLE_%s.png" action Jump("WHAT HAPPENS WHEN CLICKED") // make sure that it jumps to a label!

#CARGO CLICKABLE TEXT

label cargoDeadBodies:
    $room_buttons_enabled = False
    $room_scroll_enabled = False
    t "Disgusting. They smell far too awful to even consider getting closer than you already are, much less to consider what happened to them."
    jump cargo

label cargoCrates:
    $room_buttons_enabled = False
    $room_scroll_enabled = False
    t "They're bolted shut. There's no way to tell what might be in them."
    jump cargo

label cargoWindow:
    $room_buttons_enabled = False
    $room_scroll_enabled = False
    show windowCargoCloseup onlayer master with fade
    menu:
        "Examine outside.":
            show windowCargo onlayer master with fade
            t "You look out the window."
            menu:
                "Step away.":
                    hide windowCargoCloseup
                    hide windowCargo with fade
                    jump cargo
        "Step away.":
            hide windowCargo
            hide windowCargoCloseup with fade
            jump cargo


label cargoDoor:
    $room_buttons_enabled = False
    $room_scroll_enabled = False
    if page_combined == False and item_page_1 == False or item_page_2 == False:
        t "You should probably try and gather what you can from this room first."
        jump cargo
    if page_combined == False and item_page_1 == True and item_page_2 == True:
        t "You have what you need, but you should repair the page first."
        jump cargo
    if page_combined == True:
        t "An inconspicuous door. Should you enter?"
        menu:
            "Enter.":
                hide screen cargoRoom
                jump kitchenEnter
            "Turn away.":
                jump cargo

label cargoStatuette:
    $room_buttons_enabled = False
    $room_scroll_enabled = False
    t "A small copper statue of what, at first glance, appears to be a robed man. Upon further inspection, the man seems to have a fish-like head and webbed fingers."
    t "You wonder whether this is their god or one of them, and how such a form could be seen as worthy of worship."
    jump cargo

label cargoBook:
    $room_buttons_enabled = False
    $room_scroll_enabled = False
    $showCargoBook = True
    $readbook = True
    if item_page_1 == False:
        t "The book is open to a torn and yellowed page with few words written on it. You don't have nearly enough time or interest for that matter to read through it."
        t "The half of the page that remains bound to the rest of the book reads," 
        t " -iver us, for we yearn to be entangled in your cold embrace as the children of your new earth."
        p1 "You need the rest of this."
        t "You find yourself tearing off the page and tucking it away." #theo wrote this, replace if aidan writes smth
        $item_page_1 = True
        $showCargoBook = False
    else:
        t "You've already taken the page out."
        $showCargoBook = False
    jump cargo

label cargoPendant:
    $room_buttons_enabled = False
    $room_scroll_enabled = False
    t "A small silver pendant depicting multiple small tendrils."
    t "Perhaps the god these people follow has tentacles or feelers."
    jump cargo

label cargoPoster:
    $room_buttons_enabled = False
    $room_scroll_enabled = False
    $lookposter = True
    t "The worn, tattered poster reads \"GLORY TO THE ONE BELOW\" along the top. Along the bottom, it reads, \"AND MAY SHE RETURN ABOVE\"."
    t "Maybe this is some sort of anachronism or call and response. You shudder to think what kind of being they might be referring to."
    jump cargo