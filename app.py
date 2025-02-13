from flask import Flask, flash, render_template, request
from flask_sqlalchemy import SQLAlchemy
from weather import get_weather
from models import db, Search


# Skapa en instans av Flask
app = Flask(__name__)

# Visar vart databasen ska skapas
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///weather.db"

# kopplar ihop db med flask
db.init_app(app)

# kollar om databasen finns, om inte skapas den. Annars görs ingenting
with app.app_context(): 
    db.create_all()  

# Skapa en route för startsidan som kan hantera GET och POST requests
@app.route('/', methods=['GET', 'POST']) 
def home():
    weather_data = None # skapar en variabel för att lagra väderdata
    recent_searches = Search.query.order_by(Search.timestamp.desc()).limit(5).all()  # Hämta senaste 5 sökningar


    if request.method == 'POST': # kollar om användaren har skickat in ett formulär
        city = request.form.get('city') # hämtar staden användaren skrivit in

        if city: 
            weather_data = get_weather(city) # har användaren skrivit in en stad så hämtar vi väderdata för staden

            if weather_data: 
                new_search = Search( # skapar en ny sökning i databasen så att vi kan spara den
                    city=weather_data["city"], # sparar staden användaren sökt på
                    temperature=weather_data["temperature"], # sparar temperaturen för staden användaren sökt på
                    description=weather_data["description"] # sparar beskrivningen för staden användaren sökt på
                )
                db.session.add(new_search) # lägger till den nya sökningen i databasen
                db.session.commit() # sparar den nya sökningen i databasen

# skickar med väderdata och senaste sökningar till index.html
    return render_template('index.html', weather=weather_data, searches=recent_searches) 

if __name__ == '__main__': # kollar om filen körs direkt eller importeras av en annan fil 
    app.run(debug=True) # startar webbservern och sätter debug-läge till True så att vi får felmeddelanden om något går fel 
