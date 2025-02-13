class Fruit: # Klasside määratlus
    def __init__(self): # Konstruktor, mille abil algväärtustatakse objekti atribuudid
        self.name = "apple" # Algväärtustatakse nimi kui "apple"
        self.colour = "red"  # Algväärtustatakse värv kui "red"

my_fruit = Fruit() # Luuakse objekt my_fruit, millel on atribuudid name ja colour

my_fruit.colour = "green"  # Määratakse värv "green"
my_fruit.colour = "kiwi"  # Määratakse värv "kiwi", mis ületab eelmise väärtuse

print(my_fruit.colour) # Määratakse värv "kiwi", mis ületab eelmise väärtuse
print(my_fruit.name)  # Prinditakse objekti nimi, mis on "apple"