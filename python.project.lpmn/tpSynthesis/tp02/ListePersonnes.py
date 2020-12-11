class ListePersonnes: 
    def __init__(self):
        self._personnes = []

    def get_personnes(self):
        return self._personnes

    def add_personnes(self,e):
		if e not in self._personnes:
			self._personnes.append(e)

    def remove_personnes(self,e):
        if e in self._personnes:
			self._personnes.remove(e)

    def find_by_nom(self, s: str):
        if len(s) == 0:
            return 0
        else:
            for personne in self._personnes:
                if personne.nom == s:
                    return self._personnes.__getattribute__(s)
                else:
                    return 0

    def exists_code(self, cp:str):
        if len(cp) == 0:
            return 0
        else:
            for personne in self._personnes:
                if personne.address == cp:
                    return True
                else:
                    return False