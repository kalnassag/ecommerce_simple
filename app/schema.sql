-- Create table for the User model
CREATE TABLE user_account (
    user_id INTEGER PRIMARY KEY,
    name VARCHAR(80) NOT NULL,
    email VARCHAR(80) UNIQUE NOT NULL,
    phone_number VARCHAR(80),
    address VARCHAR(100),
    password VARCHAR(255) NOT NULL
);

-- Create table for the CarListing model
CREATE TABLE car_listings (
    car_id INTEGER PRIMARY KEY,
    user_id INTEGER,
    make VARCHAR(20) NOT NULL,
    model VARCHAR(20) NOT NULL,
    year INTEGER NOT NULL,
    mileage INTEGER NOT NULL,
    price REAL NOT NULL,
    description VARCHAR(500),
    features VARCHAR(200),
    pictures VARCHAR(100),
    FOREIGN KEY(user_id) REFERENCES user_account(user_id)
);

-- Create table for the Category model
CREATE TABLE category (
    cat_id INTEGER PRIMARY KEY,
    category_name VARCHAR(20) NOT NULL
);

-- Create association table for many-to-many relationship between CarListing and Category
CREATE TABLE car_listing_category (
    car_id INTEGER,
    cat_id INTEGER,
    PRIMARY KEY (car_id, cat_id),
    FOREIGN KEY(car_id) REFERENCES car_listings(car_id),
    FOREIGN KEY(cat_id) REFERENCES category(cat_id)
);

-- Create table for the Garage model
CREATE TABLE garage (
    garage_id INTEGER PRIMARY KEY,
    user_id INTEGER,
    FOREIGN KEY(user_id) REFERENCES user_account(user_id)
);

-- Create table for the Order model
CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    user_id INTEGER,
    payment_method VARCHAR(20) NOT NULL,
    order_amount REAL NOT NULL,
    order_date DATETIME NOT NULL,
    billing_address VARCHAR(200),
    FOREIGN KEY(user_id) REFERENCES user_account(user_id)
);

-- Create table for the ContactUs model
CREATE TABLE contactus (
    contact_form_id INTEGER PRIMARY KEY,
    contact_email VARCHAR(40) NOT NULL,
    user_id INTEGER,
    phone_number VARCHAR(20),
    message VARCHAR(200) NOT NULL,
    submission_date DATETIME NOT NULL,
    FOREIGN KEY(user_id) REFERENCES user_account(user_id)
);

-- Create table for the AboutUs model
CREATE TABLE aboutus (
    content_id INTEGER PRIMARY KEY,
    content_title VARCHAR(100) NOT NULL,
    content_text VARCHAR(500) NOT NULL
);