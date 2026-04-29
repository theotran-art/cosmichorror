label moonpoolEnter:
    #hide kitchen related items
    $ kitchenSpices = False
    $ kitchenStew = True
    $ kitchenArm = False

    $locationTracker = "moonpool"
    hide screen kitchenRoom
    hide screen suspicion_overlay
    show screen moonpoolRoom onlayer master
    t "As you enter, you see a large rectangular room with a dock to a moon pool cut into the floor."
    t "Crates of cargo sit packed into every corner with copious loose item scattered about them. An out-of-place yet normal looking woman stands thinking in the corner."
    t "The floor, unlike the rest of the boat so far, is contructed of wooden planks. The perfect staging ground for a ritual."
    jump moonpool

label moonpool:
    #variable stuff
    $locationTracker = "moonpool"
    $characterTalk = False

    #screen transitions
    $room_buttons_enabled = False
    $hide_inventory = False
    show screen moonpoolRoom onlayer master

    #persistent parasite quest
    if item_lighter == False:
        p3 "YOU NEED HER LITTLE FLAME."
    
    #reset sus overlay
    if item_lighter == True and skesus >= 1:
        hide screen suspicion_overlay with fade
        
    #loop for point and click
    $room_scroll_enabled = True
    label pauseMoonpool:
        window hide
        $room_buttons_enabled = True
        pause
        jump pauseMoonpool
    window auto  

    #TEMP MENU FOR ACESSS
    #menu:
        #"Talk to Skeptic":
            #$ hide_inventory = True
            #jump skeptictalk
        #"Crates" if sketalks == 0:
            #$ hide_inventory = True
            #jump moonpoolCrates
        #"Diagnosis" if sketalks == 1:
            #$ hide_inventory = True
            #jump moonpoolDiagnosis
        #"Specimen" if sketalks == 1:
            #$ hide_inventory = True
            #jump moonpoolSpecimen
        #"Diagram" if sketalks == 1:
            #$ hide_inventory = True
            #jump moonpoolDiagram

screen moonpoolRoom:
    tag room

    #pannable view of room
    viewport id "moonpoolScene":
        area (0, 0, 1920, 1080) #size of screen (leave the same)
        child_size (5497, 1620) #change based on image size

        if room_scroll_enabled == True and locationTracker == "moonpool" and allow_edge_scroll():
            edgescroll (150, 1400) #how fast the scrolling is (horizontal_speed, vertical_speed)
        else: 
            edgescroll (0,0)
 
        add "images/backgrounds/moonpool.png" #name of the background image
        
        add "images/sprites/skeptic.png":
            pos (100,700)
        if room_buttons_enabled == True and locationTracker == "moonpool":
            #imagebutton: #for 
                #pos (340,945) #where it appears on the screen
                #auto "images/items/moonpool/_%s.png" action Hide("inventory"), Jump("moonpoolA")
            #add more imgbutt if needed

            #temp buttons

            textbutton "Cultist": #skeptic
                text_size 80
                text_color "#ffffff"
                text_outlines [(3, "#1e4961", 2, 2)]
                text_hover_color "#68a0be"
                pos (350,700) #where it appears on the screen
                action SetVariable("hide_inventory", True), Jump("skeptictalk")
            textbutton "Moon Pool": #moonpool
                text_size 80
                text_color "#ffffff"
                text_outlines [(3, "#1e4961", 2, 2)]
                text_hover_color "#68a0be"
                pos (1050,1200) #where it appears on the screen
                action SetVariable("hide_inventory", True), Jump("moonpoolDock")
            if sketalks == 0:
                textbutton "Crates": #crates
                    text_size 80
                    text_color "#ffffff"
                    text_outlines [(3, "#1e4961", 2, 2)]
                    text_hover_color "#68a0be"
                    pos (1440,750) #where it appears on the screen
                    action SetVariable("hide_inventory", True), Jump("moonpoolCrates")
            if sketalks == 1:
                textbutton "Diagnosis": #Diagnosis
                    text_size 80
                    text_color "#ffffff"
                    text_outlines [(3, "#1e4961", 2, 2)]
                    text_hover_color "#68a0be"
                    pos (5000,945) #where it appears on the screen
                    action SetVariable("hide_inventory", True), Jump("moonpoolDiagnosis")
                textbutton "Specimen": #Specimen
                    text_size 80
                    text_color "#ffffff"
                    text_outlines [(3, "#1e4961", 2, 2)]
                    text_hover_color "#68a0be"
                    pos (1300,230) #where it appears on the screen
                    action SetVariable("hide_inventory", True), Jump("moonpoolSpecimen")
                textbutton "Diagram": #Diagram
                    text_size 80
                    text_color "#ffffff"
                    text_outlines [(3, "#1e4961", 2, 2)]
                    text_hover_color "#68a0be"
                    pos (4000,500) #where it appears on the screen
                    action SetVariable("hide_inventory", True), Jump("moonpoolDiagram")


    #IMAGES THAT SHOW UP AFTER CLICKING AN ITEM (CLOSE UP)
    if showItemSpecimen:
        add Solid("#00000088")

        # Centered image
        add "images/items/moonpool/specimen.png":
            xalign 0.5
            yalign 0.5
    
    if showItemDiagram:
        add Solid("#00000088")

        # Centered image
        add "images/items/moonpool/diagram.png":
            xalign 0.5
            yalign 0.5
    
    if showItemDiagnosis:
        add Solid("#00000088")

        # Centered image
        add "images/items/moonpool/diagnosis.png":
            xalign 0.5
            yalign 0.5


#writing for clickable items
label moonpoolCrates:
    $room_buttons_enabled = False
    $room_scroll_enabled = False
    t "A pile of crates fills the corner of the room. They smell like salt water and dead fish."
    jump moonpool

label moonpoolDiagram:
    $room_buttons_enabled = False
    $room_scroll_enabled = False
    $showItemDiagram = True
    if mpDiagram == False:
        $evidence += 1
        $mpDiagram = True
    t "A diagram of some sort of worm-like creature. It's like someone was studying it for application as some sort of mind control."
    $showItemDiagram = False
    jump moonpool

label moonpoolSpecimen:
    $room_buttons_enabled = False
    $room_scroll_enabled = False
    $showItemSpecimen = True
    if mpSpecimen == False:
        $evidence += 1
        $mpSpecimen = True
    t "A dried specimen of an odd worm-like creature. You've never seen anything like it before."
    $showItemSpecimen = False
    jump moonpool

label moonpoolDiagnosis:
    $room_buttons_enabled = False
    $room_scroll_enabled = False
    $showItemDiagnosis = True
    t "You find a piece of paper that has a medical diagnosis."
    if mpDiagnosis == False:
        $evidence += 1
        $mpDiagnosis = True
    "{font=fonts/oceanside_typewriter/Oceanside Typewriter.ttf}Doctor Name: Dr. Alan Richards{p}Patient Name: Simon Ellis{p}Patient Age: 38 / Patient Sex: Male{p}Date: 9/23/--{p}Diagnosis: Parasitic Infection{/font}"
    "{font=fonts/oceanside_typewriter/Oceanside Typewriter.ttf}Patient entered urgent care at approximately 4:30 AM with complaints of severe headaches, memory loss, and compulsive/intrusive thoughts.{/font}"
    "{font=fonts/oceanside_typewriter/Oceanside Typewriter.ttf}I ran several rudimentary tests on him without anything leading to an explanation for his symptoms, however I did find several bite marks on his arms.{/font}"
    "{font=fonts/oceanside_typewriter/Oceanside Typewriter.ttf}After a number of scans, an X-ray revealed a small parasitic organism within his cranial cavity.{/font}"
    "{font=fonts/oceanside_typewriter/Oceanside Typewriter.ttf}It was unlike any parasite I had ever studied. I have hereby reached out to several medical research facilities and hospitals in hopes that they will take his case.{/font}"
    "{font=fonts/oceanside_typewriter/Oceanside Typewriter.ttf}I am unaware whether or not his condition is fatal, but the deterioration of his personality and ability to compose himself is clear.{/font}"
    $showItemDiagnosis = False
    jump moonpool
    

label moonpoolDock:
    $room_buttons_enabled = False
    $room_scroll_enabled = False
    t "You look into the moon pool."
    t "The water beneath you seems strangely calm." 
    t "The light from the ceiling lamp above you penetrates the surface for about a foot, but beyond that, you cannot see much of anything."
    t "The water fills with a deep, consuming void. It seems to extend onward for eternity."
    jump moonpool

label moonpoolRitual:
    $room_buttons_enabled = False
    $room_scroll_enabled = False
    t "The cold brass of the zippo lighter impresses into your palm."
    t "You notice that, as you turn from the woman, all you can focus on is walking."
    hide screen suspicion_overlay
    hide screen moonpoolRoom 
    show expression Solid("#000") as fade_black onlayer master with fade
    t "Your head pounds and throbs far too much to control multiple faculties at once."
    t "It becomes more and more difficult to take the next step until..."
    t "Your body is not your own. You kneel in the middle of the wooden floor as you watch your hands remove your gathered materials from your pockets."
    p3 "A KNIFE TO CARVE THE CIRCLE.{p}HOLY WORDS TO BLESS THE SUMMONING.{p}AND A FLAME TO CLEANSE THE BODY.{p}LET HER COME."
    t "As soon as you wonder if the woman will attempt to stop you, you hear her footsteps cut short by the grotesque sound of a fleshy explosion and the sound of a headless body hitting the floor."
    t "You do as the parasite commands." 
    t "Your hands carve a large circle with profane symbolism encompassing it. You strike the lighter and hold the flame near your chest while you read the words upon the page, your lips moving against your will."
    "\"O Mother of the Great Deep, we sever our love to our flesh to offer it to you alone, flaying our imperfect forms as penance for the circumstances of our births.\""
    "\"Accept our immaciated bodies and deliver us, for we yearn to be entangled in your cold embrace as the children of your new earth.\""
    t "For a moment, but only for a moment, both the ship and the water surrounding it are calmed for the first time. As if in answer, the hull begins to creak worse than ever before to a point at which you think it may crack... and it does."
    t "The walls burst and collapse in on each other. The structure of the ship is fully compromised, and you fall through the floor."
    t "Your body may be your own now, but it does not matter. You did all that the parasite needed you to do."
    $persistent.game_finished_once = True
    show screen ending_cutscene
    pause 7.0
    show expression Solid("#000") as fade_black onlayer master with fade
    show screen end
    pause 4.0
    $ MainMenu(confirm=False)()

image sinking:
    "images/death/cutscene/end1.png"
    pause 2.0
    "images/death/cutscene/end2.png"
    pause 1.0
    "images/death/cutscene/end3.png"
    pause 0.5
    "images/death/cutscene/end4.png"
    pause 0.5
    "images/death/cutscene/end5.png"
    pause 0.5
    "images/death/cutscene/end6.png"
    pause 0.5
    "images/death/cutscene/end7.png"
    pause 1.0

screen ending_cutscene:
    add "sinking"

screen end:
    text "The end. Thank you for playing!":
        xalign 0.5
        yalign 0.5
        size 100
        color "#ffffff"
        outlines [(3, "#32464e", 1, 1)]