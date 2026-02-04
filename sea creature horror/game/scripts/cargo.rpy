define mc = Character("You")
define h = Character("Hag")
define c = Character("Cannibal")
define s = Character("Skeptic")
define p = Character((None), what_color="BF1717")

label cargo:

    #call screen cargoRoom

    p "YOU NEED HER HOLY TEXT."

    #TEMP ACCESS TO ACTIONS WITHOUT IMG BUTTONS
    menu:
        "Talk to Hag":
            call hagtalk
        "Crates":
            call cargoCrates
        "Dead bodies":
            call cargoCrates
        "Paraphenalia":
            call cargoParaphenalia
        


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
            auto "_%s.png" action Call("cargoDeadBodies") 
        imagebutton: #for paraphenalia
            pos (0,0) #where it appears on the screen
            auto "_%s.png" action Call("cargoParaphenalia")
        imagebutton: #for crates
            pos (0,0) #where it appears on the screen
            auto "_%s.png" action Call("cargoCrates")
        imagebutton: #for the Hag
            pos (0,0) #where it appears on the screen
            auto "_%s.png" action Call("hagtalk")    

screen paraphenalia:
    viewport id "paraphenalia":
        area (0, 0, 1920, 1080) #size of screen (leave the same)
        child_size (0, 1080) #change based on image size
        edgescroll (150, 1400) #how fast the scrolling is (horizontal_speed, vertical_speed)
 
        #add ".png" #name of the background image
        
        imagebutton: #for statuette
            pos (0,0) #where it appears on the screen
            auto "_%s.png" action Call("cargoStatuette") 
        imagebutton: #for book
            pos (0,0) #where it appears on the screen
            auto "_%s.png" action Call("cargoBook")
        imagebutton: #for pendant
            pos (0,0) #where it appears on the screen
            auto "_%s.png" action Call("cargoPendant")
        imagebutton: #for poster
            pos (0,0) #where it appears on the screen
            auto "_%s.png" action Call("cargoPoster")    


#imagebutton: #make sure the image has normal and _hover 
            #pos (0,0) #where it appears on the screen
            #auto "_%s.png" action Jump("") #auto "IMAGE NAME OF CLICKABLE_%s.png" action Jump("WHAT HAPPENS WHEN CLICKED") // make sure that it jumps to a label!

#CARGO CLICKABLE TEXT

label cargoDeadBodies:
    "Disgusting. They smell far too awful to even consider getting closer than you already are, much less to consider what happened to them."
    call cargo
label cargoCrates:
    "They're bolted shut. There's no way to tell what might be in them."
    call cargo

label cargoParaphenalia:
    "At a glance, you thought someone had set up a Catholic gift shop in the corner. Upon further inspection, you realize nothing could be further from the truth. There are effigies and symbols the likes of which you have never seen."
    #TEMP MENU
    menu:
        "Statuette":
            call cargoStatuette
        "Book":
            call cargoBook
        "Pendant":
            call cargoPendant
        "Poster":
            call cargoPoster
        "(Leave)":
            call cargo

label cargoStatuette:
    "A small copper statue of what, at first glance, appears to be a robed man. Upon further inspection, the man seems to have a fish-like head and webbed fingers."
    "You wonder whether or not this is their god, and how such a form could be seen as worthy of worship."
    call cargoParaphenalia

label cargoBook:
    "The book is open to a torn and yellowed page with few words written on it. You don't have nearly enough time or interest for that matter to read through it."
    "The half of the page that remains bound to the rest of the book reads," 
    " -iver us, for we yearn to be entangled in your cold emabrace as the children of your new earth."
    p "You need the rest of this."
    call cargoParaphenalia

label cargoPendant:
    "A small silver pendant depicting multiple small tendrils."
    "Perhaps the god these people follow has tentacles or feelers."
    call cargoParaphenalia
label cargoPoster:
    "The worn, tattered poster reads \"GLORY TO THE ONE BELOW\" along the top. Along the bottom, it reads, \"AND MAY SHE RETURN ABOVE\"."
    "Maybe this is some sort of anachronism or call and response. You shudder to think what kind of being they might be referring to."
    call cargoParaphenalia