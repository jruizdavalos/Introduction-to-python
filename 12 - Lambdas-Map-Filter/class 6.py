names=["John Doe","Alice Smith","Bob Ford","Jake Lee"]

for name in names:
    print(name.split())
    print(name.split()[0])
    print("\t",name.split()[1])
    print(name.split()[0][0]+"."+name.split()[1][0])



l=list(map(lambda name: name, names))

print(l)


p=list(map(lambda name:"".join([n[0] for n in name.split()]), names))

print(p)

