class Cal:  
    def __init__(self, a, b):  
        # Konstruktor, mis initsialiseerib kaks arvu  
        self.a = a  
        self.b = b  

    def liitmine(self):  
        # Liitmine: tagastab kahe arvu summa  
        return self.a + self.b  

    def lahutamine(self):  
        # Lahutamine: tagastab esimese arvu ja teise arvu vahe  
        return self.a - self.b  

    def korrutamine(self):  
        # Korrutamine: tagastab kahe arvu korrutise  
        return self.a * self.b  

    def jagamine(self):  
        # Jagamine: tagastab esimese arvu ja teise arvu jagatise  
        if self.b == 0:  
            return "Jagamine nulliga ei ole lubatud!"  # Tagasta veateade, kui jagaja on null  
        return self.a / self.b  

    def jaak(self):  
        # Jääk: tagastab kahe arvu jagamisel jäägi  
        return self.a % self.b  

    def ruutjuur(self):  
        # Ruutjuur: tagastab esimese arvu ruutjuure  
        return self.a ** 0.5  # Ruutjuure arvutamiseks piisab esimesest arvust  


def menu():  
    # Kuvab valikud kasutajaliidese menüüs  
    print('''  
    1. Liitmine  
    2. Lahutamine  
    3. Korrutamine  
    4. Jagamine  
    5. Jäägi leidmine  
    6. Ruutjuure leidmine  
    0. Väljumine  
    ''')  


# Küsi kasutajalt kaks arvu  
a = int(input("Sisesta esimene number: "))  
b = int(input("Sisesta teine number: "))  

# Loo kalkulaatori objekt  
kalk = Cal(a, b)  

# Juhib menüüd, kuni kasutaja otsustab väljuda  
while True:  
    menu()  # Kuvab menüü  
    valik = int(input('Sisesta üks valikutest: '))  
    
    if valik == 1:  
        print("Vastus: ", kalk.liitmine())  # Näitab liitmise vastust  
    elif valik == 2:  
        print("Vastus: ", kalk.lahutamine())  # Näitab lahutamise vastust  
    elif valik == 3:  
        print("Vastus: ", kalk.korrutamine())  # Näitab korrutamise vastust  
    elif valik == 4:  
        print("Vastus: ", kalk.jagamine())  # Näitab jagamise vastust  
    elif valik == 5:  
        print("Vastus: ", kalk.jaak())  # Näitab jäägi leidmise vastust  
    elif valik == 6:  
        print("Vastus: ", kalk.ruutjuur())  # Näitab ruutjuure leidmise vastust  
    elif valik == 0:  
        print('Kalkulaator suletud.')  # Välju menüüst  
        break  # Lõpetab while tsükli  
    else:  
        print('Vale valik! Palun proovi uuesti.')  # Vigane valik

