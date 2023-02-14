from app import *

with app.app_context():
    db.create_all()
    item1= Item(name="iPhone 14", price=1500, barcode="646483856343", description="256GB ROM")
    db.session.add(item1)
    db.session.commit()
    item= Item(name="iPhone 14 Pro Max", price=1700, barcode="646483856343", description="The Pallets organization develops and supports Flask-SQLAlchemy and other popular packages. In order to grow the community of contributors and users, and allow the maintainers to devote more time to the projects, please donate today.")
    db.session.add(item2)
    db.session.commit()
    print(Item.query.all())
  #u2=User(username="Almubaraq", email_address="peace@gmail.com", password_hash="zamani_akinlaso", budget=45000)