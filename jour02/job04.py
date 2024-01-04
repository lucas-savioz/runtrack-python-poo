class Student:
    def __init__(self, nom, prenom, numEtudiant, credit):
        self.__nom = nom
        self.__prenom = prenom
        self.__numEtudiant = numEtudiant
        self.__credit = credit
        self.__level = self.studentEval()
    
    def add_credits(self):
        if self.__credit <= 0:
            print("Vos crédits doivent être supérieurs à 0.")
        else:
            print("Le nombre de crédits de", self.__prenom, self.__nom, "est de", self.__credit)

        while self.__credit < 30:
            self.__credit += 10
            print("Le nombre de crédits de", self.__prenom, self.__nom, "est de", self.__credit)

    def studentEval(self):
        if self.__credit >= 90:
            return "Excellent"
        elif self.__credit >= 80:
            return "Très bien"
        elif self.__credit >= 70:
            return "Bien"
        elif self.__credit >= 60:
            return "Passable"
        else:
            return "Insuffisant"

    def studentInfo(self):
        print("Nom:", self.__nom)
        print("Prénom:", self.__prenom)
        print("Identifiant:", self.__numEtudiant)
        print("Niveau:", self.__level)

# Création d'une instance de la classe Student
etudiant = Student("Doe", "John", 145, 100)

# Appel de la méthode add_credits
etudiant.add_credits()

# Appel de la méthode studentEval
etudiant.studentEval()

# Appel de la méthode studentInfo
etudiant.studentInfo()
