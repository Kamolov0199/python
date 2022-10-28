class Computer:
    def __init__(self, name, system):
        self.name = name
        self.system = system

    def seal1(self):
        print(self.name, self.system)

    def seal2(self):
        print(self.name, "kompyuteri", self.system, "sistemasida ishlaydi")

comp1 = Computer("Apple", "Mac")
comp2 = Computer("Acer", "Windows")

print(comp1.seal1())
print(comp1.seal2())

print(comp2.seal1())
print(comp2.seal2())



