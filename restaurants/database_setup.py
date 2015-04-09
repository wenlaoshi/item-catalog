import sys

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()
    
class Restaurant(Base):
    __tablename__ = 'restaurant'
    
    id = Column(Integer, primary_key = True)
    name = Column(String(80), nullable = False)
    category = Column(String(80))
    description = Column(String(250))
    address = Column(String(250))
    latlng = Column(String(32))
    telephone = Column(String(15))
    url = Column(String(124))
    hours = Column(String(80))
    image_url = Column(String(124))
    rating = Column(Integer)
    price_range = Column(Integer)

    @property
    def serialize(self):
        # Returns object data in an easily serialize-able format
        return {
            'name' : self.name,
            'description' : self.description,
            'id' : self.id,
            'category' : self.category,
            'address' : self.address,
            'latlng' : self.latlng,
            'telephone' : self.telephone,
            'url' : self.url,
            'hours' : self.hours,
            'image_url' : self.image_url,
            'rating' : self.rating,
            'price_range' : self.price_range,
        }


class MenuItem(Base):
    __tablename__ = 'menu_item'
    
    id = Column(Integer, primary_key = True)
    name = Column(String(80), nullable = False)
    course = Column(String(250))
    description = Column(String(250))
    price = Column(String(8))
    calories = Column(Integer)
    image_url = Column(String(124))
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
    
    restaurant = relationship(Restaurant)
    
    @property
    def serialize(self):
        # Returns object data in an easily serialize-able format
        return {
            'name' : self.name,
            'description' : self.description,
            'id' : self.id,
            'price' : self.price,
            'course' : self.course,
            'calories' : self.calories,
            'image_url' : self.image_url,
        }

   
####### insert at end of file #######

engine = create_engine('sqlite:///lbrestaurants.db')

Base.metadata.create_all(engine)