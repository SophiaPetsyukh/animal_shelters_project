import petpy
from pet_class import Pet
from multiset_class import Array
import folium
from geopy.geocoders import ArcGIS
from hidden import give_key
import branca


def get_pets(loc, anm, age, sex, br, am):
    '''
    :param loc: str
    :param anm: str
    :param age: str
    :param sex: str
    :param br: str
    :param am: str
    :return: array

    This function finds the appropriate pets for the user and puts them into the array
    '''
    pf = petpy.Petfinder(give_key())
    available = Array(int(am))
    if loc == '-':
        loc = 'NY'
    if anm == '-':
        anm = None
    if br == '-':
        br = None
    if age == '-':
        age = None
    if sex == '-':
        sex = None
    if am == '-':
        am = 5
    pets_dict = pf.pet_find(loc, anm, br, None, sex, age, count=am)
    if len(pets_dict['petfinder']['header']['status']['message']) != 0:
        return None
    i = 0
    for a in pets_dict['petfinder']['pets']['pet']:
        available[i] = Pet(a['id']['$t'])
        i+=1
    return available

def help_html(address, animal, breed, sex, age, name, photo, shelter, description):
    '''
    :param address: str
    :param animal: str
    :param breed: str
    :param sex: str
    :param age: str
    :param name: str
    :param photo: str
    :param shelter: str
    :param description: str
    :return: str

    This function creates a table in html format for the popup on the map
    '''
    left_col_colour = "#2A799C"
    right_col_colour = "#C5DCE7"

    html = """<!DOCTYPE html>
    <html>

    <head>
    <h4 style="margin-bottom:0"; width="300px">{}</h4>""".format(address) + """

    </head>
        <table style="height: 126px; width: 300px;">
    <tbody>
    <tr>
    <td style="background-color: """ + left_col_colour + """;"><span style="color: #ffffff;">Animal</span></td>
    <td style="width: 200px;background-color: """ + right_col_colour + """;">{}</td>""".format(animal) + """
    </tr>
    <tr>
    <td style="background-color: """ + left_col_colour + """;"><span style="color: #ffffff;">Breed</span></td>
    <td style="width: 200px;background-color: """ + right_col_colour + """;">{}</td>""".format(breed) + """
    </tr>
    <tr>
    <td style="background-color: """ + left_col_colour + """;"><span style="color: #ffffff;">Sex</span></td>
    <td style="width: 200px;background-color: """ + right_col_colour + """;">{}</td>""".format(sex) + """
    </tr>
    <tr>
    <td style="background-color: """ + left_col_colour + """;"><span style="color: #ffffff;">Age</span></td>
    <td style="width: 200px;background-color: """ + right_col_colour + """;">{}</td>""".format(age) + """
    </tr>
    <tr>
    <td style="background-color: """ + left_col_colour + """;"><span style="color: #ffffff;">Name</span></td>
    <td style="width: 200px;background-color: """ + right_col_colour + """;">{}</td>""".format(name) + """
    </tr>
    <tr>
    <td style="background-color: """ + left_col_colour + """;"><span style="color: #ffffff;">Description</span></td>
    <td style="width: 200px;background-color: """ + right_col_colour + """;">{}</td>""".format(
        description) + """
    </tr>
    <tr>
    <td style="background-color: """ + left_col_colour + """;"><span style="color: #ffffff;">Photo</span></td>
    <td style="width: 200px;background-color: """ + right_col_colour + """;">{}</td>""".format(
        photo) + """
    </tr>
    <tr>
    <td style="background-color: """ + left_col_colour + """;"><span style="color: #ffffff;">Contacts</span></td>
    <td style="width: 200px;background-color: """ + right_col_colour + """;">{}</td>""".format(
        shelter) + """
    </tr>
    </tbody>
    </table>
    </html>
    """
    return html


def result_map(available):
    '''

    :param available: array
    :return: NoneType

    This function creates the result map
    '''
    geolocator = ArcGIS(timeout=10)
    sheltersMap = folium.Map()
    fg = folium.FeatureGroup(name='shelters')
    for a in available:
        loc = geolocator.geocode(a.shelter_info())
        html = help_html(a.shelter_info(), a.get_type(), a.get_breed(), a.get_sex(), a.get_age(), a.get_name(), a.photo_link(), a.shelter_link(), a.to_str())
        iframe = branca.element.IFrame(html=html, width=600, height=300)
        popup = folium.Popup(iframe, parse_html=True)
        fg.add_child(folium.Marker(location=[loc.latitude, loc.longitude], popup=popup, icon=folium.Icon()))
    sheltersMap.add_child(fg)
    sheltersMap.save('templates/SheltersMap.html')