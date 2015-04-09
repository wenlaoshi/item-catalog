from flask import Flask, render_template, request, abort, session, redirect, url_for, flash, jsonify, Response
import requests

app = Flask(__name__)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

engine = create_engine('sqlite:///lbrestaurants.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
sqlsession = DBSession()


# Make JSON API Endpoints (GET Requests)
@app.route('/restaurants/JSON')
def restaurantListJSON():
    restaurants = sqlsession.query(Restaurant).all()
    return jsonify(Restaurants=[i.serialize for i in restaurants])

@app.route('/restaurants/<int:restaurant_id>/menu/JSON')
def restaurantMenuJSON(restaurant_id):
    restaurant = sqlsession.query(Restaurant).filter_by(id = restaurant_id).one()
    items = sqlsession.query(MenuItem).filter_by(restaurant_id = restaurant_id).all()
    return jsonify(MenuItems=[i.serialize for i in items])

@app.route('/restaurants/<int:restaurant_id>/menu/<int:menu_id>/JSON')
def restaurantMenuItemJSON(restaurant_id, menu_id):
    item = sqlsession.query(MenuItem).filter_by(id = menu_id).one()
    return jsonify(MenuItem=[item.serialize])

# Convert data objects into XML 
def xmlify(myobj):
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml = xml + '<' + myobj.__class__.__name__ + '>\n'
    if type(myobj) == type([]):
        for item in myobj:
            mydict = item.serialize
            xml = xml + '<' + item.__class__.__name__ + '>\n'
            for key in sorted(mydict.iterkeys()):
                xml = xml + '  <' + str(key) + '>' + str(mydict[key]).replace('&', '&amp;')  + '</' + str(key) + '>\n'
            xml = xml + '</' + item.__class__.__name__ + '>\n'
    else:
        item = myobj.serialize
        for key in sorted(item.iterkeys()):
            xml = xml + '  <' + str(key) + '>' + str(item[key]).replace('&', '&amp;')  + '</' + str(key) + '>\n'
    xml = xml + '</' + myobj.__class__.__name__ + '>'
    return xml
    
# Make XML API Endpoints (GET Requests)
@app.route('/restaurants/XML')
def restaurantListXML():
    restaurants = sqlsession.query(Restaurant).all()
    return Response(xmlify(restaurants), mimetype='text/xml')
    
@app.route('/restaurants/<int:restaurant_id>/menu/XML')
def restaurantMenuXML(restaurant_id):
    restaurant = sqlsession.query(Restaurant).filter_by(id = restaurant_id).one()
    items = sqlsession.query(MenuItem).filter_by(restaurant_id = restaurant_id).all()
    return Response(xmlify(items), mimetype='text/xml')
    
@app.route('/restaurants/<int:restaurant_id>/menu/<int:menu_id>/XML')
def restaurantMenuItemXML(restaurant_id, menu_id):
    item = sqlsession.query(MenuItem).filter_by(id = menu_id).one()
    return Response(xmlify(item), mimetype='text/xml')



# Restaurant List
@app.route('/')
@app.route('/restaurants')
def showRestaurants():
    restaurants = sqlsession.query(Restaurant).all()
    return render_template('restaurants.html', items = restaurants)
  
# Add New Restaurant
@app.route('/restaurant/new', methods=['GET','POST'])
def newRestaurant():
  if request.method == 'POST':
    restaurant = Restaurant()
    restaurant.name = request.form['name']
    restaurant.category = request.form['category']
    restaurant.description = request.form['description']
    restaurant.rating = request.form['rating']
    restaurant.price_range = request.form['price_range']
    restaurant.address = request.form['address']
    restaurant.latlng = request.form['latlng']
    restaurant.telephone = request.form['telephone']
    restaurant.url = request.form['url']
    restaurant.hours = request.form['hours']
    restaurant.image_url = request.form['image_url']
    sqlsession.add(restaurant)
    sqlsession.commit()
    flash("New Restaurant Created")
    return redirect(url_for('showRestaurants'))
  else:
    return render_template('newRestaurant.html')
  
# Edit Existing Restaurant
@app.route('/restaurant/<int:restaurant_id>/edit', methods=['GET','POST'])
def editRestaurant(restaurant_id):
  restaurant = sqlsession.query(Restaurant).filter_by(id = restaurant_id).one()
  if request.method == 'POST':
    restaurant.name = request.form['name']
    restaurant.category = request.form['category']
    restaurant.description = request.form['description']
    restaurant.rating = request.form['rating']
    restaurant.price_range = request.form['price_range']
    restaurant.address = request.form['address']
    restaurant.latlng = request.form['latlng']
    restaurant.telephone = request.form['telephone']
    restaurant.url = request.form['url']
    restaurant.hours = request.form['hours']
    restaurant.image_url = request.form['image_url']
    sqlsession.add(restaurant)
    sqlsession.commit()
    flash("Restaurant Successfully Edited")
    return redirect(url_for('showRestaurants'))
  else:
    return render_template('editRestaurant.html', restaurant = restaurant)
  
# Delete Existing Restaurant
@app.route('/restaurant/<int:restaurant_id>/delete', methods=['GET','POST'])
def deleteRestaurant(restaurant_id):
  restaurant = sqlsession.query(Restaurant).filter_by(id = restaurant_id).one()
  if request.method == 'POST':
    sqlsession.delete(restaurant)
    sqlsession.commit()
    flash("Restaurant Successfully Deleted")
    return redirect(url_for('showRestaurants'))
  else:
    return render_template('deleteRestaurant.html', restaurant = restaurant)
  
# Show Restaurant Menu
@app.route('/restaurant/<int:restaurant_id>')
@app.route('/restaurant/<int:restaurant_id>/menu')
def restaurantMenu(restaurant_id):
  restaurant = sqlsession.query(Restaurant).filter_by(id = restaurant_id).one()
  items = sqlsession.query(MenuItem).filter_by(restaurant_id = restaurant.id)
  return render_template('menu.html', restaurant = restaurant, items = items)
  
# Add New Menu Item
@app.route('/restaurant/<int:restaurant_id>/menu/new', methods=['GET','POST'])
def newMenuItem(restaurant_id):
  if request.method == 'POST':
    item = MenuItem()
    item.name = request.form['name']
    item.course = request.form['course']
    item.description = request.form['description']
    item.price = request.form['price']
    item.calories = request.form['calories']
    item.image_url = request.form['image_url']
    item.restaurant_id = restaurant_id
    sqlsession.add(item)
    sqlsession.commit()
    flash("Menu Item Created")
    return redirect(url_for('restaurantMenu', restaurant_id = restaurant_id))
  else:
    restaurant = sqlsession.query(Restaurant).filter_by(id = restaurant_id).one()
    return render_template('newMenuItem.html', restaurant = restaurant)
  
# Edit Existing Menu Item
@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/edit', methods=['GET','POST'])
def editMenuItem(restaurant_id, menu_id):
  item = sqlsession.query(MenuItem).filter_by(id = menu_id, restaurant_id = restaurant_id).one()
  if request.method == 'POST':
    item.name = request.form['name']
    item.course = request.form['course']
    item.description = request.form['description']
    item.price = request.form['price']
    item.calories = request.form['calories']
    item.image_url = request.form['image_url']
    item.restaurant_id = restaurant_id
    sqlsession.add(item)
    sqlsession.commit()
    flash("Menu Item Successfully Edited")
    return redirect(url_for('restaurantMenu', restaurant_id = restaurant_id))
  else:
    return render_template('editMenuItem.html', item = item)
  
# Delete Existing Menu Item
@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/delete', methods=['GET','POST'])
def deleteMenuItem(restaurant_id, menu_id):
  item = sqlsession.query(MenuItem).filter_by(id = menu_id, restaurant_id = restaurant_id).one()
  if request.method == 'POST':
    sqlsession.delete(item)
    sqlsession.commit()
    flash("menu item deleted")
    return redirect(url_for('restaurantMenu', restaurant_id = restaurant_id))
  else:
    return render_template('deleteMenuItem.html', restaurant_id = restaurant_id, item = item)
  
# Mozilla Persona Authentication Login
# Code from https://github.com/mozilla/browserid-cookbook
@app.route('/auth/login', methods=["POST"])
def login():
    if 'assertion' not in request.form:
        abort(400)

    assertion_info = {'assertion': request.form['assertion'], 'audience': 'localhost:5000' }
    resp = requests.post('https://verifier.login.persona.org/verify', data=assertion_info, verify=True)

    if not resp.ok:
        abort(500)

    data = resp.json()

    if data['status'] == 'okay':
        session.update({'email': data['email']})
        flash("You are now signed in as " + data['email'] + ".")
        return resp.content

# Mozilla Persona Authentication Logout
@app.route('/auth/logout', methods=["POST"])
def logout():
    session.pop('email', None)
    return redirect('/')
    
    
    
if __name__ == '__main__':
    app.secret_key = 'dude, this is my super secret key'
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)