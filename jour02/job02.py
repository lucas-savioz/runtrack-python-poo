class Livre:
    def __init__(self, titre, auteur, nombrePage):
        self._titre = titre
        self._auteur = auteur

        if not isinstance(nombrePage, int):
            raise ValueError("Le nombre de pages doit être un nombre entier.")
        
        self._nombrePage = nombrePage
    
    def get_livre(self):
        return self._titre, self._auteur, self._nombrePage
    
    def set_livre(self, nouveau_titre, nouveau_auteur, nouveau_nombrePage):
        self._titre = nouveau_titre
        self._auteur = nouveau_auteur

        if not isinstance(nouveau_nombrePage, int):
            raise ValueError("Le nouveau nombre de pages doit être un nombre entier.")

        self._nombrePage = nouveau_nombrePage

# Instanciation de l'objet
livre = Livre("Fables de La Fontaine", "Jean de La Fontaine", 110)

# Utilisation du mutateur pour modifier les informations du livre
livre.set_livre("Harry Potter", "J. K. Rowling", 260)

# Utilisation de l'accesseur pour obtenir les informations du livre
nouvelles_infos_livre = livre.get_livre()

# Affichage
print("Le nouveau livre est :", nouvelles_infos_livre)
