from flask import Flask, render_template
import pathlib
import sqlite3

base_path = pathlib.Path(r'C:\DAB111\final_project\bassey_complete\database')
db_name = "bikes.db"
db_path = base_path / db_name
print(db_path)

app = Flask(__name__)

@app.route("/")
def index():
    return render_template(
        "index.html",
        title="Home Page", 
        message="Hello, welcome to Group 14 Flask app!",
        year=2024
    )

@app.route("/about")
def about():
    data_sources = [
        {"name": "Bike Sales Database", "link": "https://www.kaggle.com/datasets/efoceeworld/bikes-orderliness/data"}
    ]
    data_definitions = [
        {"name": "order_date", "definition": "The date when the order was placed.", "type": "Date"},
        {"name": "order_id", "definition": "A unique identifier for each order.", "type": "Ordinal"},
        {"name": "quantity", "definition": "The number of items ordered.", "type": "Discrete"},
        {"name": "price", "definition": "The price per item.", "type": "Discrete"},
        {"name": "total_price", "definition": "The total cost for the order.", "type": "Discrete"},
        {"name": "city", "definition": "The city where the order was shipped.", "type": "Category"},
        {"name": "state", "definition": "The state where the order was shipped.", "type": "Category"}
    ]
    return render_template(
        "about.html",
        data_source_description="Our data is sourced from trusted providers and regularly updated for accuracy.",
        data_sources=data_sources,
        data_definitions=data_definitions,
        year=2024
    )

@app.route("/data")
def data():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    records = cursor.execute("SELECT * FROM bikes_orderlines limit 40").fetchall()
    columns = [description[0] for description in cursor.description]
    conn.close()
    return render_template("data.html", columns=columns, records=records, year=2024)


if __name__=="__main__":
    app.run(debug=True)