# animal_shelters_project

This project is aimed to create a search system for finding animals available for adoption in different shelters. It will take the user's likings into consideration and display the available shelters on a map of a given by user region. For more specific information see wiki.

Information about adoptable pets will be taken from the petfinder.com API, which allows to access their database of different shelters by providing an API key. If you want to get yours, please go to https://www.petfinder.com/developers/api-key.

User needs to provide these kind of parameters:
-location;
-animal;
-breed;
-sex;
-age;
-amount of results.

![Знімок екрана (9)](https://user-images.githubusercontent.com/47388433/57974703-61552900-79c5-11e9-92ed-6ff7d0f67cbb.png)

After providing the right kind of information user can see a map with markers, which show the location of shelters that can provide the user with their wanted pet.
For more information on the pet, user needs to click on the marker.

![Знімок екрана (7)](https://user-images.githubusercontent.com/47388433/57974738-d4f73600-79c5-11e9-8086-ec8101b1b049.png)


If some of the information was invalid, user will get a message about it and will have to restart the program.

![Знімок екрана (8)](https://user-images.githubusercontent.com/47388433/57974727-c3ae2980-79c5-11e9-8fa6-092bc4427b40.png)


Program structure:
-The main module is called main.py
-The classes, which I am using are in modules named pet_class.py and multiset_class.py. These modules are tested in test_classes.py
-All the additional functions are in module named create_map.py
-The html files, which I am using are in the folder called templates

To use the petfinder program without downloading the whole package you can go to sofiykapet.pythonanywhere.com
