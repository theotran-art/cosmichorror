init python:
    def allow_edge_scroll():
        x, y = renpy.get_mouse_pos()
        return x < 1620

screen uiWindow:
    layer "ui" 
    add "gui/customui/uioverlay.png"

    imagebutton: #settings
        pos (1755,51) #where it appears on the screen
        auto "gui/customui/settings_%s.png" action Jump("uiSettings")
    if hide_inventory is False:
        if inventory_open == False:
            add "gui/customui/inventory.png":
                pos (1703,175)
        add "gui/customui/brain1.png":
            pos (1723,895)
        if inventory_open == False:
            textbutton "{size=28}Inventory":
                pos (1737,192)
                action Show("inventoryView"), SetVariable("inventory_open", True), SetVariable("cargo_buttons_enabled", False), SetVariable("cargo_scroll_enabled", False)


label uiSettings:
    "hi"
