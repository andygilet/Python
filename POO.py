import math
class Voiture:
    voitures_crees = 0
    def __init__(self, marque, age):
        Voiture.voitures_crees += 1
        self.marque = marque
        self.age = age
    
    def afficher(self):
        print(f"La voiture est une {self.marque} et a {self.age}")
    
    @property
    def marqueV(self):
        return self.marque
    
    @marqueV.setter
    def marqueV(self, val):
        self.marque = val
        
    def changer_age(self, nouveau_age):
        self.age = nouveau_age
        if self.age > 100:
            raise ValueError("Send this car to the junkyard !!!")
        
    @classmethod
    def nbr_voiture(cls):
        print (cls.voitures_crees)
    
    @classmethod
    def from_str(cls, s):
        marque, age = s.split(',')
        return cls(marque, int(age))
    
    @classmethod
    def from_dict(cls, d):
        return cls(d["marque"], d["age"])
    
    @staticmethod
    def Calcul_circonference(rayon):
        return rayon * 2 * math.pi
    
class Citroen(Voiture):
    def __init__(self, age):
        super.__init__("Citroën", age)
    
    def message():
        print("coucou je suis une citroën")

class Audi(Voiture):
    def __init__(self, age):
        super.__init__("Audi", age)
        
    def message():
        print("Coucou je suis une Audi")
        
def car_message(car):
    print(car.marque)
    print("Message" + car.message())
            
voiture1 = Voiture("Lamborgini", 12)
voiture_string = Voiture.from_str("Toyota, 45")
voiture_dictionary = Voiture.from_dict({"marque" : "Jeep", "age" : 89})