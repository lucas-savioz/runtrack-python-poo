import random

class Personnage:

    def __init__(self, nom, vie):
        self.nom = nom
        self.vie = vie
    
    def attaquer(self, adversaire):
        attaque1 = 15
        attaque2 = 40
        degats = random.randint(attaque1, attaque2)
        degats_crit = 2 * attaque2  # Attaque critique
        print(f"{self.nom} attaque {adversaire.nom} et lui inflige {degats} points de dégâts.")
        if random.random() < 0.2:  # 20% de chance pour une attaque critique
            print(f"{self.nom} attaque critique {adversaire.nom} et lui inflige {degats_crit} points de dégâts !")
            adversaire.vie -= degats_crit
        else:
            adversaire.vie -= degats

class Jeu:
    def __init__(self):
        self.niveau = 1
    
    def choisirNiveau(self):
        while True:
            try:
                niveau = int(input("Choisissez le niveau des pokémon (entre 1 et 100) : "))
                if 1 <= niveau <= 100:
                    self.niveau = niveau
                    break
                else:
                    print("Veuillez choisir un niveau entre 1 et 100.")
            except ValueError:
                print("Veuillez entrer un nombre valide.")

    def lancerJeu(self):
        self.choisirNiveau()
        vie_pkm1 = self.niveau * 5
        vie_pkm2 = self.niveau * 5
        pkm1 = Personnage("Pikachu", vie_pkm1)
        pkm2 = Personnage("Salamèche", vie_pkm2)

        while pkm1.vie > 0 and pkm2.vie > 0:
            pkm1.attaquer(pkm2)
            if pkm2.vie <= 0:
                print(f"{pkm2.nom} a été vaincu ! {pkm1.nom} a gagné la partie.")
                break
            
            pkm2.attaquer(pkm1)
            if pkm1.vie <= 0:
                print(f"{pkm1.nom} a été vaincu ! {pkm2.nom} a gagné la partie.")
                break

            print(f"{pkm1.nom} - Vie : {pkm1.vie} | {pkm2.nom} - Vie : {pkm2.vie}")

if __name__ == "__main__":
    jeu = Jeu()
    jeu.lancerJeu()