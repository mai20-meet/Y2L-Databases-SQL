
from model import Base, product


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_product(name, price, picture_link, description):
    product_object = product(
        name=name,
        price=price,
        picture_link=picture_link,
        description=description)
    session.add(product_object)
    session.commit()

def update_lab_status(name, finished_lab):

   product_object = session.query(
       product).filter_by(
       product_id=product_id).first()
   product_object.finished_lab = finished_lab
   session.commit()


def delete_product(their_name):

   session.query(product).filter_by(
       product_id=product_id).delete()
   session.commit()


def query_all():

   products = session.query(
      product).all()
   return products


print(query_all())

def query_by_id():

   products = session.query(
      product_id=product_id)
   return products

def Add_To_Cart(cart):
    product_object = product(
         cart=cart)
    session.add(product_object)
    session.commit()



print(query_all())