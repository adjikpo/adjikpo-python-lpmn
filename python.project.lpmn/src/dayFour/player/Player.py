class Player:

    def __init__(self, name, level):
        self._name = name
        self._level = level
    
    def whoami(self):
        print(" {} ({}) ".format(self._name, self._level))