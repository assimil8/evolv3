import tcod as libtcod

"""
    movement stored and defined as key/val pairs in dictionary
"""

def handle_keys(key):
    #movement keys, all return dict values that will be
    #stored in 'action' var in engine.py
    if key.vk == libtcod.KEY_UP:
        return {'move': (0,-1)}
    elif key.vk == libtcod.KEY_DOWN:
        return {'move':(0,1)}
    elif key.vk == libtcod.KEY_LEFT:
        return {'move':(-1,0)}
    elif key.vk == libtcod.KEY_RIGHT:
        return {'move':(1,0)}

    if key.vk == libtcod.KEY_ENTER and key.lalt:
        #alt+enter: toggle full screen
        return {'fullscreen': True}
    
    elif key.vk == libtcod.KEY_ESCAPE:
        #exit game
        return {'exit': True}

    #no key pressed
    return{}