init python:

    def slider_update():

        global slider_x
        global slider_direction
        speed = slider_speed #change this line to make it faster/slower ex: 1.5 slow, 5 fast
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

        global arm_cuts #if it hits safe zone  
        global arm_attempts #how many attempts
        global arm_bad_cut #if you lose
        global stop_slider

        if safe_zone_x < slider_x < safe_zone_x + safe_zone_size[0]:

            arm_cuts = True
            stop_slider = True
            #renpy.play("audio/open-door.ogg", "sound") #WIN

        elif arm_attempts > 0:
            #renpy.play("audio/error.ogg", "sound") #LOSE NOISE
            arm_attempts -= 1

        if arm_attempts == 0:
            #renpy.show_screen("game_over") probably transfer to game over
            arm_bad_cut = True
            stop_slider = True

        renpy.restart_interaction()

    def reset_cut_arm():

        global slider_x
        global safe_zone_x
        global arm_cuts #if it hits safe zone  
        global arm_attempts #how many attempts
        global arm_bad_cut #if you lose
        global stop_slider
        global slider_speed

        slider_x = 0
        safe_zone_x = renpy.random.randint(0, slider_bar_size[0] - safe_zone_size[0])

        arm_cuts = False
        stop_slider = False

        renpy.restart_interaction()

transform half_size:
    zoom 0.5

#screen game_over:

    #replace with something else, dont need this


screen mg_kitchen_arm_cut:
    on "show" action Function(reset_cut_arm)
    
    key ["K_SPACE","mousedown_1"] action If(
        arm_cuts,
        true=[Hide("mg_kitchen_arm_cut"), Return(True)],
        false=[Function(check_slider_safe_zone), SetScreenVariable("dummy", True)]
    )
    
    if not arm_cuts:
        frame: 
            background "#00000088"
            padding (5,5)
            align (0.5, 0.1)
            text "Cut the arm into smaller pieces." size 40 color "#ffffff"
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
        
    if arm_bad_cut: #what happens if you lose
        timer 0.01 action [Hide("mg_kitchen_arm_cut"), Jump("mg_kitchenArmCut_bad")]

label mg_KitchenArmCut:

    $room_buttons_enabled = False
    $room_scroll_enabled = False

    # Safe zone variables
    $ safe_zone_size = (int(149 / 2), int(70 / 2))

    # Slider variables
    $ slider_bar_size = (int(545 / 2), int(70 / 2))
    $ slider_size = (int(48 / 2), int(66 / 2))

    $ slider_direction = "right"
    $ armcut_speeds = [4, 6, 8]
    $ armcut_required = 3
    $ arm_attempts = 2
    $ arm_bad_cut = False

    $ armcut_index = 0

    while armcut_index < armcut_required:

        # Apply speed for this round
        $ slider_speed = armcut_speeds[min(armcut_index, len(armcut_speeds)-1)]

        # Reset round-specific stuff
        $ slider_x = 0
        $ safe_zone_x = renpy.random.randint(0, slider_bar_size[0] - safe_zone_size[0])
        $ arm_cuts = False
        $ stop_slider = False

        show screen mg_kitchen_arm_cut onlayer master

        if arm_bad_cut:
            jump mg_kitchenArmCut_bad

        $ armcut_index += 1

    jump mg_KitchenArmCut_finished

label mg_KitchenArmCut_finished:
    $kitchenArmCut = True
    t "You finish cutting up the arm."
    jump kitchen

label mg_kitchenArmCut_bad:
    $kitchenArmCut = True
    $kitchenArmCutBad = True
    t "It doesn't look very good, but you finish cutting up the arm. "
    jump kitchen