class Livre:
    def __init__(self, titre, auteur, nombrePage, disponible=True):
        self._titre = titre
        self._auteur = auteur
        self._nombrePage = nombrePage
        self._disponible = disponible

        if not isinstance(nombrePage, int):
            raise ValueError("Le nombre de pages doit être un nombre entier.")


    def get_disponible(self):
        return self._disponible
    
    def set_disponible(self, disponible):
        self._disponible = disponible

    def emprunter(self):
        # print(f"method emprunter Avant emprunt - Disponibilité : {self.get_disponible()}")

        if self.get_disponible():
            self.set_disponible(False)
            print("Livre emprunté.")
        else:
            print("Le livre n'est pas disponible.")

        # print(f" method emprunter Après emprunt - Disponibilité : {self.get_disponible()}")

    def rendre(self):
        # print(f"method rendre Avant rendu - Disponibilité : {self.get_disponible()}")

        if self.get_disponible():
            print("Livre disponible.")
        else:
            print("Livre pas encore rendu")
            self.set_disponible(True)
            print("Livre rendu")

        # print(f" method rendre Après rendu - Disponibilité : {self.get_disponible()}")


# Création d'une instance de la classe Livre
livre = Livre("Fables de La Fontaine", "Jean de La Fontaine", 110)

# Emprunter le livre
livre.emprunter()

# Rendre le livre
livre.rendre()