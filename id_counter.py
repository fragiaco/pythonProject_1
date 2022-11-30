

class Dog:
    specie='Canis Lupus'
    id_dog_counter =1


    def __init__(self, name):
        self._id = Dog.id_dog_counter
        self.n = name
        Dog.id_dog_counter+=1

    def get_id(self):
        return self._id

print(Dog.id_dog_counter)

D1=Dog('io')
print(D1.n)
print(D1.get_id())

D2=Dog('tu')
print(D2.n)
print(D2.get_id())