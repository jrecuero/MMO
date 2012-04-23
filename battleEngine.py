#!/usr/bin/env python

class Weapon(object):
    """ """
    
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
        self.weakness   = None
        self.inmune     = None
        self.robustness = None
        self.life       = 0
        pass

    def isAlive(self):
        return self.life > 0
    

class BattleEngine(object):
    """ """
    
    def __init__(self):
        pass
    
