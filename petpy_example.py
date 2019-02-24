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
    wa_shelter = pf.shelter_find(location='WA', count=1)
    return wa_shelter

