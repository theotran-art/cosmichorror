# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define t = Character((None), what_italic=True) #thoughts
define h = Character((None), screen='hag_screen', what_font="fonts/fonts_hag/Funnel_Display_Lacquer/Lacquer/Lacquer-Regular.ttf", what_size=36) #hag
define c = Character((None)) #cannibal
define s = Character((None)) #skeptic
define p1 = Character((None), what_color="FCC7C7")
define p2 = Character((None), what_color="B54545")
define p3 = Character((None), what_color="BF1717")


default hagsus = 0
default item_page = False
default readbook = False
default lookposter = False

default item_knife = False
default item_lighter = False

screen hag_screen(who, what):

    style_prefix "hag"

    window id "hag_window":
        xalign 0.5
        yalign 0.65

    text what id "what":
        layout "nobreak"
        text_align 0.5
        xalign 0.5
        yalign 0.65

label start: 
    call intro
return

#MENU/OPTION SELECT GUIDE because im gonna forget
#menu:
    #"INSERT A QUESTION/DIALOUGE SHOWN WITH OPTIONS"
    #"Choice": DONT FORGET COLON
    #"Choice": 
        #Branching path/different dialogue triggered