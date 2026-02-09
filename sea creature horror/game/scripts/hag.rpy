label hagtalk:
    
    "An elderly woman seems to be reflecting, meditating, or praying in soem sort of way. She pays you no mind until you walk closer to her."
    
    menu:
        h "Ahh! Another young aspirant come to witness the birth of the new earth!"

        "What are you talking about?":
            $hagsus += 1
            if hagsus == 2: 
                jump death
            
            else:
                h "You clearly are no aspirant. Leave me."
                jump cargo
        
        "Well of course! Do you know where everyone went?":
            menu:
                h "It matters not dear one! We shall all be her children in her cold embrace. Glory to the One Below!"

                "And may she return above!":
                    "WIP"

                "Okay... Do you seriously not know where everyone went?":
                    $hagsus += 1

                "You seem to be stuck just as much as I am. Do you know a way out?":
                    $hagsus += 1
            
        
        "(Leave)":
            jump cargo

        