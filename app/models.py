from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

db = SQLAlchemy()

# Association table for the many-to-many relationship between CarListing and Category


class CarListingCategory(db.Model):
    __tablename__ = "car_listing_category"
    car_id = db.Column(db.Integer, ForeignKey(
        "car_listings.car_id"), primary_key=True)
    cat_id = db.Column(db.Integer, ForeignKey(
        "category.cat_id"), primary_key=True)

# User model representing the users of the application


class User(db.Model):
    __tablename__ = "user_account"
    # Primary key for the user table
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)  # User's name
    email = db.Column(db.String(80), unique=True,
                      nullable=False)  # User's email, unique
    phone_number = db.Column(
        db.String(80), nullable=True)  # User's phone number
    address = db.Column(db.String(100), nullable=True)  # User's address
    password = db.Column(db.String(40), nullable=False)  # User's password

    # Relationships to other models
    car_listings = db.relationship(
        "CarListing", back_populates="owner")  # Cars listed by the user
    # Orders placed by the user
    orders = db.relationship("Order", back_populates="customer")
    garages = db.relationship(
        "Garage", back_populates="user", lazy='dynamic')  # User's garage
    contact_us = db.relationship(
        "ContactUs", back_populates="user")  # User's contact messages

# CarListing model representing individual car listings


class CarListing(db.Model):
    __tablename__ = "car_listings"
    # Primary key for the car listing
    car_id = db.Column(db.Integer, primary_key=True)
    # Foreign key to the user who listed the car
    user_id = db.Column(db.Integer, db.ForeignKey("user_account.user_id"))
    make = db.Column(db.String(20), nullable=False)  # Car's make
    model = db.Column(db.String(20), nullable=False)  # Car's model
    year = db.Column(db.Integer, nullable=False)  # Car's manufacturing year
    mileage = db.Column(db.Integer, nullable=False)  # Car's mileage
    price = db.Column(db.Float, nullable=False)  # Car's price
    description = db.Column(db.String(200), nullable=True)  # Car's description
    # URL to the car's image
    image_url = db.Column(db.String(200), nullable=False)

    # Relationships to other models
    # The owner of the car listing
    owner = db.relationship("User", back_populates="car_listings")
    categories = db.relationship("Category", secondary="car_listing_category",
                                 back_populates="car_listings")  # Categories the car belongs to
    # Garages containing this car
    garages = db.relationship("Garage", back_populates="car")

# Category model representing car categories


class Category(db.Model):
    __tablename__ = "category"
    # Primary key for the category
    cat_id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(
        db.String(20), nullable=False)  # Name of the category

    # Relationship to car listings
    car_listings = db.relationship("CarListing", secondary="car_listing_category",
                                   back_populates="categories")  # Car listings in this category

# Garage model representing a user's garage (shopping cart)


class Garage(db.Model):
    __tablename__ = 'garage'
    # Primary key for the garage
    garage_id = db.Column(db.Integer, primary_key=True)
    car_id = db.Column(db.Integer, db.ForeignKey(
        'car_listings.car_id'))  # Foreign key to the car
    user_id = db.Column(db.Integer, db.ForeignKey(
        'user_account.user_id'))  # Foreign key to the user

    # Relationships to other models
    # The car in the garage
    car = db.relationship('CarListing', back_populates='garages')
    # The owner of the garage
    user = db.relationship('User', back_populates='garages')

# Order model representing an order placed by a user


class Order(db.Model):
    __tablename__ = "orders"
    # Primary key for the order
    order_id = db.Column(db.Integer, primary_key=True)
    # Foreign key to the user who placed the order
    user_id = db.Column(db.Integer, ForeignKey("user_account.user_id"))
    # Payment method used for the order
    payment_method = db.Column(db.String(20), nullable=False)
    # Total amount of the order
    order_amount = db.Column(db.Float, nullable=False)
    # Date when the order was placed
    order_date = db.Column(db.DateTime, nullable=False)
    # Billing address for the order
    billing_address = db.Column(db.String(200), nullable=True)

    # Relationship to the user who placed the order
    # The user who placed the order
    customer = db.relationship("User", back_populates="orders")

# ContactUs model representing a contact form submission


class ContactUs(db.Model):
    __tablename__ = "contactus"
    # Primary key for the contact form submission
    contact_form_id = db.Column(db.Integer, primary_key=True)
    # Email of the person who submitted the form
    contact_email = db.Column(db.String(40), nullable=False)
    # Foreign key to the user who submitted the form
    user_id = db.Column(db.Integer, ForeignKey("user_account.user_id"))
    # Phone number of the person who submitted the form
    phone_number = db.Column(db.String(20), nullable=True)
    # Message content of the form submission
    message = db.Column(db.String(200), nullable=False)
    # Date when the form was submitted
    submission_date = db.Column(db.DateTime, nullable=False)

    # Relationship to the user who submitted the form
    # The user who submitted the contact form
    user = db.relationship("User", back_populates="contact_us")

# AboutUs model representing the content for the About Us page


class AboutUs(db.Model):
    __tablename__ = "aboutus"
    # Primary key for the About Us content
    content_id = db.Column(db.Integer, primary_key=True)
    content_title = db.Column(
        db.String(100), nullable=False)  # Title of the content
    # Text content for the About Us page
    content_text = db.Column(db.String(500), nullable=False)
