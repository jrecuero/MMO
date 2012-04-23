#!/usr/bin/env python

class Weapon(object):
    
    def __init__(self):
        pass
    
    
class Magic(object):
    
    def __init__(self):
        pass
    

class Actor(object):

    def __init__(self, name):
        self.name       = name
        self.weakness   = None
        self.inmune     = None
        self.robustness = None
        pass


class BattleEngine(object):
    
    def __init__(self):
        pass
    