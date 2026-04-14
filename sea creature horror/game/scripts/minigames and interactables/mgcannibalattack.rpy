init python:

    def slider_update():

        global slider_x
        global slider_direction
        speed = slider_speed  # change this line to make it faster/slower ex: 1.5 slow, 5 fast
        max_x = slider_bar_size[0] - slider_size[0]

        if slider_direction == "right":
            slider_x += speed
            if slider_x >= max_x:
                slider_x = max_x
                slider_direction = "left"
        else:
            slider_x -= speed
            if slider_x <= 0:
                slider_x = 0
                slider_direction = "right"

    def check_slider_safe_zone():

        global cann_defeat  # if you successfully hit the safe zone
        global cann_hits  # how many times you fail/the cannibal hits you
        global cann_lose  # if you lose
        global stop_slider
        global cann_warning_type

        # SUCCESS
        if safe_zone_x < slider_x < safe_zone_x + safe_zone_size[0]:
            cann_defeat = True
            stop_slider = True
            return

        # MISS
        if cann_hits > 0:
            cann_hits -= 1
            if cann_hits == 1:
                cann_warning_type = 1   # show DURING this slider
            elif cann_hits == 0:
                cann_warning_type = 2   # final warning, will persist for remaining sliders

        if cann_hits == 0:
            cann_lose = True
            stop_slider = True

        renpy.restart_interaction()

    def reset_cannibal_attack():

        global slider_x
        global safe_zone_x
        global cann_defeat
        global cann_hits
        global cann_lose
        global stop_slider
        global slider_speed
        global cann_warning_type

        slider_x = 0
        safe_zone_x = renpy.random.randint(0, slider_bar_size[0] - safe_zone_size[0])

        cann_defeat = False
        stop_slider = False

        # Don't reset final warning if already triggered
        if cann_warning_type < 2:
            cann_warning_type = 0

        renpy.restart_interaction()

transform half_size:
    zoom 0.5

screen mg_cannibal_attack:
    on "show" action Function(reset_cannibal_attack)
    
    key ["K_SPACE","mousedown_1"] action If(
        cann_defeat,
        true=Hide("mg_cannibal_attack"),
        false=Function(check_slider_safe_zone)
    )
    
    if not cann_defeat:
        # Main slider and instruction
        frame: 
            background "#00000088"
            padding (5,5)
            xalign 0.5
            yalign 0.13
            text "Defend yourself!":
                size 50 
                color "#FF0000"
                font "fonts/fisherman_2/Fisherman-Regular.otf"

        frame:
            background None
            align (0.5,0.4)
            xysize slider_bar_size

            add "images/minigames/slider-bar.png" at half_size
            add "images/minigames/safe-zone.png":
                xpos safe_zone_x
                ypos 0
                zoom 0.5
            add "images/minigames/slider.png":
                xpos slider_x
                ypos 0
                zoom 0.5

            if not stop_slider:
                timer 0.016 repeat True action Function(slider_update)

    # Warnings
    if cann_warning_type == 1:  # only during first missed slider
        frame:
            background "#00000088"
            padding (5,5)
            xalign 0.5
            yalign 0.5
            text "You missed, and he kicks you in the stomach. You need to take him down now!":
                size 30
                color "#FF0000"
                font "fonts/fisherman_2/Fisherman-Regular.otf"
    elif cann_warning_type == 2:  # persistent for remaining rounds
        frame:
            background "#00000088"
            padding (5,5)
            xalign 0.5
            yalign 0.5
            text "You can't afford another mistake.":
                size 30
                color "#FF0000"
                font "fonts/fisherman_2/Fisherman-Regular.otf"
        
    if cann_lose:
        timer 0.01 action [Hide("mg_cannibal_attack"), Jump("death")]

    if cann_defeat:
        timer 0.01 action Jump("mg_canatt_after_round")

screen temp_cann_attack:
    textbutton "Get attacked by the Cannibal":
        action [Hide("temp_cann_attack"), Show("mg_cannibal_attack")]

label mg_canatt:

    $ room_buttons_enabled = False 
    $ room_scroll_enabled = False

    # Safe zone variables
    $ safe_zone_size = (int(149 / 2), int(70 / 2))

    # Slider variables
    $ slider_bar_size = (int(545 / 2), int(70 / 2))
    $ slider_size = (int(48 / 2), int(66 / 2))

    $ slider_direction = "right"
    $ cann_speeds = [6, 8, 10]
    $ cann_required = 3
    $ cann_hits = 2
    $ cann_lose = False
    $ cann_warning_type = 0
    $ attack_index = 0

    jump mg_canatt_round

label mg_canatt_round:

    if attack_index >= cann_required:
        jump mg_canatt_win

    # Apply speed for this round
    $ slider_speed = cann_speeds[min(attack_index, len(cann_speeds)-1)]

    # Reset round-specific stuff
    $ slider_x = 0
    $ safe_zone_x = renpy.random.randint(0, slider_bar_size[0] - safe_zone_size[0])
    $ cann_defeat = False
    $ stop_slider = False

    call screen mg_cannibal_attack

label mg_canatt_after_round:

    $ renpy.restart_interaction()  

    if cann_lose:
        jump death

    # Upgrade first warning to persistent
    if cann_warning_type == 1:
        $ cann_warning_type = 2

    # Dialogue in between each slider/attack (respects text speed)
    if attack_index == 0:
        t "You managed to dodge his attack, but he lunges for you again."
    elif attack_index == 1:
        t "You narrowly managed to dodge again. He seems desperate now and attacks you with all he has."

    $ attack_index += 1

    jump mg_canatt_round

label mg_canatt_win:
    $ canndead = True
    t "Good riddance."
    $ kitchenDoorKey = True
    t "You pick up the key from his corpse."
    jump kitchen