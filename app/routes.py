# The routes module contains the URL routes for the application.
# In here we define the routes for all our pages and the functions necessary to render them and pass data to them.
# Comments are added to the non-default routes to explain its operation.

from flask import current_app as app, render_template, request, flash, redirect, url_for
from .models import CarListing, Category, CarListingCategory, Garage, User
import sqlalchemy
from .helper import group_list
from . import db


@app.route('/')
@app.route('/index')
def index():
    # Fetching all car listings from the database
    car_listings = CarListing.query.all()
    # Grouping cars in groups of 3 for ease of use with the carousel
    grouped_car_listings = list(group_list(car_listings, 3))

    # Fetching all categories from the database for the Categories button row
    categories = Category.query.all()

    # Rendering the index page with the grouped car listings and categories
    return render_template('index.html', grouped_car_listings=grouped_car_listings, categories=categories)

# Route for displaying cars within a specific category


@app.route('/category/<int:category_id>')
def category_listings(category_id):
    # Fetching the specified category or returning 404 if not found
    category = Category.query.get_or_404(category_id)
    # Fetching all car listings that belong to the specified category
    car_listings = CarListing.query.join(CarListingCategory, CarListing.car_id == CarListingCategory.car_id)\
                                   .filter(CarListingCategory.cat_id == category_id).all()
    # Rendering the category listings page with the car listings in the specified category
    return render_template('category_listings.html', category=category, car_listings=car_listings)

# Route for displaying details of a specific car


@app.route('/cardetails/<int:id>', endpoint='cardetails')
def cardetails(id):
    # Fetching the specified car or returning 404 if not found
    car = CarListing.query.get_or_404(id)
    # Rendering the car details page with the details of the specified car
    return render_template('cardetails.html', car=car)

# Route for displaying all car listings with pagination


@app.route('/thelot')
def thelot():
    # Getting the page number from the request, default is 1
    page = request.args.get('page', 1, type=int)
    # Number of car listings per page
    per_page = 16
    # Fetching car listings for the specified page
    car_listings = CarListing.query.paginate(page=page, per_page=per_page)
    # Rendering the "The Lot" page with the paginated car listings
    return render_template('thelot.html', car_listings=car_listings)

# Route for displaying the About Us page


@app.route('/aboutus')
def aboutus():
    # Rendering the About Us page
    return render_template('aboutus.html')

# Route for displaying the Contact Us page


@app.route('/contactus')
def contactus():
    # Rendering the Contact Us page
    return render_template('contactus.html')

# Route for displaying the checkout page and handling the checkout process


@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    print("Checkout route accessed")  # Debugging
    user_id = 1  # Assuming a single user for simplicity
    user = User.query.get(user_id)
    garage = Garage.query.filter_by(user_id=user_id).all()
    car_ids = [g.car_id for g in garage]
    cars = CarListing.query.filter(CarListing.car_id.in_(car_ids)).all()

    total_price = sum(car.price for car in cars)

    # Rendering the checkout page with the cars in the garage and the total price
    return render_template('checkout.html', cars=cars, total_price=total_price)

# Route for displaying the user's garage


@app.route('/garage')
def garage():
    user_id = 1  # Assuming a single user for simplicity
    user = User.query.get(user_id)
    garage = Garage.query.filter_by(user_id=user_id).all()
    car_ids = [g.car_id for g in garage]
    cars = CarListing.query.filter(CarListing.car_id.in_(car_ids)).all()
    # Rendering the garage page with the cars in the user's garage and the user info
    return render_template('garage.html', cars=cars, user=user)

# Route for adding a car to the user's garage (Shopping Cart)


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
    # Redirecting to the garage page after adding the car
    return redirect(url_for('garage'))

# Route for removing a car from the user's garage


@app.route('/remove_from_garage/<int:car_id>', methods=['GET'])
def remove_from_garage(car_id):
    user_id = 1  # Assuming a single user for simplicity as we're not required to implement user authentication
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
    # Redirecting to the garage page after removing the car
    return redirect(url_for('garage'))

# Route for handling search queries


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
    # Rendering the search results page with the search query and car listings
    return render_template('search_results.html', query=query, car_listings=car_listings)
