class Rectangle:
    def __init__(self, longueur, largeur):
        self._longueur = longueur
        self._largeur = largeur
    
    def get_rectangle(self):
        return self._longueur, self._largeur
    
    def set_rectangle(self, nouvelle_longueur, nouvelle_largeur):
        self._longueur = nouvelle_longueur
        self._largeur = nouvelle_largeur
        
rectangle = Rectangle(10, 5)

rectangle.set_rectangle(20, 10)

nouvelles_valeurs_rectangle = rectangle.get_rectangle()

print("Les dimensions du rectangle sont : ", nouvelles_valeurs_rectangle)