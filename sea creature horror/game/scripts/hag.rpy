# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define mc = Character("You")
define h = Character("Hag")
define c = Character("Cannibal")
define s = Character("Skeptic")


# The game starts here.

label start:

    #BELOW IS DEFAULT TUTORIAL CODE

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    #scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #show eileen happy

    #These display lines of dialogue.

    # This ends the game.
    #return
    menu:
        "Question/Dialouge"
        "Choice 1": #dont forget the colon
            #Branching path/different dialogue triggered
            "1"
        "Choice 2":
            #Branching path/different dialogue triggered
            "2"
label partone:
    "I. The Cargo"
    "In the room the player wakes up in, there is an old, eccentric hag."
    "This eccentric elderly woman is an aspirant of the cult. She lived among commonfolk for the majority of her life, performing strange and unsettling rituals to gain the Cults attention. Finally, in her old age, she has been taken by them in order to become a full fledged member."
    "The player must interact with her and solve puzzles within room 1 in order to obtain the Excerpt, the passage from the Cult's holy texts that the player must read during the ritual."
    call minigametut
    
return