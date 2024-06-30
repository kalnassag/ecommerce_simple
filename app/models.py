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


class User(db.Model):
    __tablename__ = "user_account"
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    phone_number = db.Column(db.String(80), nullable=True)
    address = db.Column(db.String(100), nullable=True)
    password = db.Column(db.String(40), nullable=False)

    car_listings = db.relationship("CarListing", back_populates="owner")
    orders = db.relationship("Order", back_populates="customer")
    garages = db.relationship("Garage", back_populates="user", lazy='dynamic')
    contact_us = db.relationship("ContactUs", back_populates="user")


class CarListing(db.Model):
    __tablename__ = "car_listings"
    car_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user_account.user_id"))
    make = db.Column(db.String(20), nullable=False)
    model = db.Column(db.String(20), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    mileage = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(200), nullable=True)
    image_url = db.Column(db.String(200), nullable=False)

    owner = db.relationship("User", back_populates="car_listings")
    categories = db.relationship(
        "Category", secondary="car_listing_category", back_populates="car_listings")
    garages = db.relationship("Garage", back_populates="car")


class Category(db.Model):
    __tablename__ = "category"
    cat_id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(20), nullable=False)

    car_listings = db.relationship(
        "CarListing", secondary="car_listing_category", back_populates="categories")


class Garage(db.Model):
    __tablename__ = 'garage'
    garage_id = db.Column(db.Integer, primary_key=True)
    car_id = db.Column(db.Integer, db.ForeignKey('car_listings.car_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user_account.user_id'))

    car = db.relationship('CarListing', back_populates='garages')
    user = db.relationship('User', back_populates='garages')


class Order(db.Model):
    __tablename__ = "orders"
    order_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey("user_account.user_id"))
    payment_method = db.Column(db.String(20), nullable=False)
    order_amount = db.Column(db.Float, nullable=False)
    order_date = db.Column(db.DateTime, nullable=False)
    billing_address = db.Column(db.String(200), nullable=True)

    customer = db.relationship("User", back_populates="orders")


class ContactUs(db.Model):
    __tablename__ = "contactus"
    contact_form_id = db.Column(db.Integer, primary_key=True)
    contact_email = db.Column(db.String(40), nullable=False)
    user_id = db.Column(db.Integer, ForeignKey("user_account.user_id"))
    phone_number = db.Column(db.String(20), nullable=True)
    message = db.Column(db.String(200), nullable=False)
    submission_date = db.Column(db.DateTime, nullable=False)

    user = db.relationship("User", back_populates="contact_us")


class AboutUs(db.Model):
    __tablename__ = "aboutus"
    content_id = db.Column(db.Integer, primary_key=True)
    content_title = db.Column(db.String(100), nullable=False)
    content_text = db.Column(db.String(500), nullable=False)
