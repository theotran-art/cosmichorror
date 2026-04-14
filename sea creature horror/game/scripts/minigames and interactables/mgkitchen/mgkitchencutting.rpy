default arm_slider_bar_size = (272, 35)
default arm_slider_size = (24, 33)
default arm_safe_zone_size = (74, 35)

default arm_slider_x = 0
default arm_safe_zone_x = 0
default arm_stop_slider = False
default arm_cuts = False
default arm_bad_cut = False
default arm_attempts = 2
default arm_slider_speed = 4
default arm_slider_direction = "right"

init python:

    def arm_slider_update():
        global arm_slider_x, arm_slider_direction

        speed = arm_slider_speed
        max_x = arm_slider_bar_size[0] - arm_slider_size[0]

        if arm_slider_direction == "right":
            arm_slider_x += speed
            if arm_slider_x >= max_x:
                arm_slider_x = max_x
                arm_slider_direction = "left"
        else:
            arm_slider_x -= speed
            if arm_slider_x <= 0:
                arm_slider_x = 0
                arm_slider_direction = "right"


    def arm_check_slider():
        global arm_cuts, arm_attempts, arm_bad_cut
        global arm_stop_slider

        if arm_safe_zone_x < arm_slider_x < arm_safe_zone_x + arm_safe_zone_size[0]:
            arm_cuts = True
            arm_stop_slider = True

        elif arm_attempts > 0:
            arm_attempts -= 1

        if arm_attempts == 0:
            arm_bad_cut = True
            arm_stop_slider = True

        renpy.restart_interaction()


    def arm_reset():
        global arm_slider_x, arm_safe_zone_x
        global arm_cuts, arm_stop_slider

        arm_slider_x = 0
        arm_safe_zone_x = renpy.random.randint(0, arm_slider_bar_size[0] - arm_safe_zone_size[0])

        arm_cuts = False
        arm_stop_slider = False

        renpy.restart_interaction()

transform half_size:
    zoom 0.5

#screen game_over:

    #replace with something else, dont need this


screen mg_kitchen_arm_cut:
    
    add "images/minigames/cuttingboard.png":
        xalign 0.5

    add "images/minigames/arm_assets/arm_whole.png":
        yalign 0.85
        xalign 0.5


    on "show" action Function(arm_reset)

    key ["K_SPACE","mousedown_1"] action If(
        arm_cuts,
        true=[Hide("mg_kitchen_arm_cut"), Return(True)],
        false=[Function(arm_check_slider)]
    )

    if not arm_cuts:

        text "Cut the arm into smaller pieces.": 
            xalign 0.5
            yalign 0.13
            size 50 
            color "#ffffff"
            font "fonts/fisherman_2/Fisherman-Regular.otf"

        frame:
            background None
            align (0.5,0.4)
            xysize arm_slider_bar_size
            add "images/minigames/slider-bar.png" at half_size
            add "images/minigames/safe-zone.png":
                xpos arm_safe_zone_x
                ypos 0
                zoom 0.5
            add "images/minigames/slider.png":
                xpos arm_slider_x
                ypos 0
                zoom 0.5
            if not arm_stop_slider:
                timer 0.016 repeat True action Function(arm_slider_update)

    if arm_bad_cut: #what happens if you lose
        timer 0.01 action [Hide("mg_kitchen_arm_cut"), Jump("mg_kitchenArmCut_bad")]

label mg_KitchenArmCut:

    $ room_buttons_enabled = False
    $ room_scroll_enabled = False

    $ armcut_speeds = [4, 6, 8]
    $ armcut_required = 3

    $ armcut_index = 0

    while armcut_index < armcut_required:

        # Apply speed for this round
        $ arm_slider_speed = armcut_speeds[min(armcut_index, len(armcut_speeds)-1)]

        # Reset round-specific stuff
        $ arm_attempts = 2
        $ arm_bad_cut = False

        call screen mg_kitchen_arm_cut

        if arm_bad_cut:
            jump mg_kitchenArmCut_bad

        $ armcut_index += 1

    jump mg_KitchenArmCut_finished

screen mg_KitchenArmCut_results:
    add "images/minigames/cuttingboard.png":
        xalign 0.5

    if kitchenArmCutBad:
        add "images/minigames/arm_assets/arm_messy/arm.png":
            yalign 0.85
            xalign 0.5
    else:
        add "images/minigames/arm_assets/arm_clean/arm.png":
            yalign 0.85
            xalign 0.5

label mg_KitchenArmCut_finished:
    $ kitchenArmCut = True
    show screen mg_KitchenArmCut_results
    t "You finish cutting up the arm."
    hide screen mg_KitchenArmCut_results with fade
    jump kitchen

label mg_kitchenArmCut_bad:
    $ kitchenArmCut = True
    $ kitchenArmCutBad = True
    show screen mg_KitchenArmCut_results
    t "It doesn't look very good, but you finish cutting up the arm."
    hide screen mg_KitchenArmCut_results with fade
    jump kitchen