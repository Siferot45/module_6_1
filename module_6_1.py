from Flower import Flower
from Mammal import Mammal
from Predator import Predator
from Fruit import Fruit

a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')

p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(f"{p1.name}\n")

print(f"{a1.name} живой: {a1.alive}")
print(f"{a2.name} накормленный: {a2.fed}\n")

a1.eat(p1)
a2.eat(p2)
print("\n")

print(f"{a1.name} живой: {a1.alive}")
print(f"{a2.name} накормленный: {a2.fed}")

