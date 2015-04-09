from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Restaurant, Base, MenuItem

engine = create_engine('sqlite:///lbrestaurants.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()



#Menu for Starling Diner
restaurant = Restaurant(name = "Starling Diner", category = "American", description = "Casually stylish, independent local cafe serving updated diner eats with coffee & wine.", address = "4114 E 3rd St. Long Beach, CA 90814", latlng = "33.767917,-118.144339", telephone = "562-433-2041", url = "http://www.starlingdiner.com", hours = "Tuesday-Sunday 8:00AM-3:00PM", image_url = "http://www.breakfastbanter.com/wp-content/uploads/2013/01/IMG_3485.jpg", rating = 4, price_range = 2)
session.add(restaurant)
session.commit()

menuItem = MenuItem(name = "Broiled San Francisco Stuffed Toast", description = "French toast stuffed with creamy Mascarpone and Crme Fraiche. French Toast like you've never had it before--broiled instead of fried, which gives the flavor a deeper dimension.", price = "11", course = "Breakfast", image_url = "http://static.wixstatic.com/media/c0b337_01dda8d619508b558a191974288c1d3a.jpg", calories = 980, restaurant = restaurant)
session.add(menuItem)
session.commit()

menuItem = MenuItem(name = "Goat Cheese and Mushroom Scramble", description = "Two eggs scrambled with herbed goat cheese, spinach, and shiitake mushrooms. Served with polenta potatoes & sliced baguette.", price = "9", course = "Breakfast", image_url = "http://a4.urbancdn.com/w/s/Wr/mxQdWYIER4PHgQ.jpg", calories = 620, restaurant = restaurant)
session.add(menuItem)
session.commit()

menuItem = MenuItem(name = "Smoked Wild Salmon", description = "Layers of thinly sliced salmon, fresh dill, avocado cream , baby greens and slivered red onions served on a fresh, crispy baguette. Comes with soup or salad.", price = "9", course = "Sandwiches", image_url = "http://s3.amazonaws.com/foodspotting-ec2/reviews/2086063/thumb_600.jpg?1342799466?1427440474", calories = 360, restaurant = restaurant)
session.add(menuItem)
session.commit()

menuItem = MenuItem(name = "Breakfast Polenta", description = "Polenta with fresh seasonal berries and cream", price = "6.95", course = "Breakfast", image_url = "http://www.roadfood.com/Photos/21743.jpg", calories = 410, restaurant = restaurant)
session.add(menuItem)
session.commit()

menuItem = MenuItem(name = "Cream Scones", description = "Baked-Every-Morning Basket of Scones served w/ house made lemon curd (limited availability).", price = "5.95", course = "Breakfast", image_url = "http://www.roadfood.com/photos/21696.jpg", calories = 280, restaurant = restaurant)
session.add(menuItem)
session.commit()


#Menu for Roscoe's
restaurant = Restaurant(name = "Roscoe's House of Chicken and Waffles", category = "Soul Food", description = "Where Fried Chicken is our specialty!!! No one knows chicken like we do. But that's only part of our story, we are also famous for our delicious greens, Mac and Cheese, hot water cornbread, and red beans and rice.", address = "730 E Broadway, Long Beach, CA 90802", latlng = "33.769059,-118.183114", telephone = "562-437-8355", url = "http://www.roscoeschickenandwaffles.com/", hours = "Daily 8:00AM-11:00PM", image_url = "https://s-media-cache-ak0.pinimg.com/originals/77/8f/17/778f17a3b202a459a6dfc4f577548964.jpg", rating = 4, price_range = 2)
session.add(restaurant)
session.commit()

menuItem = MenuItem(name = "Obama Special", description = "Three southern style Chicken Wings with two waffles", price = "8.40", course = "Brunch	", image_url = "http://www.kcet.org/living/food/assets/images/roscoes.jpg", calories = 780, restaurant = restaurant)
session.add(menuItem)
session.commit()
	
menuItem = MenuItem(name = "Jean's Delight", description = "Mixed Greens, Thigh, Macaroni & Cheese and Hot Water Cornbread", price = "7.70", course = "Brunch", image_url = "http://static.panoramio.com/photos/large/4099487.jpg", calories = 920, restaurant = restaurant)
session.add(menuItem)
session.commit()

menuItem = MenuItem(name = "Herb's Special", description = "Half Chicken prepared southern style with two waffles", price = "15.30", course = "Brunch", image_url = "https://livewirepast.files.wordpress.com/2008/09/chick-and-waffles.jpg", calories = 960, restaurant = restaurant)
session.add(menuItem)
session.commit()

menuItem = MenuItem(name = "Home Style", description = "Two Sausage Patties, two Eggs, Grits or Waffle & Biscuit", price = "8.30", course = "Brunch", image_url = "http://s3.amazonaws.com/foodspotting-ec2/reviews/1455048/thumb_600.jpg?1331741240", calories = 410, restaurant = restaurant)
session.add(menuItem)
session.commit()

menuItem = MenuItem(name = "Leg or Thigh & Waffle", description = "Crispy southern style chicken and waffle", price = "6.90", course = "Brunch", image_url = "http://chicrunner.com/wp-content/uploads/2010/06/roscoes-chick-and-waff.jpg", calories = 280, restaurant = restaurant)
session.add(menuItem)
session.commit()


#Menu for The Local Spot
restaurant = Restaurant(name = "The Local Spot", category = "American", description = "The Local Spot has earned a place in the hearts of local diners. Our dog-friendly outdoor patio is a great way to enjoy our famous banana pancakes, hand-made breakfast burritos, freshly ground Javatini's coffee, crisp salads and mouth-watering sandwiches.", address = "6200 Pacific Coast Hwy, Long Beach, CA 90803", latlng = "33.767043,-118.11718", telephone = "562-498-0400", url = "http://thelocalspotlongbeach.com/menus/dinner/", hours = "Daily 7:00AM-2:00PM", image_url = "http://blogs.ocweekly.com/stickaforkinit/localspot1.jpg", rating = 4, price_range = 1)
session.add(restaurant)
session.commit()

menuItem = MenuItem(name = "California Spuds", description = "A meal in itself! We take our delicious home fries and top them with generous portions of avocado, cheddar cheese and sour cream.", price = "5.45", course = "Breakfast	", image_url = "http://blogs.ocweekly.com/stickaforkinit/localspot3.jpg", calories = 510, restaurant = restaurant)
session.add(menuItem)
session.commit()
	
menuItem = MenuItem(name = "Bananna Pancakes", description = "Two fluffy buttermilk pancakes with bannanas and fresh maple syrup", price = "6.95", course = "Breakfast", image_url = "http://s3-media3.fl.yelpcdn.com/bphoto/zayxg-dOyfDmuHYxEJcJog/o.jpg", calories = 550, restaurant = restaurant)
session.add(menuItem)
session.commit()

menuItem = MenuItem(name = "California Benedict", description = "Two poached eggs on an English Muffin topped with homemade hollandaise sauce, avocado and bacon. Served with home fries, brown rice or fruit.", price = "8.95", course = "Breakfast", image_url = "http://s3.amazonaws.com/foodspotting-ec2/reviews/1895220/thumb_600.jpg?1339698161", calories = 1050, restaurant = restaurant)
session.add(menuItem)
session.commit()

menuItem = MenuItem(name = "Aloha Omelette", description = "Three eggs, portugese sausage, spinach, onion, and swiss cheese. Served with home fries, brown rice or fruit, and choice of toast, tortillas or biscuit & gravy.", price = "8.95", course = "Breakfast", image_url = "http://media-cdn.tripadvisor.com/media/photo-s/07/77/fa/45/aloha-omelette-10.jpg", calories = 850, restaurant = restaurant)
session.add(menuItem)
session.commit()

menuItem = MenuItem(name = "Rancho Omelette", description = "Three eggs, steak, mushrooms, onions, bell peppers, cheddar cheese and topped with our homemade Ranchero sauce. Served with home fries, brown rice or fruit, and choice of toast, tortillas or biscuit & gravy.", price = "8.95", course = "Breakfast", image_url = "http://media-cdn.tripadvisor.com/media/photo-s/07/78/05/20/rancho-omelette-12.jpg", calories = 890, restaurant = restaurant)
session.add(menuItem)
session.commit()


#Menu for Schooner Or Later
restaurant = Restaurant(name = "Schooner Or Later", category = "American", description = "American breakfast & lunch fare, plus cocktails, on a spacious patio with marina views.", address = "241 Marina Dr, Long Beach, CA 90803", latlng = "33.752168,-118.108183", telephone = "562-430-3495", url = "http://www.schoonerorlater.com/", hours = "Monday-Friday 6:30AM-3:00PM and Saturday-Sunday 6:30AM-4:00PM", image_url = "http://static1.squarespace.com/static/52588671e4b0b7382f16a3db/529684fbe4b0f3077c25da89/529685e7e4b0d642edd5f664/1385596392605/IMG_5662_resized.jpg?format=500w", rating = 4, price_range = 2)
session.add(restaurant)
session.commit()

menuItem = MenuItem(name = "The Mess", description = "This world famous, local tradition is a tasty blend of chopped ham, onion, and bell pepper grilled with hash browns and eggs.  Topped with melted Cheddar cheese. Served with sourdough toast.", price = "11.15", course = "Breakfast	", image_url = "http://a4.urbancdn.com/w/s/ML/oJMQPO6V7C0IhM-640m.jpg", calories = 810, restaurant = restaurant)
session.add(menuItem)
session.commit()
	
menuItem = MenuItem(name = "Tuna Sandwich", description = " Tuna salad with mayo, celery and sweet pickle on your choice of bread.", price = "9.45", course = "Sandwich", image_url = "http://s3.amazonaws.com/foodspotting-ec2/reviews/380925/thumb_600.jpg?1298850293", calories = 520, restaurant = restaurant)
session.add(menuItem)
session.commit()

menuItem = MenuItem(name = "Belgian Waffle", description = "Belgian Waffle with seasonal berries, bananas and cream.", price = "8.85", course = "Breakfast", image_url = "http://s3.amazonaws.com/foodspotting-ec2/reviews/1895220/thumb_600.jpg?1339698161", calories = 850, restaurant = restaurant)
session.add(menuItem)
session.commit()

menuItem = MenuItem(name = "Crab & Avocado Benedict", description = "Poached eggs and Crab on an English muffin. Topped with avocado and Hollandaise sauce. Served with hash browns or spinach.", price = "15.45", course = "Breakfast", image_url = "http://s3.amazonaws.com/foodspotting-ec2/reviews/538139/thumb_600.jpg?1304285908", calories = 1050, restaurant = restaurant)
session.add(menuItem)
session.commit()

menuItem = MenuItem(name = "Italian Omlette", description = "Mildly spiced Italian sausage and Mozzarella topped with zesty Italian sauce and  sour cream.", price = "10.85", course = "Breakfast", image_url = "http://californiathroughmylens.com/wp-content/uploads/2012/01/italian-omelette-at-schooner-or-later.jpg", calories = 890, restaurant = restaurant)
session.add(menuItem)
session.commit()


#Menu for The Potholder Cafe
restaurant = Restaurant(name = "The Potholder Cafe", category = "American", description = "American & Mexican comfort foods plus breakfast all day served in homey diner digs with booths.", address = "3700 E Broadway, Long Beach, CA 90803", latlng = "33.764315,-118.148989", telephone = "562-433-9305", url = "http://www.schoonerorlater.com/", hours = "Monday-Friday 7AM-3PM and Saturday-Sunday 7AM-4PM", image_url = "http://www.thepotholdercafe.com/images/a.jpg", rating = 4, price_range = 1)
session.add(restaurant)
session.commit()

menuItem = MenuItem(name = "Flaky French Toast", description = "French toast dippd in corn flakes with strawberries and cream cheese filling.", price = "10.95", course = "Breakfast	", image_url = "http://s3.amazonaws.com/foodspotting-ec2/reviews/264280/thumb_600.jpg?1293332693", calories = 910, restaurant = restaurant)
session.add(menuItem)
session.commit()
	
menuItem = MenuItem(name = "Club Sandwich", description = "Triple decker sandwich with ham, bacon, turkey, lettuce, tomato and mayo. Served with curly fries.", price = "9.45", course = "Sandwich", image_url = "http://s3-media1.fl.yelpcdn.com/bphoto/sbTtNvbLbg_1AyaxG_EPfQ/o.jpg", calories = 880, restaurant = restaurant)
session.add(menuItem)
session.commit()

menuItem = MenuItem(name = "Breakfast Enchiladas", description = "Eggs & Cheese in COrn Tortillas, SOur Cream, Avocado & Enchilada Sauce.", price = "9.95", course = "Breakfast", image_url = "http://s3-media1.fl.yelpcdn.com/bphoto/kpWSfVoE2hbTjW2mC8NuLg/348s.jpg", calories = 910, restaurant = restaurant)
session.add(menuItem)
session.commit()

menuItem = MenuItem(name = "Mac Daddy Frankie", description = "One 18 inch pancake, two eggs and two bacon or sausage.", price = "13.95", course = "Breakfast", image_url = "http://s3-media3.fl.yelpcdn.com/bphoto/XnCrawAOF3L_284vb267Hg/o.jpg", calories = 950, restaurant = restaurant)
session.add(menuItem)
session.commit()

menuItem = MenuItem(name = "El Matador", description = "Three egg omlette with ortega chili, jack cheese, avocado, salsa & sour cream. Served with potatoes and your choice of toast, tortilla or biscuit.", price = "9.95", course = "Breakfast", image_url = "http://s3-media4.fl.yelpcdn.com/bphoto/e1Me7vj-8pKKbMSjmtDkEA/o.jpg", calories = 830, restaurant = restaurant)
session.add(menuItem)
session.commit()



