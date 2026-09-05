"""
Drill 02: Sessions — INSERT and SELECT using SQLAlchemy ORM.
No raw SQL strings. All data operations go through Python objects.
"""
import os
from sqlalchemy import create_engine, String, Float, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session

# --- Model Setup (same as Drill 01) ---

class Base(DeclarativeBase):
    pass

class Product(Base):
    __tablename__ = "products"
    id:    Mapped[int]   = mapped_column(primary_key=True)
    name:  Mapped[str]   = mapped_column(String(60))
    price: Mapped[float] = mapped_column(Float)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
engine = create_engine(f"sqlite:///{BASE_DIR}/drill_01.db", echo=True)
Base.metadata.create_all(engine)
print("Table ready.\n")

# --- INSERT 3 Products ---

with Session(engine) as session:
    p = Product(name="Laptop",   price=75000.0)
    q = Product(name="Mouse",    price=850.0)
    r = Product(name="Keyboard", price=2200.0)
    session.add_all([p, q, r])
    session.commit()
    print("3 products inserted.\n")

# --- SELECT All Products ---

with Session(engine) as session:
    stmt   = select(Product)
    result = session.execute(stmt).scalars().all()

    print("--- All Products ---")
    for product in result:
        print(f"ID: {product.id} | Name: {product.name} | Price: {product.price}")

    print("\n--- Products with price > 1000 ---")
    for product in result:
        if product.price > 1000:
            print(f"ID: {product.id} | Name: {product.name} | Price: {product.price}")

print("\ncode run successfully.")
