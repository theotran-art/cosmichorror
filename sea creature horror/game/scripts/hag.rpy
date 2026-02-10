label hagtalk:
    
    if item_page == False:
        t "An elderly woman seems to be reflecting, meditating, or praying in soem sort of way. She pays you no mind until you walk closer to her."
    
        menu:
            h "\"Ahh! Another young aspirant come to witness the birth of the new earth!\""

            "\"What are you talking about?\"":
                $hagsus += 1
                if hagsus == 2: 
                    jump death
            
                else:
                    h "\"You clearly are no aspirant. Leave me.\""
                    jump cargo
        
            "\"Well of course! Do you know where everyone went?\"":
                menu:
                    h "\"It matters not dear one! We shall all be her children in her cold embrace. Glory to the One Below!\""

                    "\"And may she return above!\"" if lookposter == True: #GOOD CHOICE ROUTE PT1
                        h "\"Ahhhhhhhh! You are a true aspirant!\"" 
                        h "\"It brings me great comfort to know I will not be embraced by my lonesome.\"" 
                        menu:
                            h "\"Tell me, would you care to join me in a reading of The Cephalonomicon?\""

                            "\"Of course.\"": #GOOD CHOICE PT2
                                t "She begins to read immediately after you accept."
                                t "She holds one of her arms out to the side, holding a small torn piece of paper in front of her face with the other, reciting,"
                                h "\"O Mother of the Great Deep,\""
                                h "\"we sever our love to our flesh to offer it to you alone,\""
                                h "\"flaying our imperfect forms as penance for the circumstances of our births.\""
                                h "\"Accept our immaciated bodies and deliver us,\"" 
                                h "\"for we yearn to be entangled in your cold embrace as the children of your new earth.\""
                                menu:
                                    "Hold your hands together and bow softly.":
                                        h "\"Such a respectful aspirant you are.\""
                                        menu:
                                            h "\"Tell me, do you wish to carry this passage with you into The Deep?\""

                                            "\"I... think that I need it.\"":
                                                $hagsus += 1
                                                if hagsus == 2: 
                                                    jump death
            
                                                else:
                                                    h "\"What an unkind little rat you are. Leave me.\""
                                                    jump cargo

                                            "\"Would you truly give it to me?\"": #GOOD CHOICE
                                                h "\"Oh dear, but this page is important to me!\""
                                                h "\"It was the passage I would read my grandson before bed every night.\""
                                                h "\"Of course, since he isn't coming with us, I suppose I could give it to you.\""
                                                menu:
                                                    h "\"But first, I must know if you are truly dedicated to following Her below.\""
                                                
                                                    "\"Of course I am! I have wished to be embraced in her ancient {i}arms{/i} for as long as I can remember.\"":
                                                        "WIP"

                                                    "\"Of course I am! I have wished to be embraced in her ancient {i}tendrils{/i} for as long as I can remember.\"": #GOOD CHOICE
                                                        menu:
                                                            h "\"And what do you make of her ascendants?\""

                                                            "\"They are our most holy guides, and their piscine forms are evidence of Her choosing them to do so.\"":
                                                                h "\"You are sure to be an ascendant, young one. Here, take the page. I can think of no one more deserving.\""
                                                                t "The old woman reaches her frail hand towards you, holding the old decrepit page." 
                                                                $item_page = True
                                                                t "You take it from her, and she gives you a smile that is somehow both warm and ice cold at the same time."
                                                                jump cargo

                                                            "\"Honestly, they creep me out a little bit.\"":
                                                                $hagsus += 1
                                                                if hagsus == 2: 
                                                                    jump death
                                        
                                                                else:
                                                                    jump cargo

                                                            "\"Who?\"":
                                                                $hagsus += 1
                                                                if hagsus == 2: 
                                                                    jump death
                                        
                                                                else:
                                                                    jump cargo

                                                    "\"Of course I am! I have wished to be embraced in her ancient {i}fins{/i} for as long as I can remember.\"":
                                                        "WIP"

                                        

                                    "\"What does that passage mean?\"":
                                        $hagsus += 1
                                        if hagsus == 2: 
                                            jump death
            
                                        else:
                                            h "\"If you were truly an aspirant, I would have to do no explaining. Leave me.\""
                                            jump cargo

                                    "Slowly inch away as she reads to inspect the room once more.":
                                        $hagsus += 1
                                        if hagsus == 2: 
                                            jump death
                                        
                                        else:
                                            jump cargo

                            "\"Of course! I have a passage in mind that I can't quite remember.\"" if readbook == True: #GOOD CHOICE + BOOK PT2.5
                                "\"It ends with, \"for we yearn to be entangled in your cold emabrace as the children of your new earth.\" or something like that.\""
                                h "\"I know exactly of which passage you speak!\""
                                t "She holds one of her arms out to the side, holding a small torn piece of paper in front of her face with the other, reciting,"
                                h "\"O Mother of the Great Deep,\""
                                h "\"we sever our love to our flesh to offer it to you alone,\""
                                h "\"flaying our imperfect forms as penance for the circumstances of our births.\""
                                h "\"Accept our immaciated bodies and deliver us,\"" 
                                menu:
                                    h "\"for we yearn to be entangled in your cold embrace as the children of your new earth.\""
                                    
                                    "\"Yes, that's it! I have such a hard time remembering the beginning. Is there any way I can trouble you for that page of yours?\"":
                                        h "\"Oh dear, but this page is important to me!\""
                                        h "\"It was the passage I would read my grandson before bed every night.\""
                                        h "\"Of course, since he isn't coming with us, I suppose I could give it to you.\""
                                        menu:
                                            h "\"But first, I must know if you are truly dedicated to following Her below.\""
                                                
                                            "\"Of course I am! I have wished to be embraced in her ancient {i}arms{/i} for as long as I can remember.\"":
                                                "WIP"

                                            "\"Of course I am! I have wished to be embraced in her ancient {i}tendrils{/i} for as long as I can remember.\"": #GOOD CHOICE
                                                menu:
                                                    h "\"And what do you make of her ascendants?\""

                                                    "\"They are our most holy guides, and their piscine forms are evidence of Her choosing them to do so.\"":
                                                        h "\"You are sure to be an ascendant, young one. Here, take the page. I can think of no one more deserving.\""
                                                        t "The old woman reaches her frail hand towards you, holding the old decrepit page." 
                                                        $item_page = True
                                                        t "You take it from her, and she gives you a smile that is somehow both warm and ice cold at the same time."
                                                        jump cargo

                                                    "\"Honestly, they creep me out a little bit.\"":
                                                        $hagsus += 1
                                                        if hagsus == 2: 
                                                            jump death
                                        
                                                        else:
                                                            jump cargo

                                                    "\"Who?\"":
                                                        $hagsus += 1
                                                        if hagsus == 2: 
                                                            jump death
                                        
                                                        else:
                                                            jump cargo

                                            "\"Of course I am! I have wished to be embraced in her ancient {i}fins{/i} for as long as I can remember.\"":
                                                "WIP"



                            "\"No thank you. I have other things to worry about.\"":
                                "WIP"

                    "\"Okay... Do you seriously not know where everyone went?\"":
                        $hagsus += 1
                        if hagsus == 2: 
                            jump death 
                        else:
                            h "\"What an unkind little rat you are. Leave me.\""
                            jump cargo

                    "\"You seem to be stuck just as much as I am. Do you know a way out?\"":
                        $hagsus += 1
                        if hagsus == 2: 
                            jump death
                        else:
                            h "\"You clearly are no aspirant. Leave me.\""
                            jump cargo
            
        
            "Leave.":
                jump cargo

    else:
        t "You already got what you needed from her. There's no need to talk to her further."
        jump cargo