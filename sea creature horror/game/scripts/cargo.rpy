label cargo:

    #call screen cargoRoom

    if item_page == False:
        p1 "YOU NEED HER HOLY TEXT."

    #TEMP ACCESS TO ACTIONS WITHOUT IMG BUTTONS
    menu:
        "Talk to Hag":
            jump hagtalk
        "Crates":
            jump cargoCrates
        "Dead bodies":
            jump cargoDeadBodies
        "Paraphenalia":
            jump cargoParaphenalia
        "Door":
            jump cargoDoor
        


#CARGO SCREENS/IMAGE BUTTONS

screen cargoRoom:
    #pannable view of room
    viewport id "cargoScene":
        area (0, 0, 1920, 1080) #size of screen (leave the same)
        child_size (0, 1080) #change based on image size
        edgescroll (150, 1400) #how fast the scrolling is (horizontal_speed, vertical_speed)
 
        #add ".png" #name of the background image
        
        imagebutton: #for dead bodies
            pos (0,0) #where it appears on the screen
            auto "_%s.png" action Jump("cargoDeadBodies") 
        imagebutton: #for paraphenalia
            pos (0,0) #where it appears on the screen
            auto "_%s.png" action Jump("cargoParaphenalia")
        imagebutton: #for crates
            pos (0,0) #where it appears on the screen
            auto "_%s.png" action Jump("cargoCrates")
        imagebutton: #for the Hag
            pos (0,0) #where it appears on the screen
            auto "_%s.png" action Jump("hagtalk")    
        imagebutton: #for the cargo door
            pos (0,0)
            auto "_%s.png" action Jump ("cargoDoor")

screen paraphenalia:
    viewport id "paraphenalia":
        area (0, 0, 1920, 1080) #size of screen (leave the same)
        child_size (0, 1080) #change based on image size
        edgescroll (150, 1400) #how fast the scrolling is (horizontal_speed, vertical_speed)
 
        #add ".png" #name of the background image
        
        imagebutton: #for statuette
            pos (0,0) #where it appears on the screen
            auto "_%s.png" action Jump("cargoStatuette") 
        imagebutton: #for book
            pos (0,0) #where it appears on the screen
            auto "_%s.png" action Jump("cargoBook")
        imagebutton: #for pendant
            pos (0,0) #where it appears on the screen
            auto "_%s.png" action Jump("cargoPendant")
        imagebutton: #for poster
            pos (0,0) #where it appears on the screen
            auto "_%s.png" action Jump("cargoPoster")    


#imagebutton: #make sure the image has normal and _hover 
            #pos (0,0) #where it appears on the screen
            #auto "_%s.png" action Jump("") #auto "IMAGE NAME OF CLICKABLE_%s.png" action Jump("WHAT HAPPENS WHEN CLICKED") // make sure that it jumps to a label!

#CARGO CLICKABLE TEXT

label cargoDeadBodies:
    t "Disgusting. They smell far too awful to even consider getting closer than you already are, much less to consider what happened to them."
    jump cargo

label cargoCrates:
    t "They're bolted shut. There's no way to tell what might be in them."
    jump cargo

label cargoDoor:
    if item_page == False:
        t "You should probably try and gather what you can from this room first."
        jump cargo
    if item_page == True:
        t "An inconspicuous door. Should you enter?"
        menu:
            "Enter.":
                jump kitchen
            "Turn away.":
                jump cargo


label cargoParaphenalia:
    t "At a glance, you thought someone had set up a Catholic gift shop in the corner. Upon further inspection, you realize nothing could be further from the truth. There are effigies and symbols the likes of which you have never seen."
    #TEMP MENU
    menu:
        "Statuette":
            jump cargoStatuette
        "Book":
            jump cargoBook
        "Pendant":
            jump cargoPendant
        "Poster":
            jump cargoPoster
        "Leave.":
            jump cargo

label cargoStatuette:
    t "A small copper statue of what, at first glance, appears to be a robed man. Upon further inspection, the man seems to have a fish-like head and webbed fingers."
    t "You wonder whether or not this is their god, and how such a form could be seen as worthy of worship."
    jump cargoParaphenalia

label cargoBook:
    $readbook = True
    t "The book is open to a torn and yellowed page with few words written on it. You don't have nearly enough time or interest for that matter to read through it."
    t "The half of the page that remains bound to the rest of the book reads," 
    t " -iver us, for we yearn to be entangled in your cold emabrace as the children of your new earth."
    p1 "You need the rest of this."
    jump cargoParaphenalia

label cargoPendant:
    t "A small silver pendant depicting multiple small tendrils."
    t "Perhaps the god these people follow has tentacles or feelers."
    jump cargoParaphenalia

label cargoPoster:
    t "The worn, tattered poster reads \"GLORY TO THE ONE BELOW\" along the top. Along the bottom, it reads, \"AND MAY SHE RETURN ABOVE\"."
    t "Maybe this is some sort of anachronism or call and response. You shudder to think what kind of being they might be referring to."
    jump cargoParaphenalia