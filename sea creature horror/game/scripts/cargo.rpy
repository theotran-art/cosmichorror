label cargo:

    $cargo_scroll_enabled = True

    show screen cargoRoom

    #scene cargo

    if item_page == False:
        p1 "YOU NEED HER HOLY TEXT."

    show screen inventory 

    pause

#CARGO SCREENS/IMAGE BUTTONS

screen cargoRoom:
    #pannable view of room
    viewport id "cargoScene":
        area (0, 0, 1920, 1080) #size of screen (leave the same)
        child_size (5497, 1620) #change based on image size

        if cargo_scroll_enabled:
            edgescroll (150, 1400) #how fast the scrolling is (horizontal_speed, vertical_speed)
        else: 
            edgescroll (0,0)
 
        add "images/backgrounds/cargo.png" #name of the background image
        
        imagebutton: #for dead bodies
            pos (1000,600) #where it appears on the screen
            auto "images/items/cargo/bodies_%s.png" action Jump("cargoDeadBodies") 
        imagebutton: #for crates
            pos (3000,600) #where it appears on the screen
            auto "images/items/cargo/crates_%s.png" #action Jump("cargoCrates")
        imagebutton: #for the Hag
            pos (4500,400) #where it appears on the screen
            auto "images/sprites/cargo/hag_%s.png" #action Jump("hagtalk")
        imagebutton: #for the window
            pos (5000,600)
            auto "images/items/cargo/window_%s.png" #action Jump("cargoWindow")    
        imagebutton: #for the cargo door
            pos (2000,600)
            auto "images/items/cargo/door_%s.png" #action Jump ("cargoDoor")
        imagebutton: #for statuette
            pos (4000,600) #where it appears on the screen
            auto "images/items/cargo/figurine_%s.png" #action Jump("cargoStatuette")
        imagebutton: #for book
            pos (5000,600) #where it appears on the screen
            auto "images/items/cargo/book_%s.png" #action Jump("cargoBook")
        #imagebutton: #for pendant
            #pos (0,0) #where it appears on the screen
            #auto "images/items/_%s.png" action Jump("cargoPendant")
        imagebutton: #for poster
            pos (2000,600) #where it appears on the screen
            auto "images/items/cargo/poster1_%s.png" #action Jump("cargoPoster")
        imagebutton: #for poster2
            pos (1000,600) #where it appears on the screen
            auto "images/items/cargo/poster2_%s.png" #action Jump("cargoPoster") 


#imagebutton: #make sure the image has normal and _hover 
            #pos (0,0) #where it appears on the screen
            #auto "_%s.png" action Jump("") #auto "IMAGE NAME OF CLICKABLE_%s.png" action Jump("WHAT HAPPENS WHEN CLICKED") // make sure that it jumps to a label!

#CARGO CLICKABLE TEXT

label cargoDeadBodies:
    $cargo_scroll_enabled = False
    t "Disgusting. They smell far too awful to even consider getting closer than you already are, much less to consider what happened to them."
    jump cargo

label cargoCrates:
    $cargo_scroll_enabled = False
    t "They're bolted shut. There's no way to tell what might be in them."
    jump cargo

label cargoWindow:
    $cargo_scroll_enabled = False
    hide screen cargoRoom

    #scene window
    menu:
        "Examine outside.":
            "You look out the window."
            jump cargoWindow
        "Step away.":
            jump cargo


label cargoDoor:
    $cargo_scroll_enabled = False
    if item_page == False:
        t "You should probably try and gather what you can from this room first."
        jump cargo
    if item_page == True:
        t "An inconspicuous door. Should you enter?"
        menu:
            "Enter.":
                "(You have finished the first room - End of playtest.)"
                return
                #jump kitchen
            "Turn away.":
                jump cargo

label cargoStatuette:
    $cargo_scroll_enabled = False
    t "A small copper statue of what, at first glance, appears to be a robed man. Upon further inspection, the man seems to have a fish-like head and webbed fingers."
    t "You wonder whether this is their god or one of them, and how such a form could be seen as worthy of worship."
    jump cargo

label cargoBook:
    $cargo_scroll_enabled = False
    $readbook = True
    t "The book is open to a torn and yellowed page with few words written on it. You don't have nearly enough time or interest for that matter to read through it."
    t "The half of the page that remains bound to the rest of the book reads," 
    t " -iver us, for we yearn to be entangled in your cold emabrace as the children of your new earth."
    p1 "You need the rest of this."
    jump cargo

label cargoPendant:
    $cargo_scroll_enabled = False
    t "A small silver pendant depicting multiple small tendrils."
    t "Perhaps the god these people follow has tentacles or feelers."
    jump cargo

label cargoPoster:
    $cargo_scroll_enabled = False
    $lookposter = True
    t "The worn, tattered poster reads \"GLORY TO THE ONE BELOW\" along the top. Along the bottom, it reads, \"AND MAY SHE RETURN ABOVE\"."
    t "Maybe this is some sort of anachronism or call and response. You shudder to think what kind of being they might be referring to."
    jump cargo