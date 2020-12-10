class City:

    #Construstor
    def __init__(self, nameCity):
        self._nameCity = nameCity
        self._buildings = []
    
    #Getter
    @property
    def nameCity(self):
        return self._nameCity

    #Setter
    @nameCity.setter
    def nameCity(self, nameCity):
        self._nameCity = nameCity

    def getBuilding(self):
        return self._buildings
    
    def addBuilding(self, building):
        if len(building) == 0:
            return 0
        if building not in self._buildings:
            self._buildings.append(building)
            
    def removeBuilding(self, building):
        if len(building) == 0:
            return 0
        if building in self._buildings:
            self._buildings.remove(building)

    # def getAllCities(self):
    #     return len(self._buildings)
        