from flask import current_app as app, render_template, jsonify, request, flash, redirect, url_for
from .models import CarListing, Category, CarListingCategory, Garage, User
import sqlalchemy
from .helper import group_list
from . import db


@app.route('/')
@app.route('/index')
def index():
    car_listings = CarListing.query.all()
    # Grouping cars in groups of 3 for ease of use with the carousel
    grouped_car_listings = list(group_list(car_listings, 3))
    categories = Category.query.all()
    return render_template('index.html', grouped_car_listings=grouped_car_listings, categories=categories)


@app.route('/category/<int:category_id>')
def category_listings(category_id):
    category = Category.query.get_or_404(category_id)
    car_listings = CarListing.query.join(CarListingCategory, CarListing.car_id == CarListingCategory.car_id)\
                                   .filter(CarListingCategory.cat_id == category_id).all()
    return render_template('category_listings.html', category=category, car_listings=car_listings)


@app.route('/cardetails/<int:id>', endpoint='cardetails')
def cardetails(id):
    car = CarListing.query.get_or_404(id)
    return render_template('cardetails.html', car=car)


@app.route('/thelot')
def thelot():
    page = request.args.get('page', 1, type=int)
    per_page = 16
    car_listings = CarListing.query.paginate(page=page, per_page=per_page)
    return render_template('thelot.html', car_listings=car_listings)


@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')


@app.route('/contactus')
def contactus():
    return render_template('contactus.html')


@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    print("checkout route accessed")  # Debugging
    user_id = 1  # Assuming a single user for simplicity
    user = User.query.get(user_id)
    garage = Garage.query.filter_by(user_id=user_id).all()
    car_ids = [g.car_id for g in garage]
    cars = CarListing.query.filter(CarListing.car_id.in_(car_ids)).all()

    total_price = sum(car.price for car in cars)

    return render_template('checkout.html', cars=cars, total_price=total_price)


@app.route('/garage')
def garage():
    user_id = 1  # Assuming a single user for simplicity
    user = User.query.get(user_id)
    garage = Garage.query.filter_by(user_id=user_id).all()
    car_ids = [g.car_id for g in garage]
    cars = CarListing.query.filter(CarListing.car_id.in_(car_ids)).all()
    return render_template('garage.html', cars=cars, user=user)


@app.route('/add_to_garage/<int:car_id>', methods=['GET'])
def add_to_garage(car_id):
    user_id = 1  # Assuming a single user for simplicity
    user = User.query.get(user_id)
    try:
        # Check if the car is already in the garage
        if not Garage.query.filter_by(user_id=user_id, car_id=car_id).first():
            garage_entry = Garage(car_id=car_id, user_id=user_id)
            db.session.add(garage_entry)
            db.session.commit()
            flash('Car added to the garage successfully.')
    except sqlalchemy.exc.OperationalError as e:
        if 'database is locked' in str(e):
            flash('Database is currently busy. Please try again.')
        else:
            flash('An error occurred while adding the car to the garage.')
    return redirect(url_for('garage'))


@app.route('/remove_from_garage/<int:car_id>', methods=['GET'])
def remove_from_garage(car_id):
    user_id = 1  # Assuming a single user for simplicity
    try:
        garage_entry = Garage.query.filter_by(
            user_id=user_id, car_id=car_id).first()
        if garage_entry:
            db.session.delete(garage_entry)
            db.session.commit()
            flash('Car removed from the garage successfully.')
        else:
            flash('Car not found in the garage.')
    except sqlalchemy.exc.OperationalError as e:
        if 'database is locked' in str(e):
            flash('Database is currently busy. Please try again.')
        else:
            flash('An error occurred while removing the car from the garage.')
    return redirect(url_for('garage'))


@app.route('/search')
def search():
    query = request.args.get('query', '')
    if query:
        search_term = f"%{query}%"
        car_listings = CarListing.query.filter(
            CarListing.make.ilike(search_term) |
            CarListing.model.ilike(search_term) |
            CarListing.description.ilike(search_term)
        ).all()
    else:
        car_listings = []
    return render_template('search_results.html', query=query, car_listings=car_listings)
