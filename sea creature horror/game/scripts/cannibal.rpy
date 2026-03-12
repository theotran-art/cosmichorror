
#function to use when adding sus to cannibal
#$cansus += 1
#call cansus_check

label cannibaltalk:
    #$kitchen_buttons_enabled = False 
    #$kitchen_scroll_enabled = False

    hide screen inventory

    #start of convo
    t "cannibal sitting there woah."
    menu:
        "say smth good":
            "nice"
        "say smth bad":
            "woah that not nice"
            $cansus += 3
            call cansus_check

