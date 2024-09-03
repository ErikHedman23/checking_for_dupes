def remove_duplicates(dogs):
    new_dogs = set()
    for dog in dogs:
        new_dogs.add(dog)
    new_dogs_list = []
    for dog in new_dogs:
        new_dogs_list.append(dog)
    return new_dogs_list