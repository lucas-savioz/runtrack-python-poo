class Ville:
    def __init__(self, nom, nombre_habitants):
        self.__nom = nom
        self.__nombre_habitants = nombre_habitants

    def get_nom(self):
        return self.__nom

    def get_nombre_habitants(self):
        return self.__nombre_habitants

    def ajouter_population(self):
        self.__nombre_habitants += 1


class Personne:
    def __init__(self, nom, age, ville):
        self.__nom = nom
        self.__age = age
        self.__ville = ville
        self.__ville.ajouter_population()

    def ajouter_population(self):
        self.__ville.ajouter_population()


# Création des objets Ville
ville_paris = Ville("Paris", 1000000)
ville_marseille = Ville("Marseille", 861635)

# Affichage du nombre d'habitants initial des villes
print(f"Nombre d'habitants à {ville_paris.get_nom()}: {ville_paris.get_nombre_habitants()}")
print(f"Nombre d'habitants à {ville_marseille.get_nom()}: {ville_marseille.get_nombre_habitants()}")

# Création des objets Personne
john = Personne("John", 45, ville_paris)
myrtille = Personne("Myrtille", 4, ville_paris)
chloe = Personne("Chloé", 18, ville_marseille)

# Affichage du nombre d'habitants après l'arrivée des nouvelles personnes
print(f"Nombre d'habitants à {ville_paris.get_nom()} après l'arrivée de John et Myrtille: {ville_paris.get_nombre_habitants()}")
print(f"Nombre d'habitants à {ville_marseille.get_nom()} après l'arrivée de Chloé: {ville_marseille.get_nombre_habitants()}")
