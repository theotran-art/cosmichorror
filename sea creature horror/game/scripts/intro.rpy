label intro: # The game starts here.
    #scene black image

    "Your head throbs. Your body shakes uncontrollably. You know not where you are or how you got here. Any attempt to rack your brain results in a surge of your already pounding headache."
    
    menu:
        "Attempt to search your memories once more.": #dont forget the colon
            #Branching path/different dialogue triggered
            "Against all instinct, you rage through your migraine-bordering headache. Single, isolated images drip into your consciousness like water from unserviced faucet."
            "A masked man."
            "His reaching hand."
            "The boarding of a boat."
            "That is all you can glean for now. It may be best to attempt to remember more from your surroundings."
            jump cargo
        "Attempt to gain your bearings.":
            #Branching path/different dialogue triggered
            jump cargo