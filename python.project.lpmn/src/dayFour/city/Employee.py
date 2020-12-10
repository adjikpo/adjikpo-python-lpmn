class Employee:

    def __init__(self,firstname, lastname):
        self._firstname = firstname
        self._lastname = lastname

    #Getter
    @property
    def firstname(self):
        return self._firstname

    #Setter
    @firstname.setter
    def firstname(self, firstname):
        self._firstname = firstname

    #Getter
    @property
    def lastname(self):
        return self._lastname

    #Setter
    @lastname.setter
    def lastname(self, lastname):
        self._lastname = lastname