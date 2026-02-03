define mc = Character("You")
define h = Character("Hag")
define c = Character("Cannibal")
define s = Character("Skeptic")

label cargo:

    call screen cargoRoom
    
label partone:
    "I. The Cargo"
    "In the room the player wakes up in, there is an old, eccentric hag."
    "This eccentric elderly woman is an aspirant of the cult. She lived among commonfolk for the majority of her life, performing strange and unsettling rituals to gain the Cults attention. Finally, in her old age, she has been taken by them in order to become a full fledged member."
    "The player must interact with her and solve puzzles within room 1 in order to obtain the Excerpt, the passage from the Cult's holy texts that the player must read during the ritual."
    call minigametut
    
return

#CARGO SCREENS

screen cargoRoom:
    #pannable view of room
    viewport id "cargoScene":
        area (0, 0, 1920, 1080) #size of screen (leave the same)
        child_size (2886, 1080) #change based on image size
        edgescroll (150, 1400) #how fast the scrolling is (horizontal_speed, vertical_speed)
 
        #add ".png" #name of the background image
        imagebutton:
            pos (650,800) #where it appears on the screen
            auto "drawer_%s.png" action Jump("") #auto "IMAGE NAME OF CLICKABLE.png" action Jump("WHAT HAPPENS WHEN CLICKED") // make sure that it jumps to a label!