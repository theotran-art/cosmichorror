# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define config.choice_layer = "text"
define config.say_layer = "text"

init python:
    config.layers = ['background', 'master', 'ui', 'transient', 'screens', 'text', 'overlay', 'top']

    #config.rollback_enabled = False #disable going back

define t = Character((None), what_italic=True) #thoughts
define h = Character((None), screen='character_screen', what_font="fonts/fonts_hag/Funnel_Display_Lacquer/Lacquer/Lacquer-Regular.ttf", what_size=32) #hag
define c = Character((None), screen='cannibal_screen', what_size=32) #cannibal
define s = Character((None)) #skeptic
define p1 = Character((None), what_color="FCC7C7")
define p2 = Character((None), what_color="B54545")
define p3 = Character((None), what_color="BF1717")



#general things
image black bckgd = "images/backgrounds/blackbckgd.jpg" 
define music.bgm = "music/bgm.wav"
default characterTalk = False

#inventory items
default settingsClicked = False
default inventory_open = False
default hide_inventory = False
default item_page = False
default showItemPage = False
default showItemPage1 = False
default showItemPage2 = False
default item_knife = False
default item_lighter = False

#cargo/hag related variables
default cargo_scroll_enabled = True
default cargo_buttons_enabled = True
default showCargoBook = False
default hagsus = 0
default phag = False
default readbook = False
default item_page_1 = False
default item_page_2 = False
default page_combined = False
default lookposter = False
image windowCargoCloseup = "images/backgrounds/windowCargoCloseup.png"
image windowCargo = "images/backgrounds/windowCargo.png"

#kitchen/cannibal related variables
default kitchen_scroll_enabled = True
default kitchen_buttons_enabled = True
default cansus = 0
default pcan = False


screen character_screen(who, what):
    if not renpy.context()._menu:
        zorder 100
        #window id "window":
            #xalign 0.5
            #yalign 0.65

        frame:
            background "gui/customui/textbox2.png"
            xsize 1800
            ysize 90
            xalign 0.5
            yalign 0.66

        text what id "what":
            layout "nobreak"
            text_align 0.5
            xalign 0.5
            yalign 0.65

#sorry reddit told me to put it here
init python:

    renpy.music.register_channel("music1", mixer="music", loop=True, stop_on_mute=True, tight=False, file_prefix='', file_suffix='', buffer_queue=True)

    def audio_crossFade(fadeTime, music):
        oldChannel = None
        newChannel = None
        if renpy.music.get_playing(channel="music") is not None and renpy.music.get_playing(channel="music1") is None:
            oldChannel = "music"
            newChannel = "music1"
        elif renpy.music.get_playing(channel="music") is None and renpy.music.get_playing(channel="music1") is not None:
            oldChannel = "music1"
            newChannel = "music"
        elif renpy.music.get_playing(channel="music") is None and renpy.music.get_playing(channel="music1") is None:
            oldChannel = None
            newChannel = "music"
            
        if oldChannel is not None:
            renpy.music.stop(channel= oldChannel, fadeout=fadeTime)
            
        if newChannel is not None:
            renpy.music.play(music, channel=newChannel, loop=None,fadein=fadeTime)

label start: 
    $ quick_menu = False
    call intro from _call_intro
return

#MENU/OPTION SELECT GUIDE because im gonna forget
#menu:
    #"INSERT A QUESTION/DIALOUGE SHOWN WITH OPTIONS"
    #"Choice": DONT FORGET COLON
    #"Choice": 
        #Branching path/different dialogue triggered