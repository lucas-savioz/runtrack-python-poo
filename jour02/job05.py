class Voiture:
    def __init__(self, marque, modele, annee, kilometrage, en_marche=True, reservoir=50):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__kilometrage = kilometrage
        self.__en_marche = en_marche
        self.__reservoir = reservoir

    # Assesseurs
    def get_marque(self):
        return self.__marque

    def get_modele(self):
        return self.__modele

    def get_annee(self):
        return self.__annee

    def get_kilometrage(self):
        return self.__kilometrage

    def get_en_marche(self):
        return self.__en_marche

    def get_reservoir(self):
        return self.__reservoir

    # Mutateurs
    def set_marque(self, nouvelle_marque):
        self.__marque = nouvelle_marque

    def set_modele(self, nouveau_modele):
        self.__modele = nouveau_modele

    def set_annee(self, nouvelle_annee):
        self.__annee = nouvelle_annee

    def set_kilometrage(self, nouveau_kilometrage):
        self.__kilometrage = nouveau_kilometrage

    def set_en_marche(self, nouvel_etat):
        self.__en_marche = nouvel_etat

    def set_reservoir(self, nouveau_reservoir):
        self.__reservoir = nouveau_reservoir

    # Méthode privée
    def __verifier_plein(self):
        return self.__reservoir

    # Méthodes publiques
    def demarrer(self):
        if self.__verifier_plein() > 5:
            self.__en_marche = True
            print("La voiture a démarré.")
        else:
            print("Le réservoir est trop bas. La voiture ne peut pas démarrer.")

    def arreter(self):
        self.__en_marche = False
        print("La voiture s'est arrêtée.")


# Exemple d'utilisation de la classe Voiture
ma_voiture = Voiture("Tesla", "model S", 2022, 10000)

# Affichage des informations initiales
print("Informations initiales de la voiture:")
print("Marque:", ma_voiture.get_marque())
print("Modèle:", ma_voiture.get_modele())
print("Année:", ma_voiture.get_annee())
print("Kilométrage:", ma_voiture.get_kilometrage())
print("En marche:", ma_voiture.get_en_marche())

# Démarrage de la voiture
ma_voiture.demarrer()

# Arrêt de la voiture
ma_voiture.arreter()
