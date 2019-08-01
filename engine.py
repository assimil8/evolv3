import tcod as libtcod

from input_handlers import handle_keys
from entity import Entity
from render_functions import render_all,clear_all
from map_objects.game_map import GameMap

def main():
    #eventually we will load these values from a JSON file vs. hardcoding them
    screen_width = 80
    screen_height = 50
    map_width = 80
    map_height = 45

    #reminiscent of gdscripts 'quick struct', this is blocked tile vs. passable
    colors = {
        'dark_wall': libtcod.Color(44,0,12),
        'dark_ground': libtcod.Color(0, 0, 0)
        }

    player = Entity(int(screen_width/2),int(screen_height/2),'@', libtcod.red)
    npc = Entity(int(screen_height/2 - 5),int(screen_height/2), '@', libtcod.yellow)
    entities = [npc,player]

    #specify font, tell which type of file
    libtcod.console_set_custom_font('arial10x10.png', libtcod.FONT_TYPE_GRAYSCALE | libtcod.FONT_LAYOUT_TCOD)
    #instantiate window with w,h, title and full screen bool
    libtcod.console_init_root(screen_width,screen_height,'evolv3',False)

    con = libtcod.console_new(screen_width,screen_height)

    game_map = GameMap(map_width, map_height)
    game_map.make_map()
    
    #store keyboard and mouse input
    key = libtcod.Key()
    mouse = libtcod.Mouse()

    #our game loop; while window isn't closed do the following
    while not libtcod.console_is_window_closed():
        #capture new events (user input), update key and mouse vars
        libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS,key,mouse)
        render_all(con,entities,game_map,screen_width,screen_height, colors)
        

        #flush pushes to screen
        libtcod.console_flush()
        clear_all(con, entities)

        libtcod.console_put_char(con,player.x,player.y,' ', libtcod.BKGND_NONE)
        libtcod.console_put_char(0,player.x,player.y,' ', libtcod.BKGND_NONE)

        action = handle_keys(key)

        move = action.get('move')
        exit = action.get('exit')
        fullscreen = action.get('fullscreen')

        if move:
            #move is a tuple
            dx, dy = move
            if not game_map.is_blocked(player.x + dx, player.y + dy):
                player.move(dx,dy)

        if exit:
            return True

        if fullscreen:
            libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())

if __name__ == '__main__':
	main()