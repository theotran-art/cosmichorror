
#function to use when adding sus to cannibal
#$cansus += 1
#call cansus_check

label cannibaltalk:
    $kitchen_buttons_enabled = False 
    $kitchen_scroll_enabled = False

    $hide_inventory = True
    $characterTalk = True
    
    if kitchenDoorKey == False:
    
        #start of convo
        t "A lithe, gangly man sits above a nigh-unrecognizable pile of bodies."
        c "\"Hey! Snuck up on me a little there...\"" 
        c "\"Most people would have a little more self-preservation than to sneak up on a stranger like that.\"" 
        menu:            
            c "\"What brings you here, little ghost?\""

            "\"I'm... not sure. I can't remember. I just sort of woke up here.\"":
                label cann_talk_why:
                c "\"I remember seeing you asleep amongst the cargo. You're in for something special, you just don't know yet.\""
                t "The man quietly giggles to himself."
                label cann_talk_knife:
                p2 "YOU NEED HIS BLADE."
                menu:
                    "\"How willing would you be to part with that knife of yours?\"":
                        c "\"You hear it's call too, huh? As long as that's what it is, I could be persuaded.\"" 
                        menu:
                            c "\"As long as you don't plan to turn it on me.\""

                            "\"I won't. I'm not even sure what I need it for, but I don't plan on hurting you.\"":
                                c "\"I know what you need it for. What's more important is the key to the door over there.\"" 
                                c "\"It'll call you there sooner or later.\""
                                t "The cannibal hands you the dull blade."
                                $item_knife = True
                                c "\"Tell you what. You make this morsel here a bit more palateable, and the key is yours.\""
                                $kitchenArm = True
                                c "\"The prisoners down here were oh so stressed. Bad for the flesh.\""
                                menu:                                    
                                    "\"I can certainly try.\"":
                                        jump kitchen
                                    "Attack him.": 
                                        jump mg_canatt

            "\"Are you... eating those bodies?\"":
                c "\"What does it look like, little ghost?\"" 
                c "\"We all have our vices. Why do you think I aim to become an ascendant?\"" 
                c "\"While we wait though, my desires must be satiated.\"" 
                c "\"You wouldn't want me to start feasting on the living, would you?\""
                t "A horrible grin splits the cannibal's face in two. His question seemed rhetorical, yet he still looks to you eagerly. He twirls the knife in his hand."
                jump cann_talk_knife
            "\"I'm one of you. I aim to reach Her, and ascend my body.\"":
                $cansus += 1
                call cansus_check
                menu:
                    c "\"You shouldn't have to lie to me, little ghost. I am one of them, although they find me... unsavory.\""
                    
                    "\"I wonder why...\"":
                        $cansus += 1
                        call cansus_check
                        #unfinished
                    "\"You're one of them? Did you bring me here?\"":
                        jump cann_talk_why



$cansus += 1
call cansus_check

