class Animal:
    def __init__(self, name, tur):
        self.name = name
        self.tur =tur
    
    def pechat1(self):
        print(self.name, self.tur)

    def pechat2(self):
        print(self.name, "bu", self.tur, "hayvon")

animal1 = Animal("Sher", "mushuksimonlar")
animal2 = Animal("Quyon", "tovushqonlar")

print(animal1.pechat1())
print(animal1.pechat2())

print(animal2.pechat1())
print(animal2.pechat2())




class Cat(Animal):
    def __init__(self, name, tur, xarakter, color):
        super().__init__(name, tur)
        self.xarakter = xarakter
        self.color = color

    def seal1(self):
        print(self.name, self.tur, self.xarakter, self.color)

    def seal2(self):
        print(self.name, "-", self.tur, "oilasi vakili. U", self.xarakter, "xayvon va rangi", self.color, "rang")

cat1 = Cat("Yulbars", "mushuksimon", "yirtqich", "yo'l-yo'l")
cat2 = Cat("Sher", "mushuksimon", "yirtqich", "sariq")
cat3 = Cat("Mushuk", "mushuksimon", "yirtqich", "qora")



print(cat1.seal1())
print(cat1.seal2())

print(cat2.seal1())
print(cat2.seal2())

print(cat3.seal1())
print(cat3.seal2())


class Bear(Animal):
    def __init__(self, name, tur, color, live):
        super().__init__(name, tur)
        self.color = color
        self.live = live

    def chiqarish1(self):
        print(self.name, self.tur, self.color, self.live)

    def chiqarish2(self):
        print(self.name, "bu", self.tur, "oilasi vakili. Uning rangi",self.color, "va u", self.live, "da yashaydi")

bear1 = Bear("Oq ayiq", "ayiqsimonlar", "oq", "shimoliy qutb")
bear2 = Bear("Qo'ng'ir ayiq", "ayiqsimon", "qo'ng'ir", "o'rmonlar")
bear3 = Bear("Panda", "ayiqsimon", "oq-qora", "bambukzor")

print(bear1.chiqarish1())
print(bear1.chiqarish2())

print(bear2.chiqarish1())
print(bear2.chiqarish2())

print(bear3.chiqarish1())
print(bear3.chiqarish2())





class Fish(Animal):
    def __init__(self, name, tur, teri, skelet):
        super().__init__(name, tur)
        self.teri = teri
        self.skelet = skelet

    def pechatat1(self):
        print(self.name, self.tur, self.teri, self.skelet)

    def pechatat2(self):
        print(self.name, "-", self.tur, "oilasiga kiradi. Uning tashqi tuzilishi", self.teri, "bilan qoplangan.", self.skelet, "sinfiga kiradi")

fish1 = Fish("Akula", "baliqsimon", "teri", "tog'aylilar")
fish2 = Fish("Losos", "baliqsimon", "tangali", "suyaklilar")
fish3 = Fish("Karp", "baliqsimon", "tangali", "suyaklilar")

print(fish1.pechatat1())
print(fish1.pechatat2())

print(fish2.pechatat1())
print(fish2.pechatat2())

print(fish3.pechatat1())
print(fish3.pechatat2())
