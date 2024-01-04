zoo = list()
select = None
print("Ez egy állatkert.")
print("Állat hozzáadása (1) - elvétele (2) kilépés (0)")

while select != "0":
    select = input("Mit szeretne tenni?")
    if select !="0":
        if select == "1":
            animal = dict()
            name = input("Az állat neve: ")
            if name not in animal.keys():
                animal[name] = 1
            else:
                animal[name] += 1
            zoo.append(animal)

print("Az állatkertben lévő állatok nevei:")
for animal in zoo:
    for name, count in animal.items():
        print(f"{name} ({count} db)")