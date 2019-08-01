class Tile:
    
#A tile on a map. May OR may not be blocked, may OR may not block sight

    def __init__(self, blocked, block_sight=None):
        self.blocked = blocked

        #by default, if tile is blocked, it also blocks sight
        if block_sight is None:
            block_sight = blocked

        self.block_sight = block_sight

