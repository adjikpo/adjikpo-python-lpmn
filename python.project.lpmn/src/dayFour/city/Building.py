class Building:

    def __init__(self, nameBuilding):
        self._nameBuilding = nameBuilding
        self._employees = []

    #Getter
    @property
    def nameBuilding(self):
        return self._nameBuilding

    #Setter
    @nameBuilding.setter
    def nameBuilding(self, nameBuilding):
        self._nameBuilding = nameBuilding

    def getEmployees(self):
        return self._employees
    
    def addEmployee(self, employee):
        if len(employee) == 0:
            return 0
        if employee not in self._employees:
            self._employees.append(employee)
            
    def removeEmployee(self, employee):
        if len(employee) == 0:
            return 0
        if employee in self._employees:
            self._employees.remove(employee)

    # def getAllEmployees(self):
    #     return len(self._employees)