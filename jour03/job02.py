class CompteBancaire:
    def __init__(self, numero_compte, nom, prenom, solde, decouvert=False):
        self.__numero_compte = numero_compte
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.__decouvert = decouvert

    def afficher(self):
        print(f"Compte n°{self.__numero_compte} {self.__prenom} {self.__nom}")
        print(f"Solde: {self.__solde} €")

    def afficherSolde(self):
        print(f"Solde actuel: {self.__solde} €")

    def versement(self, montant):
        self.__solde += montant
        print(f"Versement de {montant} € effectué. Nouveau solde: {self.__solde} €")

    def retrait(self, montant):
        if self.__solde >= montant or self.__decouvert:
            self.__solde -= montant
            print(f"Retrait de {montant} € effectué. Nouveau solde: {self.__solde} €")
        else:
            print("Opération impossible. Solde insuffisant.")

    def agios(self, taux_agios):
        if self.__solde < 0:
            agios = abs(self.__solde) * (taux_agios / 100)
            self.__solde -= agios
            print(f"Agios appliqués. Nouveau solde: {self.__solde} €")

    def virement(self, compte_destinataire, montant):
        if self.__solde >= montant or self.__decouvert:
            self.__solde -= montant
            compte_destinataire.versement(montant)
            print("Virement effectué avec succès.")
        else:
            print("Opération impossible. Solde insuffisant.")

# Création de deux instances de la classe CompteBancaire
compte1 = CompteBancaire(numero_compte=1, nom="Doe", prenom="John", solde=5000)
compte2 = CompteBancaire(numero_compte=2, nom="Smith", prenom="Alice", solde=-1000, decouvert=True)

# Affichage des détails des comptes
compte1.afficher()
compte2.afficher()

# Versement sur le compte 1
compte1.versement(2000)

# Retrait sur le compte 1
compte1.retrait(1000)

# Application d'agios sur le compte 2
compte2.agios(taux_agios=2)

# Virement du compte 1 vers le compte 2
compte1.virement(compte_destinataire=compte2, montant=1500)

# Affichage des nouveaux solde
compte1.afficherSolde()
compte2.afficherSolde()
