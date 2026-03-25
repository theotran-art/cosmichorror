default cann_slider_x = 0
default cann_safe_zone_x = 0
default cann_stop_slider = False

default cann_defeat = False #if you sucessfully hit the safe zone
default cann_hits = 2 #how many times you fail/the cannibal hits you
default cann_lose = False #if you lose

default cann_slider_speed = 6
default cann_slider_direction = "right"

default cann_warning_type = 0

init python:

    def cann_slider_update():

        global cann_slider_x
        global cann_slider_direction

        speed = cann_slider_speed #change this line to make it faster/slower ex: 1.5 slow, 5 fast
        max_x = cann_slider_bar_size[0] - cann_slider_size[0]

        if cann_slider_direction == "right": #boundary of the slider
            cann_slider_x += speed

            if cann_slider_x >= max_x:
                cann_slider_x = max_x
                cann_slider_direction = "left"

        else: #boundary of the slider
            cann_slider_x -= speed

            if cann_slider_x <= 0:
                cann_slider_x = 0
                cann_slider_direction = "right"


    def cann_check_slider():

        global cann_defeat #if you sucessfully hit the safe zone
        global cann_hits #how many times you fail/the cannibal hits you
        global cann_lose #if you lose
        global cann_stop_slider
        global cann_warning_type

        if cann_safe_zone_x < cann_slider_x < cann_safe_zone_x + cann_safe_zone_size[0]:

            cann_defeat = True
            cann_stop_slider = True
            #renpy.play("audio/open-door.ogg", "sound") #WIN

        elif cann_hits > 0:
            #renpy.play("audio/error.ogg", "sound") #LOSE NOISE
            cann_hits -= 1

            if cann_hits == 1:
                cann_warning_type = 1
            elif cann_hits == 0:
                cann_warning_type = 2

        if cann_hits == 0:
            #renpy.show_screen("game_over") probably transfer to game over
            cann_lose = True
            cann_stop_slider = True

        renpy.restart_interaction()


    def cann_reset():

        global cann_slider_x
        global cann_safe_zone_x
        global cann_defeat
        global cann_stop_slider

        cann_slider_x = 0
        cann_safe_zone_x = renpy.random.randint(0, cann_slider_bar_size[0] - cann_safe_zone_size[0])

        cann_defeat = False
        cann_stop_slider = False

        renpy.restart_interaction()
        
#screen game_over:

    #replace with something else, dont need this

transform cann_shake_transform:
    linear 0.05 xoffset -10
    linear 0.05 xoffset 10
    linear 0.05 xoffset -6
    linear 0.05 xoffset 6
    linear 0.05 xoffset 0

screen mg_cannibal_attack:

    on "show" action Function(cann_reset)

    key ["K_SPACE","mousedown_1"] action If(
        cann_defeat,
        true=[Hide("mg_cannibal_attack"), Return(True)],
        false=Function(cann_check_slider)
    )

    if not cann_defeat:

        frame: 
            background "#00000088"
            padding (5,5)
            align (0.5, 0.1)
            text "Defend yourself!" size 40 color "#FF0000"

        frame:
            background None
            align (0.5,0.4)
            xysize cann_slider_bar_size

            add "images/minigames/slider-bar.png"

            add "images/minigames/safe-zone.png":
                xpos cann_safe_zone_x
                ypos 0

            add "images/minigames/slider.png":
                xpos cann_slider_x
                ypos 0

            if not cann_stop_slider:
                timer 0.016 repeat True action Function(cann_slider_update)

    if cann_warning_type == 1:
        frame:
            background "#00000088"
            padding (5,5)
            align (0.5, 0.15)
            text "You missed, and he stabs you. You need to take him down now!" size 30 color "#FF0000"

    elif cann_warning_type == 2:
        frame:
            background "#00000088"
            padding (5,5)
            align (0.5, 0.15)
            text "You can't afford another mistake." size 30 color "#FF4444"

    if cann_lose: #what happens if you lose
        timer 0.01 action [Hide("mg_cannibal_attack"), Jump("death")]


screen temp_cann_attack:
    textbutton "Get attacked by the Cannibal":
        action [Hide("temp_cann_attack"), Show("mg_cannibal_attack")]

label cansus_check:
    if cansus > 0:
        show screen suspicion_overlay
    if cansus == 3: #trigger cannibal attack
        jump mg_canatt

label mg_canatt:
    $ cann_defeat = False
    $ cann_hits = 2
    $ cann_lose = False
    $ cann_stop_slider = False
    $ cann_warning_type = 0

    $ kitchen_buttons_enabled = False 
    $ kitchen_scroll_enabled = False

    # Safe zone variables
    $ cann_safe_zone_size = (int(149 / 2), int(70 / 2))

    # Slider variables
    $ cann_slider_bar_size = (int(545 / 2), int(70 / 2))
    $ cann_slider_size = (int(48 / 2), int(66 / 2))

    $ cann_slider_direction = "right"
    $ cann_speeds = [6, 8, 10]
    $ cann_required = 3

    $ attack_index = 0

    while attack_index < cann_required:

        # Apply speed for this round
        $ cann_slider_speed = cann_speeds[min(attack_index, len(cann_speeds)-1)]

        # Reset round-specific stuff
        $ cann_hits = 2
        $ cann_lose = False
        $ cann_warning_type = 0

        call screen mg_cannibal_attack

        if cann_lose:
            jump death

        if attack_index == 0: #dialogue inbetween each slider/attack
            t "You managed to dodge his attack, but he lunges for you again."
        elif attack_index == 1:
            t "You narrowly managed to dodge again. He seems desperate now and attacks you with all he has."

        $ attack_index += 1

    jump mg_canatt_win

label mg_canatt_win:
    "you killed him woah!"
    jump kitchen