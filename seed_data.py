from app import db, create_app
from app.models import User, CarListing, Category, Garage, CarListingCategory

app = create_app()
app.app_context().push()

# Adding sample users
user1 = User(name="John Doe", email="john@example.com", password="password")
user2 = User(name="Jane Smith", email="jane@example.com", password="password")

db.session.add(user1)
db.session.add(user2)
db.session.commit()

# Adding sample categories
categories = [
    Category(category_name="SUV"),
    Category(category_name="Sedan"),
    Category(category_name="Truck"),
    Category(category_name="Coupe"),
    Category(category_name="Convertible")
]

db.session.add_all(categories)
db.session.commit()

# Adding sample car listings
car_listings = [
    CarListing(make="Toyota", model="Camry", year=2020, mileage=15000, price=20000,
               description="A reliable car", image_url="static/IMG/toyota_camry.jpg", user_id=user1.user_id),
    CarListing(make="Honda", model="Civic", year=2019, mileage=20000, price=18000,
               description="A compact car", image_url="static/IMG/honda_civic.jpg", user_id=user1.user_id),
    CarListing(make="Ford", model="F-150", year=2021, mileage=10000, price=30000,
               description="A powerful truck", image_url="static/IMG/ford_f150.jpg", user_id=user2.user_id),
    CarListing(make="Chevrolet", model="Malibu", year=2018, mileage=25000, price=15000,
               description="A mid-size sedan", image_url="static/IMG/chevrolet_malibu.jpg", user_id=user2.user_id),
    CarListing(make="BMW", model="3 Series", year=2020, mileage=5000, price=35000,
               description="A luxury sedan", image_url="static/IMG/bmw_3_series.jpg", user_id=user1.user_id),
    CarListing(make="Audi", model="A4", year=2020, mileage=8000, price=32000,
               description="A luxury compact car", image_url="static/IMG/audi_a4.jpg", user_id=user2.user_id),
    CarListing(make="Mercedes-Benz", model="C-Class", year=2019, mileage=12000, price=34000,
               description="A luxury car", image_url="static/IMG/mercedes_c_class.jpg", user_id=user1.user_id),
    CarListing(make="Tesla", model="Model S", year=2021, mileage=5000, price=70000,
               description="An electric car", image_url="static/IMG/tesla_model_s.jpg", user_id=user2.user_id),
    CarListing(make="Hyundai", model="Elantra", year=2018, mileage=30000, price=15000,
               description="A compact car", image_url="static/IMG/hyundai_elantra.jpg", user_id=user1.user_id),
    CarListing(make="Nissan", model="Altima", year=2019, mileage=25000, price=18000,
               description="A mid-size car", image_url="static/IMG/nissan_altima.jpg", user_id=user2.user_id),
    CarListing(make="Kia", model="Optima", year=2018, mileage=20000, price=17000,
               description="A mid-size sedan", image_url="static/IMG/kia_optima.jpg", user_id=user1.user_id),
    CarListing(make="Mazda", model="CX-5", year=2021, mileage=10000, price=28000,
               description="A compact SUV", image_url="static/IMG/mazda_cx5.jpg", user_id=user2.user_id),
    CarListing(make="Subaru", model="Outback", year=2020, mileage=15000, price=27000,
               description="A mid-size SUV", image_url="static/IMG/subaru_outback.jpg", user_id=user1.user_id),
    CarListing(make="Volkswagen", model="Passat", year=2019, mileage=22000, price=20000,
               description="A mid-size car", image_url="static/IMG/vw_passat.jpg", user_id=user2.user_id),
    CarListing(make="Volvo", model="XC90", year=2021, mileage=5000, price=50000,
               description="A luxury SUV", image_url="static/IMG/volvo_xc90.jpg", user_id=user1.user_id),
    CarListing(make="Chevrolet", model="Tahoe", year=2019, mileage=18000, price=40000,
               description="A full-size SUV", image_url="static/IMG/chevrolet_tahoe.jpg", user_id=user2.user_id),
    CarListing(make="GMC", model="Sierra", year=2020, mileage=12000, price=45000,
               description="A full-size truck", image_url="static/IMG/gmc_sierra.jpg", user_id=user1.user_id),
    CarListing(make="Dodge", model="Charger", year=2019, mileage=16000, price=30000,
               description="A full-size sedan", image_url="static/IMG/dodge_charger.jpg", user_id=user2.user_id),
    CarListing(make="Lexus", model="RX", year=2021, mileage=8000, price=45000,
               description="A luxury SUV", image_url="static/IMG/lexus_rx.jpg", user_id=user1.user_id),
    CarListing(make="Infiniti", model="QX60", year=2020, mileage=15000, price=40000,
               description="A luxury mid-size SUV", image_url="static/IMG/infiniti_qx60.jpg", user_id=user2.user_id),
    CarListing(make="Jaguar", model="F-Pace", year=2019, mileage=10000, price=55000,
               description="A luxury compact SUV", image_url="static/IMG/jaguar_fpace.jpg", user_id=user1.user_id),
    CarListing(make="Land Rover", model="Range Rover", year=2020, mileage=12000, price=90000,
               description="A luxury full-size SUV", image_url="static/IMG/land_rover_range_rover.jpg", user_id=user2.user_id),
    CarListing(make="Porsche", model="Macan", year=2021, mileage=5000, price=60000,
               description="A luxury compact SUV", image_url="static/IMG/porsche_macan.jpg", user_id=user1.user_id),
    CarListing(make="Cadillac", model="Escalade", year=2019, mileage=15000, price=75000,
               description="A luxury full-size SUV", image_url="static/IMG/cadillac_escalade.jpg", user_id=user2.user_id),
    CarListing(make="Lincoln", model="Navigator", year=2020, mileage=8000, price=85000,
               description="A luxury full-size SUV", image_url="static/IMG/lincoln_navigator.jpg", user_id=user1.user_id),
    CarListing(make="Alfa Romeo", model="Stelvio", year=2019, mileage=10000, price=45000,
               description="A luxury compact SUV", image_url="static/IMG/alfa_romeo_stelvio.jpg", user_id=user2.user_id),
    CarListing(make="Acura", model="MDX", year=2021, mileage=5000, price=48000,
               description="A luxury mid-size SUV", image_url="static/IMG/acura_mdx.jpg", user_id=user1.user_id),
    CarListing(make="Tesla", model="Model 3", year=2020, mileage=8000, price=50000,
               description="An electric compact car", image_url="static/IMG/tesla_model_3.jpg", user_id=user2.user_id),
    CarListing(make="Ferrari", model="488", year=2019, mileage=3000, price=250000,
               description="A luxury sports car", image_url="static/IMG/ferrari_488.jpg", user_id=user1.user_id),
    CarListing(make="Lamborghini", model="Huracan", year=2021, mileage=2000, price=300000,
               description="A luxury sports car", image_url="static/IMG/lamborghini_huracan.jpg", user_id=user2.user_id)
]

db.session.add_all(car_listings)
db.session.commit()

# Assign cars to categories
car_categories = [
    # Toyota Camry -> SUV
    CarListingCategory(car_id=car_listings[0].car_id, cat_id=1),
    # Honda Civic -> Sedan
    CarListingCategory(car_id=car_listings[1].car_id, cat_id=2),
    # Ford F-150 -> Truck
    CarListingCategory(car_id=car_listings[2].car_id, cat_id=3),
    # Chevrolet Malibu -> Sedan
    CarListingCategory(car_id=car_listings[3].car_id, cat_id=2),
    # BMW 3 Series -> Coupe
    CarListingCategory(car_id=car_listings[4].car_id, cat_id=4),
    # Audi A4 -> Sedan
    CarListingCategory(car_id=car_listings[5].car_id, cat_id=2),
    # Mercedes-Benz C-Class -> Sedan
    CarListingCategory(car_id=car_listings[6].car_id, cat_id=2),
    # Tesla Model S -> Sedan
    CarListingCategory(car_id=car_listings[7].car_id, cat_id=2),
    # Hyundai Elantra -> Sedan
    CarListingCategory(car_id=car_listings[8].car_id, cat_id=2),
    # Nissan Altima -> Sedan
    CarListingCategory(car_id=car_listings[9].car_id, cat_id=2),
    # Kia Optima -> Sedan
    CarListingCategory(car_id=car_listings[10].car_id, cat_id=2),
    # Mazda CX-5 -> SUV
    CarListingCategory(car_id=car_listings[11].car_id, cat_id=1),
    # Subaru Outback -> SUV
    CarListingCategory(car_id=car_listings[12].car_id, cat_id=1),
    # Volkswagen Passat -> Sedan
    CarListingCategory(car_id=car_listings[13].car_id, cat_id=2),
    # Volvo XC90 -> SUV
    CarListingCategory(car_id=car_listings[14].car_id, cat_id=1),
    # Chevrolet Tahoe -> SUV
    CarListingCategory(car_id=car_listings[15].car_id, cat_id=1),
    # GMC Sierra -> Truck
    CarListingCategory(car_id=car_listings[16].car_id, cat_id=3),
    # Dodge Charger -> Sedan
    CarListingCategory(car_id=car_listings[17].car_id, cat_id=2),
    # Lexus RX -> SUV
    CarListingCategory(car_id=car_listings[18].car_id, cat_id=1),
    # Infiniti QX60 -> SUV
    CarListingCategory(car_id=car_listings[19].car_id, cat_id=1),
    # Jaguar F-Pace -> SUV
    CarListingCategory(car_id=car_listings[20].car_id, cat_id=1),
    # Land Rover Range Rover -> SUV
    CarListingCategory(car_id=car_listings[21].car_id, cat_id=1),
    # Porsche Macan -> SUV
    CarListingCategory(car_id=car_listings[22].car_id, cat_id=1),
    # Cadillac Escalade -> SUV
    CarListingCategory(car_id=car_listings[23].car_id, cat_id=1),
    # Lincoln Navigator -> SUV
    CarListingCategory(car_id=car_listings[24].car_id, cat_id=1),
    # Alfa Romeo Stelvio -> SUV
    CarListingCategory(car_id=car_listings[25].car_id, cat_id=1),
    # Acura MDX -> SUV
    CarListingCategory(car_id=car_listings[26].car_id, cat_id=1),
    # Tesla Model 3 -> Sedan
    CarListingCategory(car_id=car_listings[27].car_id, cat_id=2),
    # Ferrari 488 -> Coupe
    CarListingCategory(car_id=car_listings[28].car_id, cat_id=4),
    # Lamborghini Huracan -> Coupe
    CarListingCategory(car_id=car_listings[29].car_id, cat_id=4),
]

db.session.add_all(car_categories)
db.session.commit()


garage1 = Garage(user_id=user1.user_id)
garage2 = Garage(user_id=user2.user_id)

db.session.add(garage1)
db.session.add(garage2)
db.session.commit()
