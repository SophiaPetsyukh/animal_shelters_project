import petpy
from hidden import give_key


class Pet:
    """
    Class for pet representation
    """
    def __init__(self, pet_id):
        """
        :param pet_id: str

        Initialize pet's id and information about the pet
        """
        self.pet_id = pet_id
        pf = petpy.Petfinder(give_key())
        self.info = pf.pet_get(pet_id)

    def get_type(self):
        """
        :return: str

        Returns type of animal
        """
        return self.info['petfinder']['pet']['animal']['$t']

    def get_sex(self):
        """
        :return: str

        Returns sex of the pet
        """
        return self.info['petfinder']['pet']['sex']['$t']

    def get_breed(self):
        """
        :return: str

        Returns the breed of the pet
        """
        return self.info['petfinder']['pet']['breeds']['breed']['$t']

    def get_name(self):
        """
        :return: str

        Returns the name of the pet
        """
        return self.info['petfinder']['pet']['name']['$t']

    def get_age(self):
        """
        :return: str

        Returns the age of the pet
        """
        return self.info['petfinder']['pet']['age']['$t']

    def get_description(self):
        """
        :return: str

        Returns the decription of the pet
        """
        descr = self.info['petfinder']['pet']['description']
        if len(descr) == 0:
            return None
        return descr['$t']

    def photo_link(self):
        """
        :return: str

        Returns the photo link
        """
        photo = self.info['petfinder']['pet']['media']
        if len(photo)==0:
            return 'No photos attached'
        return photo['photos']['photo'][0]['$t']

    def shelter_link(self):
        """
        :return: str

        Returns shelter's contact information
        """
        email = self.info['petfinder']['pet']['contact']['email']
        if len(email) == 0:
            phone = self.info['petfinder']['pet']['contact']['phone']
            if len(phone) == 0:
                return 'No contact information'
            return phone['$t']
        return email['$t']


    def to_str(self):
        """
        :return: str

        Returns string representation of the pet
        """
        if self.get_description() == None:
            result = "This {}'s name is {}. It's breed is {} and the pet is {}".format(self.get_type(), self.get_name(), self.get_breed(), self.get_age())
            return result
        return self.get_description()

    def shelter_info(self):
        """
        :return: str

        Returns shelter location
        """
        address1 = self.info['petfinder']['pet']['contact']['address1']
        address2 = self.info['petfinder']['pet']['contact']['address2']
        city = self.info['petfinder']['pet']['contact']['city']['$t']
        if len(address1) != 0:
            return address1['$t'] + ', ' + city
        if len(address2) != 0:
            return address2['$t'] + ', ' + city
        return city
