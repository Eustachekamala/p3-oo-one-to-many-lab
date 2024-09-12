class Owner:
    def __init__(self, name):
        self.name = name
    ## TODO: Implement this method to return a list of pets owned by this owner.
    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
    
    ## TODO: Implement the add_pet method to add a pet to the owner's pets.
    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise TypeError("Only instances of Pet can be added.")
        if pet.owner is None:
            pet.owner = self
        else:
            raise ValueError("This pet already has an owner.")
        
    ## TODO: Implement the get_sorted_pets method to return a list of pets sorted by name.
    def get_sorted_pets(self):
        ## To sort the pets by name, we use the sorted() function and pass it a list of pets and a key function that specifies how to sort each pet. The key function is a lambda function that takes a pet as an argument and returns the name of the pet.
        return sorted(self.pets(), key=lambda pet: pet.name)


class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []
    
    ## TODO: Implement the __init__ method to initialize a new pet.
    def __init__(self, name, pet_type, owner=None):
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet_type. Must be one of {Pet.PET_TYPES}.")
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)

    
        