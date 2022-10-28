class Country:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def seal1(self):
        print(self.name, self.location)

    def seal2(self):
        print(self.name, self.location, "da joylashgan")
    
country1 = Country("Uzbekistan", "Asia")
country2 = Country("Rossiya", "Evropa")

print(country1.seal1())
print(country1.seal2())

print(country2.seal1())
print(country2.seal2())



class Asia(Country):
    def __init__(self, name, location, city, population):
        super().__init__(name, location)
        self.city = city
        self.population = population

    def pechat1(self):
        print(self.name, self.location, self.city, self.population)

    def pechat2(self):
        print(self.name, self.location, "da joylashgan. Poytaxti", self.city,"va axolisi", self.population, "ga teng")

asia1 = Asia("Uzbekistan", "Osiyo", "Toshkent", "34.23 million")
asia2 = Asia("India", "Osiyo", "DEhli", "1.415 million")
asia3 = Asia("Singapur", "Osiyo","Singapur", "5.686 million")




print(asia1.pechat1())
print(asia1.pechat2())

print(asia2.pechat1())
print(asia2.pechat2())

print(asia3.pechat1())
print(asia3.pechat2())



class Evropa(Country):
    def __init__(self, name, location, city, viloyat):
        super().__init__(name, location)
        self.city = city
        self.viloyat = viloyat

    def chiqarish1(self):
        print(self.name, self.location, self.city, self.viloyat)

    def chiqarish2(self):
        print(self.name, self.location, "da joylashgan. Mashxur shahrlaridan biri bu", self.city, self.viloyat, "ga bo'lingan")

evropa1 = Evropa("Rossiya", "Evropa", "Moskva", "89 ta subyekt federatsiya")
evropa2 = Evropa("Germaniya", "Evropa", "Myunxen", "16 ta federatsiya")
evropa3 = Evropa("Avstriya", "Evropa", "Vena", "9 ta federatsiya")

print(evropa1.chiqarish1())
print(evropa1.chiqarish2())

print(evropa2.chiqarish1())
print(evropa2.chiqarish2())

print(evropa3.chiqarish1())
print(evropa3.chiqarish2())




class Amerika(Country):
    def __init__(self, name, location, city, city2):
        super().__init__(name, location)
        self.city = city
        self.city2 = city2

    def pechatat1(self):
        print(self.name, self.location, self.city, self.city2)

    def pechatat2(self):
        print(self.name, self.location, "da joylashgan. Poytaxti", self.city, "va mashxur shahrlaridan biri bu", self.city2)
        

amerika1 = Amerika("AQSH", "Amerika", "Vashington", "Nyu-york")
amerika2 = Amerika("Kanada", "Amerika", "Ottava", "Toronto")
amerika3 = Amerika("Braziliya", "Amerika", "Braziliya", "Rio-de-janeyro")

print(amerika1.pechatat1())
print(amerika1.pechatat2())

print(amerika2.pechatat1())
print(amerika2.pechatat2())

print(amerika3.pechatat1())
print(amerika3.pechatat2())