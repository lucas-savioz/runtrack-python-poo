class Tache:

    def __init__(self, titre, description, status="À faire"):
        self.titre = titre
        self.description = description
        self.status = status

    def marquerCommeFinie(self):
        self.status = "Terminée"


class ListeDeTaches:

    def __init__(self):
        self.taches = []

    def ajouterTache(self, tache):
        self.taches.append(tache)

    def supprimerTache(self, tache):
        self.taches.remove(tache)

    def afficherListe(self):
        for tache in self.taches:
            print(f"Tâche : {tache.titre}, Description : {tache.description}, Statut : {tache.status}")

    def filterListe(self, statut):
        taches_filtrees = [tache for tache in self.taches if tache.status == statut]
        return taches_filtrees


# Création d'instances de Tache
tache1 = Tache("Faire les courses", "Acheter des fruits et légumes")
tache2 = Tache("Réviser pour l'examen", "Relire les chapitres 5 à 10")
tache3 = Tache("Faire du sport", "30 minutes de jogging")

# Création de l'instance de ListeDeTaches
liste_taches = ListeDeTaches()

# Ajout des tâches à la liste
liste_taches.ajouterTache(tache1)
liste_taches.ajouterTache(tache2)
liste_taches.ajouterTache(tache3)

# Affichage de la liste initiale
print("Liste initiale :")
liste_taches.afficherListe()

# Marquer une tâche comme terminée
tache2.marquerCommeFinie()

# Affichage de la liste mise à jour
print("\nListe mise à jour :")
liste_taches.afficherListe()

# Afficher les tâches à faire
taches_a_faire = liste_taches.filterListe("À faire")
print("\nTâches à faire :")
for tache in taches_a_faire:
    print(f"Tâche : {tache.titre}, Description : {tache.description}, Statut : {tache.status}")
