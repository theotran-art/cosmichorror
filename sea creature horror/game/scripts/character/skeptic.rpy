define skeswitch = False

label skeptictalk:
    $room_buttons_enabled = False 
    $room_scroll_enabled = False

    $hide_inventory = True
    $characterTalk = True

    if sketalks == 0:
        t "As you approach her, she double takes, seemingly not noticing that you were in the room." 
        t "She begins to intently study your eyes, contorting her body and tilting her head, possibly to get a better look at... something."
        
        menu:
            s "\"Do you still have control of yourself?\""

            "\"Uh... yes?\"":
                s "\"Good.\"" 
                jump skegood

                label skegood:
                    s "\"We don't have much time.\""
                    s "\"I am looking for evidence of these lunatics implanting people with parasites that I'm sure you're well aware of now.\""
                    s "\"I have a couple pieces, namely brain tissue from a deceased host.\""
                    s "\"This room is a submarine dock, yes, but also seemed to be some sort of research bay.\""
                    s "\"If you help me look, I can give you my lighter.\""
                    menu:
                        s "\"It will bypass the thumbprint security on the submarine terminal and call it back allowing us to escape.\""

                        "\"I'll help. What am I looking for?\"":
                            s "\"I need at least three more pieces of evidence before we leave.\""
                            s "\"Any kind of documentation or personal accounts mentioning the parasite would be extremely helpful.\""
                            menu:
                                s "\"A specimen is very unlikely but would be most helpful.\""

                                "\"I'll get looking right away.\"":
                                    s "\"Excellent. I would begin searching in the pile of crates over there.\""
                                    $sketalks = 1
                                    jump moonpool
                        "\"Parasite?\"":
                            s "\"You haven't felt it? That rogue twitch of a muscle?\""
                            s "\"That voice begging to be returned to its mother? Surely you have.\""
                            s "\"These people here, these cultists...\""
                            s "\"They implant these parasites into anyone they can get a hold of.\""
                            s "\"And once they do - there's no reason not for you to follow them into their twisted vision of an afterlife.\""
                            menu:
                                s "\"Which is certain death at the hands of a pair of lungs full of water.\""

                                "\"I... I have. I must be infected.\"":
                                    s "\"Then your only safe course of action is to get off of this boat.\""
                                    s "\"Help me, and I will take you personally to get some real medical attention.\""
                                    s "\"I would begin searching for evidence in the pile of crates over there.\""
                                    s "\"I need at least three more pieces of evidence before we leave.\""
                                    s "\"Any kind of documentation or personal accounts mentioning the parasite would be extremely helpful.\""
                                    menu:
                                        s "\"A specimen is very unlikely but would be most helpful.\""

                                        "\"Thank you.\"":
                                            $sketalks = 1
                                            jump moonpool

                        "\"I have no such parasite within me. You're delusional.\"" if skeswitch == False:
                            $skesus += 1
                            call skesus_check from _call_skesus_check
                            jump skebad


            "\"More than I ever have. I am to become an ascendant!\"":
                $skesus += 1
                call skesus_check from _call_skesus_check_1

                jump skebad

                label skebad:
                    t "You notice a dramatic shift of moods from the woman."
                    s "\"Excellent.\""
                    menu:
                        s "\"They've infected you with not only one of their disgusting worms, but their fanatic drivel too.\""

                        "\"You misunderstand. I've had to pretend to be one of them since I awoke.\"":
                            $skesus -= 1
                            call skesus_check from _call_skesus_check_2
                            "\"I was only being cautious, but it's nice to meet a normal person.\""
                            s "\"Thank God. Not only a sane person, but a smart one too.\""
                            $skeswitch = True
                            jump skegood

                        "\"It's not a worm. It is one of Her children, which I will soon join the ranks of!\"":
                            $skesus += 1
                            call skesus_check from _call_skesus_check_3
    elif sketalks == 1:
        if evidence == 3:
            s "\"Great work. We can finally leave.\""
            s "\"Head over to the terminal, and we can leave.\""
            jump moonpoolRitual
        elif evidence == 2:
            s "\"These are excellent. I need a little more, but after than we can get out of here.\""
            jump moonpool
        elif evidence == 1:
            s "\"This is excellent. I need a little more, but after than we can get out of here.\""
            jump moonpool
        elif evidence == 0:
            s "\"Have you found anything yet?\""
            s "\"I would begin searching in the pile of crates over there.\""
            jump moonpool

label skesus_check:
    #function to use when adding sus
    #$skesus += 1
    #call skesus_check
    if skesus == 0:
        hide screen suspicion_overlay
    if skesus > 0:
        show screen suspicion_overlay
    if skesus == 2:
        jump death