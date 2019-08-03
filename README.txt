I've created a python package by placing an empty __init__.py in our map_objects directory. This package will be where tile, rectangle, game_map, etc. classes will exist (hence the dir name).

This divides the project up logically and exercises good coding practice(s).


Currently working on reading .xp files from REXpaint into the console as a map/characters/etc. using XpLoaderPy3.
  - Need to solve layers, layer0 = map, layer1 = player, npcs, layer2 = environment_decoration
  - Need to integrate XpLoader's main into 'engine.py'
