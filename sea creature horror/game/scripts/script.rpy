# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

init python:
    if persistent.game_finished_once == True:
        gui.main_menu_background = "gui/titlepage2.png"
    else:
        gui.main_menu_background = "gui/titlepage.png"

    config.layers = ['background', 'master', 'window', 'transient', 'overlay', 'ui', 'screens', 'text', 'top']

    config.rollback_enabled = False #disable going back
    # Remove right-click from opening the game menu
    if "mouseup_3" in config.keymap["game_menu"]:
        config.keymap["game_menu"].remove("mouseup_3")
    if "K_ESCAPE" not in config.keymap["game_menu"]:
        config.keymap["game_menu"].append("K_ESCAPE")
        

define config.has_autosave = False
define config.say_layer = "text"
define config.choice_layer = "screens"
define config.default_afm_enable = False
define config.fast_skipping = False

define t = Character((None), what_font="fonts/Labrada/Labrada-VariableFont_wght.ttf", what_italic=True) #thoughts
define h = Character((None), screen='character_screen', what_font="fonts/fonts_hag/Funnel_Display_Lacquer/Lacquer/Lacquer-Regular.ttf", what_size=32) #hag
define c = Character((None), screen='character_screen', what_font="fonts/blackcraft/Blackcraft.ttf", what_size=36) #cannibal
define s = Character((None), screen='character_screen', what_font="fonts/subway_haze/Subway_Haze_1.1.ttf", what_size=36) #skeptic
define p1 = Character((None), what_color="FCC7C7", what_font="fonts/Labrada/Labrada-VariableFont_wght.ttf")
define p2 = Character((None), what_color="B54545", what_font="fonts/Labrada/Labrada-VariableFont_wght.ttf")
define p3 = Character((None), what_color="BF1717", what_font="fonts/Labrada/Labrada-VariableFont_wght.ttf")



#general things
define music.bgm = "music/bgm.wav"
default characterTalk = False
default locationTracker = "none"
default room_scroll_enabled = True
default room_buttons_enabled = True
default persistent.game_finished_once = False

screen blackbckgd:
    add Solid("#000")

#inventory items
default settingsClicked = False
default inventory_open = False
default hide_inventory = False
default inventory_visible = True
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
default kitchenDoorKey = False
default kitchenSpices = False
default kitchenSpicesUsed = False
default canndead = False
default showItemKnife = False
default showItemArm = False
default showItemSpices = False
default showItemKey = False
#arm states
default kitchenArm = False
default kitchenArmCut = False
default kitchenArmCutBad = False
default kitchenArmCooked = False
default kitchenArmCookedBad = False
default kitchenStew = False

#moonpool/skeptic variables
default moonpool_scroll_enabled = True
default moonpool_buttons_enabled = True
default skesus = 0
default pske = False
default sketalks = 0
default evidence = 0
default showItemLighter = False
default mpDiagnosis = False
default mpSpecimen = False
default mpDiagram = False
default showItemSpecimen = False
default showItemDiagram = False
default showItemDiagnosis = False

screen character_screen(who, what):
    if not renpy.context()._menu:
        zorder 100
        #window id "window":
            #xalign 0.5
            #yalign 0.65

        frame:
            background Frame("gui/customui/textbox2.png")
            #xsize 1800
            ysize 90
            xalign 0.5
            yalign 0.66
            padding (80,20)

            text what id "what":
                layout "nobreak"
                text_align 0.5
                xalign 0.5
                yalign 0.35

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
    $ _game_menu_screen = "history"
    $ quick_menu = False
    call intro from _call_intro
return

#MENU/OPTION SELECT GUIDE because im gonna forget
#menu:
    #"INSERT A QUESTION/DIALOUGE SHOWN WITH OPTIONS"
    #"Choice": DONT FORGET COLON
    #"Choice": 
        #Branching path/different dialogue triggered

#CHANGE TITLE SCREEN AT THE END OF THE GAME
#$ persistent.game_finished_once = True
#$ renpy.save_persistent()