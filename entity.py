"""
    generic object to represent players, items, enemies, etc.
    Entity will represent just about everything in our game world.
"""

class Entity:
    
    def __init__(self,x,y,char,color):
        self.x = x
        self.y = y
        self.char = char
        self.color = color

    def move(self,dx,dy):
        #move the entity by a given amount. Ex: in engine will call entity_type.move(dx,dy)
        self.x += dx
        self.y += dy

