init python:
    def allow_edge_scroll():
        x, y = renpy.get_mouse_pos()
        return x < 1620
    
screen uiWindow:
    layer "ui"
    add "gui/customui/fishgame ui.png"