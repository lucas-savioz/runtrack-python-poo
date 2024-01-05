class Commande:
    def __init__(self, numCommande, statusCommande="en cours"):
        self.__numCommande = numCommande
        self.__platsCommandes = {}
        self.__statusCommande = statusCommande

    def ajouter_plat(self, nom, prix):
        if self.__statusCommande == "en cours":
            self.__platsCommandes[nom] = {"prix": prix, "statut": "en cours"}
            print(f"Plat '{nom}' ajouté à la commande.")
        elif self.__statusCommande == "annulée":
            print("Impossible d'ajouter un plat, la commande est annulée.")
        else:
            print("Votre commande est terminée.")

    def annuler_commande(self):
        if self.__statusCommande == "en cours":
            print("Commande en cours.")
            self.__statusCommande = "en cours"
        elif self.__statusCommande == "annulée":
            print("La commande est déjà annulée.")
        else:
            print("Impossible d'annuler la commande, elle est déjà terminée.")

    def total_commande(self):
        if self.__statusCommande == "en cours":
            total = sum(plat["prix"] for plat in self.__platsCommandes.values() if plat["statut"] == "en cours")
            return total
        elif self.__statusCommande == "terminée":
            total = sum(plat["prix"] for plat in self.__platsCommandes.values() if plat["statut"] == "terminée")
            return total
        else:
            print("La commande est annulée, aucun total disponible.")
            return 0

    def afficher_commande(self):
        print(f"Commande #{self.__numCommande}")
        for plat, details in self.__platsCommandes.items():
            print(f"{plat}: {details['prix']} € ({details['statut']})")
        print(f"Total à payer: {self.total_commande()} €")

    def calculer_tva(self, taux_tva):
        total_tva = self.total_commande() * (taux_tva / 100)
        return total_tva

    def commander_terminee(self):
        if self.__statusCommande == "terminée":
            print("Votre commande est déjà terminée.")
            self.afficher_commande()
            montant_tva = self.obtenir_total_tva(taux_tva=20)
            print(f"Montant total de la TVA: {montant_tva} €")
            total_commande = self.total_commande()
            print(f"Total de la commande: {total_commande} €")
        elif self.__statusCommande == "en cours":
            print("Votre commande est en cours. Veuillez patienter.")
        else:
            self.__statusCommande = "annulée"
            print("La commande est annulée, aucune action supplémentaire possible.")

    def obtenir_total_tva(self, taux_tva):
        total_tva = self.calculer_tva(taux_tva)
        return total_tva

    # Ajout d'une méthode pour obtenir le statut de la commande
    def get_status_commande(self):
        return self.__statusCommande

# Création d'une instance de la classe Commande
commande1 = Commande(numCommande=1)

# Appel de la méthode pour ajouter un plat à la commande
commande1.ajouter_plat(nom="Pizza", prix=10)

# Appel de la méthode pour annuler la commande
commande1.annuler_commande()

# Appel de la méthode pour obtenir le total de la commande
total_commande = commande1.total_commande()

# Appel de la méthode pour afficher les détails de la commande
commande1.afficher_commande()

# Appel de la méthode pour commander la terminaison
commande1.commander_terminee()

# Appel de la méthode pour obtenir le total de la TVA
montant_tva = commande1.obtenir_total_tva(taux_tva=20)

# Affichage du montant de la TVA
print(f"Montant total de la TVA: {montant_tva} €")

# Imprimer le total de la commande uniquement si le statut est "terminée"
if commande1.get_status_commande() == "terminée":
    print(f"Total de la commande: {total_commande} €")
