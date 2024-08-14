class House:
    def __init__(self, numberOfFloors, buildingType):
        self.numberOfFloors = numberOfFloors
        self.buildingType = buildingType

    def __eq__(self, other):
        return isinstance(other, House) and self.buildingType == other.buildingType \
            and self.numberOfFloors == other.numberOfFloors


h1 = House('ЖК Горский', 10)
h2 = House('Домик в деревне', 10)
print(h1 == h2)