from flask import Flask, render_template, request
from create_map import get_pets, result_map

app = Flask(__name__)

@app.route('/')
def input_page():
    '''
    (None) -> html
    This function returns an html page
    '''
    return render_template('index.html')

@app.route('/SheltersMap', methods=['POST'])
def animal_map():
    '''
    (None) -> html
    This function returns an html page
    '''
    animal = request.form['Animal']
    age = request.form['Age']
    sex = request.form['Sex']
    breed = request.form['Breed']
    location = request.form['Location']
    amount = request.form['Amount']
    available_animals = get_pets(location, animal, age, sex, breed, amount)
    if available_animals == None:
        return render_template('failure.html')
    result_map(available_animals)
    return render_template("SheltersMap.html")

if __name__ == '__main__':
    app.run(debug=True)