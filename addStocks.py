import json
import os
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

# Define your database URL
from application.config import LocalDevelopmentConfig
from application.models import Stock

# Setup SQLAlchemy
Base = declarative_base()
engine = create_engine(LocalDevelopmentConfig.SQLALCHEMY_DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()




# Load the JSON file
with open('mapping.json', 'r') as file:
    data = json.load(file)

# Insert the data
for ticker, name in data.items():
    stock = Stock(ticker=ticker, name=name)
    session.add(stock)

# Commit the transaction
session.commit()

# Close the session
session.close()

print("Data inserted successfully!")
