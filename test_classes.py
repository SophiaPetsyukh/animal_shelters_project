from pet_class import Pet
from multiset_class import Array
import unittest

class TestPetClass(unittest.TestCase):
    def setUp(self):
        self.p1 = Pet('44727732')

    def test_init(self):
        self.assertTrue(self.p1.pet_id == '44727732')

    def test_get_type(self):
        self.assertTrue(self.p1.get_type() == 'Cat')

    def test_get_sex(self):
        self.assertTrue(self.p1.get_sex() == 'F')

    def test_get_breed(self):
        self.assertTrue(self.p1.get_breed() == 'Domestic Short Hair')

    def test_get_name(self):
        self.assertTrue(self.p1.get_name() == 'SKY')

    def test_get_age(self):
        self.assertTrue(self.p1.get_age() == 'Young')

    def test_get_description(self):
        self.assertFalse(self.p1.get_description() == None)

    def test_photo_link(self):
        self.assertFalse(self.p1.photo_link() == 'No photos attached')

    def test_shelter_link(self):
        self.assertTrue(self.p1.shelter_link() == '253-383-2733')

    def test_shelter_info(self):
        self.assertTrue(self.p1.shelter_info() == '2608 Center Street, Tacoma')


class TestArray(unittest.TestCase):
    def setUp(self):
        self.a1 = Array(5)
        self.a1[0] = 1
        self.a1[1] = 2

    def test_init(self):
        self.assertTrue(type(self.a1) == Array)

    def test_setitem(self):
        self.assertTrue(self.a1[0] == 1)

    def test_getitem(self):
        self.assertTrue(self.a1[1] == 2)

    def test_clear(self):
        self.a1.clear(0)
        self.assertTrue(self.a1[0] == 0)

if __name__ == '__main__':
    unittest.main()