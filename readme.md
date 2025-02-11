# NyFlaskApp

## Beskrivning
NyFlaskApp är en enkel webbapplikation byggd med Flask. Applikationen använder OpenWeatherMap API för att hämta väderdata och lagrar sökningar i en SQLite-databas.

## Installation
Följ dessa steg för att installera och köra projektet lokalt:

1. Klona detta repository:
    ```bash
    git clone https://github.com/Abbekf/NyFlaskApp.git
    ```
2. Navigera till projektets katalog:
    ```bash
    cd NyFlaskApp
    ```
3. Skapa och aktivera en virtuell miljö:
    ```bash
    python -m venv venv
    source venv/bin/activate  # På Windows använd: venv\Scripts\activate
    ```
4. Installera beroenden:
    ```bash
    pip install -r requirements.txt
    ```

## Användning
För att starta applikationen, kör följande kommando:
```bash
python app.py
```
Öppna sedan din webbläsare och navigera till `http://127.0.0.1:5000` för att se applikationen i aktion.

## Struktur
Projektets katalogstruktur är som följer:
```
NyFlaskApp/
│
├── app/
│   ├── __init__.py
│   ├── routes.py
│   └── templates/
│       └── index.html
│
├── venv/
├── requirements.txt
└── readme.md
```

## Tekniker
- **Flask**: Ett mikroramverk för Python som används för att bygga webbapplikationen.
- **OpenWeatherMap API**: Ett API som används för att hämta väderdata baserat på användarens sökning.
- **SQLite**: En lättviktsdatabas som används för att lagra användarens sökningar.