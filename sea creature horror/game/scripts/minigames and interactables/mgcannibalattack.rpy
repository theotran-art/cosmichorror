
init python:
    def slider_update():

        global slider_x
        global slider_direction
        speed = 3 #change this line to make it faster/slower ex: 1.5 slow, 5 fast
        max_x = slider_bar_size[0] - slider_size[0]

        if slider_direction == "right": #boundary of the slider
            slider_x += speed

            if slider_x >= max_x:
                slider_x = max_x
                slider_direction = "left"

        else: #boundary of the slider
            slider_x -= speed

            if slider_x <= 0:
                slider_x = 0
                slider_direction = "right"

    def check_slider_safe_zone():

        global cann_defeat #if you sucessfully hit the safe zone
        global cann_hits #how many times you fail/the cannibal hits you
        global cann_lose #if you lose
        global stop_slider

        if safe_zone_x < slider_x < safe_zone_x + safe_zone_size[0]:

            cann_defeat = True
            stop_slider = True
            #renpy.play("audio/open-door.ogg", "sound") #WIN

        elif cann_hits > 0:
            #renpy.play("audio/error.ogg", "sound") #LOSE NOISE
            cann_hits -= 1

        if cann_hits == 0:
            #renpy.show_screen("game_over") probably transfer to game over
            cann_lose = True
            stop_slider = True

    def reset_cannibal_attack():

        global slider_x
        global safe_zone_x
        global cann_defeat
        global cann_hits
        global cann_lose
        global stop_slider
        global slider_speed

        slider_x = 0
        safe_zone_x = renpy.random.randint(0, slider_bar_size[0] - safe_zone_size[0])

        cann_defeat = False
        cann_hits = 2
        stop_slider = False
        slider_speed = 2

        renpy.restart_interaction()

transform half_size:
    zoom 0.5

#screen game_over:

    #replace with something else, dont need this


screen mg_cannibal_attack:
    on "show" action Function(reset_cannibal_attack)
    
    key ["K_SPACE","mousedown_1"] action If(
        cann_defeat,
        true=[Hide("mg_cannibal_attack", transition=Fade(1,1,1)), Jump("mg_canatt_win")], 
        false=Function(check_slider_safe_zone)
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
    
    if cann_lose: #what happens if you lose
        timer 0.01 action [Hide("mg_cannibal_attack"), Jump("death")]
    #else:
        #this would be cannibals dead body or something


screen temp_cann_attack:
    textbutton "Get attacked by the Cannibal":
        action [Hide("temp_cann_attack"), Show("mg_cannibal_attack")]

label cansus_check:
    if cansus == 3: #trigger cannibal attack
        jump mg_canatt
    elif cansus > 0:
        show screen suspicion_overlay


label mg_canatt:
    $kitchen_buttons_enabled = False 
    $kitchen_scroll_enabled = False

    # Safe zone variables
    $ safe_zone_size = (int(149 / 2), int(70 / 2))

    # Slider variables
    $ slider_bar_size = (int(545 / 2), int(70 / 2))
    $ slider_size = (int(48 / 2), int(66 / 2))

    $ slider_x = 0
    $ slider_direction = "right"
    $ slider_speed = 2
    $ stop_slider = False

    # Safe zone
    $ safe_zone_x = 0

    # Cannibal variables
    $ cann_defeat = False
    $ cann_hits = 2
    $ cann_lose = False

    call screen temp_cann_attack #temp

    #show screen mg_cannibal attack
    $ renpy.pause()

label mg_canatt_win:
    "you killed him woah!"
    jump kitchen