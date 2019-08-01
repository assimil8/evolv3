# we need functions that draw every entity in our list

import tcod as libtcod
"""
called in our game loop to draw entities, map,etc. Currently accepts console, 
a list of entities, and the screen w,h as parameters and calls draw_entity on each.
Then it blits the changes to the screen.

UPDATE: render all now loops through each tile in the game map and checks
if it blocks sight or not. If it does, then it draws a wall, if not, it draws
a floor.
"""
def render_all(con, entities, game_map, screen_width, screen_height, colors):
    #draw all tiles in our games map
    for y in range(game_map.height):
        for x in range(game_map.width):
            wall = game_map.tiles[x][y].block_sight

            if wall:
                libtcod.console_set_char_background(con, x, y, colors.get('dark_wall'), libtcod.BKGND_SET)
            else:
                libtcod.console_set_char_background(con, x, y, colors.get('dark_ground'), libtcod.BKGND_SET)

    for entity in entities:
        draw_entity(con, entity)

    libtcod.console_blit(con, 0, 0, screen_width, screen_height, 0, 0, 0)

def clear_all(con, entities):
    for entity in entities:
        clear_entity(con, entity)

"""
draw_entity is what does the actual drawing. uses entities (x,y, char and color)
flexible enough atm to handle all entities invented
"""
def draw_entity(con, entity):
    libtcod.console_set_default_foreground(con, entity.color)
    libtcod.console_put_char(con, entity.x, entity.y, entity.char, libtcod.BKGND_NONE)

#clears entity so no trailing occurs
def clear_entity(con, entity):
    libtcod.console_put_char(con, entity.x, entity.y, ' ', libtcod.BKGND_NONE)

