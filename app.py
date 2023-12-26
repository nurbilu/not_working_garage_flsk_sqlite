from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import sqlite3


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cars.db'
db = SQLAlchemy(app)

# Define the 'Car' model
class Car(db.Model):
    __tablename__ = 'cars'  # Explicitly specify the table name
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column('model', db.String(50), nullable=False)
    year = db.Column('year', db.Integer, nullable=False)
    color = db.Column('color', db.String(50), nullable=False)
    
    

# Create the database tables
with app.app_context():
    conn = sqlite3.connect('cars.db')
# Create a cursor object to execute SQL commands
cursor = conn.cursor()
# Create a table named 'cars' with columns: model, year, color
cursor.execute('''
    CREATE TABLE IF NOT EXISTS cars (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        model TEXT NOT NULL,
        year INTEGER NOT NULL,
        color TEXT NOT NULL
    )
''')


# Route to display cars from db
@app.route('/', methods=["GET"])
def display_cars():
    # Implement logic to fetch and display cars from the database
    cars = Car.query.all()
    return render_template('cars.html', cars=cars)

# Route to add a new car to db
@app.route('/add', methods=["GET", "POST"])
def add():
    if request.method == "POST":
        # Get form data
        model = request.form['model']
        year = request.form['year']
        color = request.form['color']

        # Create a new car object and add it to the database
        new_car = Car(model=model, year=year, color=color)
        db.session.add(new_car)
        db.session.commit()

        return redirect(url_for('display_cars'))

    return render_template('add.html')

# Route to delete a car from db
@app.route('/delete/<int:car_id>', methods=["GET", "POST"])
def delete(car_id):
    # Implement logic to delete a car from the database
    car = Car.query.get(car_id)
    if car:
        db.session.delete(car)
        db.session.commit()

    return redirect(url_for('display_cars'))

# Route to update a car from db
@app.route('/updt/<int:car_id>', methods=["GET", "POST"])
def updt(car_id):
    # Implement logic to update a car in the database
    car = Car.query.get(car_id)

    if request.method == "POST":
        # Update car details
        car.model = request.form['model']
        car.year = request.form['year']
        car.color = request.form['color']

        # Commit changes to the database
        db.session.commit()

        return redirect(url_for('display_cars'))

    return render_template('updt.html', car=car)

if __name__ == '__main__':
    app.run(debug=True)
