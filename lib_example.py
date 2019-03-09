import hidden
import folium
from flask import Flask, render_template
import petpy

key = hidden.give_key()
pf = petpy.Petfinder(key)
data = pf.shelter_get('WA149')
latitude = float(data['petfinder']['shelter']['latitude']['$t'])
longitude = float(data['petfinder']['shelter']['longitude']['$t'])


m = folium.Map()
fg = folium.FeatureGroup(name='shelter_location')
fg.add_child(folium.Marker(location=[latitude, longitude], popup='WA shelter', icon=folium.Icon()))
m.add_child(fg)
m.save('templates/map.html')

app = Flask(__name__)
@app.route('/')
def make_map():
    return render_template('map.html')

if __name__=='__main__':
    app.run(debug=True)
