import petpy
from hidden import give_key

key = give_key()

def try_petpy(key):
    pf = petpy.Petfinder(key)
    #get info about cat breeds
    cats = pf.breed_list('cat')
    #get info about available dogs in New York, setting count=1 to see
    #complection of json dictionary
    pets = pf.pet_find('New York', 'cat', count=1)
    #print(pets)
    #get shelters info
    wa_shelter = pf.shelter_list_by_breed('dog', 'Dalamatine')
    return wa_shelter

print(try_petpy(key))

