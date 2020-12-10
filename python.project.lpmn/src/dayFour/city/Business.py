class Business:

    def __init__(self, nameBusiness):
        self._nameBusiness = nameBusiness
        self._buildings = []
        self._cities = []
    
    #Getter
    @property
    def nameBusiness(self):
        return self._nameBusiness

    #Setter
    @nameBusiness.setter
    def nameBusiness(self, nameBusiness):
        self._nameBusiness = nameBusiness
    
    def getCities(self):
        return self._cities
    
    def addCities(self, city):
        if len(city) == 0:
            return 0
        if city not in self._cities:
            self._cities.append(city)
            
    def removeCities(self, city):
        if len(city) == 0:
            return 0
        if city in self._cities:
            self._cities.remove(city)

    # def getAllEmployees(self):
    #     return len(self._employees)