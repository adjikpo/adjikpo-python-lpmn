class Addresse: 
    def __init__(self, rue, ville, code):
        self._rue = rue
        self._ville = ville
        self._code = code

    
    @property
    def rue(self):
        return self._rue

    @property
    def ville(self):
        return self._ville

    @property
    def code(self):
        return self._code

    @rue.setter
    def rue(self, rue):
        self._rue = rue

    @ville.setter
    def ville(self, ville):
        self._ville = ville

    @code.setter
    def code(self, code):
        self._code  = code 