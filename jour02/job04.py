class Student:
    def __init__(self, nom, prenom, numEtudiant, credit):
        self.__nom = nom
        self.__prenom = prenom
        self.__numEtudiant = numEtudiant
        self.__credit = credit
    
    def add_credits(self):

        if self.__credit <= 0:
            print("Vos crédit doivent être supérieur à 0.")
        else:
            print("Le nombre de crédits de", self.__prenom, self.__nom, "est de", self.__credit)

        while self.__credit < 30:
                self.__credit += 10
                print("Le nombre de crédits de", self.__prenom, self.__nom, "est de", self.__credit)
    
    def studentEval(self):
         
        if self.__credit >= 90:
            print("Excellent")
        elif self.__credit >= 80:
            print("Très bien")
        elif self.__credit >= 70:
            print("Bien")
        elif self.__credit >= 60:
            print("Passable")
        else:
            self.__credit < 60
            print("Insuffisant")

# Création d'une instance de la classe Student
etudiant = Student("Doe", "John", 145, 100)

# Appel de la méthode add_credits
etudiant.add_credits()

etudiant.studentEval()