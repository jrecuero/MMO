#!/usr/bin/env python

class Weapon(object):
    """ """

    Type = { 'SLASH' : 0, 'BLUNT' : 1 }

    def __init__(self):
        pass
    
    
class Magic(object):
    """ """
    
    def __init__(self):
        pass
    

class Actor(object):
    """ """

    def __init__(self, name):
        self.name       = name
        self.weakness   = []
        self.inmune     = []
        self.robustness = []
        self.life       = 0
        pass

    def isAlive(self):
        return self.life > 0
    
    def setWeakness(self, weak):
        self.weakness.append(weak)

class BattleEngine(object):
    """ """
    
    def __init__(self):
        pass
  
if __name__ == '__main__':
    actor = Actor('x')
    actor.setWeakness(Weapon.Type['BLUNT'])
    print actor.weakness
