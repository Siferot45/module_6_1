
class Animal:
    
    def __init__(self, name):
        
        self.name = name
        self.alive = True
        self.fed = False
        
    def eat(self, food):
        
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
            
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False