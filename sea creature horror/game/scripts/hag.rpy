# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define mc = Character("You")
define h = Character(None, screen='hag_screen')
define c = Character("Cannibal")
define s = Character("Skeptic") 
define p = Character((None), what_color="BF1717")

screen hag_screen(who, what):
    style_prefix "say"

    window id "window":
        xpos 0.7
        ypos 0.5
        anchor (0.5, 0.5)
        xsize 500
        padding (15, 10)
        if who is not None:
            window id "namebox":
                style "namebox"
                text who id "who"

        text what id "what":
            xmaximum 480

label hagtalk:
    
    "An elderly woman seems to be reflecting, meditating, or praying in soem sort of way. She pays you no mind until you walk closer to her."
    
    menu:
        h "Ahh! Another young aspirant come to witness the birth of the new earth!"
        
        "What are you talking about?":
            $hagsus += 1
            if hagsus == 2: 
                jump death
            
            else:
                "You clearly are no aspirant. Leave me."
                return
        
        "Well of course! Do you know where everyone went?":
            menu:
                h "It matters not dear one! We shall all be her children in her cold embrace. Glory to the One Below!"

                "And may she return above!":
                    "WIP"

                "Okay... Do you seriously not know where everyone went?":
                    $hagsus += 1

                "You seem to be stuck just as much as I am. Do you know a way out?":
                    $hagsus += 1
            
        
        "(Leave)":
            jump cargo

        