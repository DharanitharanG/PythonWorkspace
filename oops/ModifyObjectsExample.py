class ModifyObjects:
    name = "Dharani"
    age = 26

    def __init__(self, location):
        self.location = location


m = ModifyObjects("Chennai")
print(m.location)
m.location = 'Pune'
print(m.location)
# del m.location
# print(m.location)

del m
print(m.location)
