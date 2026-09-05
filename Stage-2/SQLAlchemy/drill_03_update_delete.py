"""
Specifications:
Model & Engine: Set up Base, Product, and engine pointing to drill_01.db (using the deterministic BASE_DIR = os.path.dirname(os.path.abspath(__file__))).
"""
from sqlalchemy import create_engine, String, Float, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session
import os

class Base(DeclarativeBase):
    pass
class Product(Base):
    __tablename__ = "products"
    id: Mapped[int] = mapped_column(primary_key = True)
    name: Mapped[str] = mapped_column(String(60))
    price: Mapped[float] = mapped_column(Float)

BASE_DIR = os.path.dirname(os.path.abspath(__file__)) 
engine = create_engine(f"sqlite:///{BASE_DIR}/drill_01.db", echo = True)
Base.metadata.create_all(engine)
print("Table created Successfully")

"""Seed Data Check:
In a session, check if any products exist using select(Product).
If the table is empty, insert the 3 initial products:
Laptop (75000.0)
Mouse (850.0)
Keyboard (2200.0) and session.commit().
"""
with Session(engine) as session: 
    smt = select(Product)
    existing = session.execute(select(Product)).scalars().first()
    if not existing:
        p = Product(name="Laptop",   price=75000.0)
        q = Product(name="Mouse",    price=850.0)
        r = Product(name="Keyboard", price=2200.0)
        session.add_all([p,q,r])
        session.commit()
        print("3 products inserted.\n")
"""
Perform UPDATE:
Find the product where Product.name == "Mouse".
Print: f"Before Update: {product.name} costs {product.price}"
Update its price to 999.0.
Call session.commit().
Print: f"After Update: {product.name} costs {product.price}"
Perform DELETE:
Find the product where Product.name == "Keyboard".
If found, call session.delete(product) and session.commit().
Print: "Deleted Keyboard successfully."
Verify Final State:
In a fresh SELECT query, fetch all products and print each remaining product:
ID: ... | Name: ... | Price: ...
(Only Laptop and Mouse at 999.0 should appear; Keyboard must be gone!)
"""
with Session(engine) as session:
    smt = select(Product).where(Product.name == "Mouse")
    product = session.execute(smt).scalars().first()
    if product:
        print(f"Before Update: {product.name} costs {product.price}")
        product.price = 999.0
        session.commit()
        print(f"After Update: {product.name} costs {product.price}")
    else:
        print("Product not found !")

with Session(engine) as session:
    smt = select(Product).where(Product.name == "Keyboard")
    product = session.execute(smt).scalars().first()
    if product:
        session.delete(product)
        session.commit()
        print("Deleted Keyboard successfully.")
    else:
        print("Product not found!")

with Session(engine) as session:
    smt = select(Product)
    result = session.execute(smt).scalars().all()
    print("--- All Products ---")
    for product in result:
        print(f"ID: {product.id} | Name: {product.name} | Price: {product.price}")
    

