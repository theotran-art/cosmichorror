#code by Discover with Mia on YouTube
init python:

    #images
    inventory_icon = ["images/items/.png", "images/items/.png", "images/items/.png"]

    #item_name
    item_name = {
        "images/items/.png": "A",
        "images/items/.png": "B",
        "images/items/.png": "C",
    }

    #description of item
    description = {
        "images/items/.png": "aa",
        "images/items/.png": "bb",
        "images/items/.png": "cc",        
    }

    #name of the item (variable)
    name_item = ""

    story_name = ""

    #show description (variable)
    show_description = ""

    #show the selected item (variable)
    show_item = ""

    #check if inventory is open
    open_inventory = False

#persistent list for check item
default persistent.choice = []

#persistent dictionary
default persistent.using_item = {
    "images/items/.png": False,
    "images/items/.png": False,
    "images/items/.png": False,    
}

screen inventory_button:
    hbox:
        xalign 1.0
        yalign 0.0
        textbutton "Show Inventory" action [Show("inventory_screen"), Hide("inventory_button")]
        #image ".png" #image of what to click on for the inventory

screen inventory_screen:
    modal True
    add "background_inventory"
    grid 1 3:
        xalign 0.5
        yalign 0.2

        for item in inventory_icon:
            if item in persistent.choice:
                frame:
                    imagebutton idle item action [SetVariable("name_item", (item_name.get(item))), SetVariable("show_description", (description.get(item))), SetVariable("show_item", item), ToggleVariable("open_inventory", True)]
            elif item 
                frame:
                    image ".png"

    #show description and use button if open_inventory is True
    if open_inventory == True:
        frame:
            background frame(Solid("#HEXCODE")) #put in color
            xfill True
            xalign 0.5
            yalign 1.0
            vbox
                for item in inventory_icon:
                    if item in persistent.choice and item in show_item:
                        text name_item
                        image item 
                        text show_description
                        frame:
                            xalign 1.0
                            yalign 1.0
                            if persistent.using_item[item] == True:
                                textbutton "Use" action [RemoveFromSet(persistent.choice, item), Notify(item_name(item))]
                            else:
                                textbutton "Use" action Notify(item_name[item]+" can't be used now.")

    textbutton "Close Inventory" action [Hide("inventory_screen"), Show"inventory_button", ToggleVariable("open_inventory", False)] xalign 1.0 yalign 0.0

