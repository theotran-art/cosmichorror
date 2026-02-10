# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define t = Character((None), what_italic=True) #thoughts
define h = Character((None), screen='hag_screen')
define c = Character("Cannibal")
define s = Character("Skeptic")
define p1 = Character((None), what_color="FCC7C7")
define p2 = Character((None), what_color="B54545")
define p3 = Character((None), what_color="BF1717")


define hagsus = 0
define item_page = False
define readbook = False

define item_knife = False
define item_lighter = False

screen hag_screen(who, what):
    style_prefix "say"

    window id "window":
        pos (250,800)
        xsize 500
        padding (15, 10)
        if who is not None:
            window id "namebox":
                style "namebox"
                text who id "who"

        text what id "what":
            #xmaximum 480
            ymaximum 1

label start: 
    call intro
return

#MENU/OPTION SELECT GUIDE because im gonna forget
#menu:
    #"INSERT A QUESTION/DIALOUGE SHOWN WITH OPTIONS"
    #"Choice": DONT FORGET COLON
    #"Choice": 
        #Branching path/different dialogue triggered