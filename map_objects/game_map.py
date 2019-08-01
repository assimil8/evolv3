from map_objects.tile import Tile
from map_objects.rectangle import Rect

"""
GameMap acts as a container for our Tile objects
Our map is going to consist of a 2d array of Tile objects. Tiles will have a few properties that define
traversibility/visibility
"""

class GameMap:
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.tiles = self.initialize_tiles()

    def initialize_tiles(self):
        #start with a completely walled off room, and then 'dig' out sections as we go
        tiles = [[Tile(True) for y in range(self.height)] for x in range(self.width)]
        return tiles

    def make_map(self):
        #create two rooms for demo purposes
        room1 = Rect(20,15,10,15)
        room2 = Rect(35,15,10,15)

        self.create_room(room1)
        self.create_room(room2)

    def create_room(self, room):
        """
            go through the tiles in the room(rect) and make them passable
            the +1 on both room.x1 and room.y1 means there will always be a wall between generated rooms
            UNLESS we deliberately create overlapping rooms
        """
        for x in range(room.x1+1, room.x2):
            for y in range(room.y1+1, room.y2):
                self.tiles[x][y].blocked = False
                self.tiles[x][y].block_sight = False

    def is_blocked(self, x, y):
        if self.tiles[x][y].blocked:
            return True

        return False