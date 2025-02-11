from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

# Skapar en klass för att representera tabellen Search i databasen
class Search(db.Model): 
    id = db.Column(db.Integer, primary_key=True) # Primärnyckel för tabellen
    city = db.Column(db.String(50), nullable=False) # Kolumn för stadens namn, får inte vara null
    temperature = db.Column(db.Float, nullable=False) # Kolumn för temperaturen, får inte vara null
    description = db.Column(db.String(100), nullable=False) # Kolumn för väderbeskrivningen, får inte vara null
    timestamp = db.Column(db.DateTime, default=datetime.utcnow) # Kolumn för tidsstämpel, standardvärde är nuvarande tid

