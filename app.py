from flask import Flask, render_template, url_for, request, redirect,send_file
import pandas as pd
from flask import jsonify
app = Flask(__name__)

# @app.route('/', methods=['POST'])
# def index():
#     if request.method == 'POST':
#         saveFolder = 'D:/Workspace/tuto/static/music/'
#         path = request.files['file']
#         track = path.filename
#         fullPath = saveFolder + track
#         path.save(fullPath)
#         g = getGenra(fullPath)
#         m_ganre = ['blues','classical', 'country','disco', 'hiphop','jazz','metal','pop','reggae','rock']
#         return render_template('index.html',g = m_ganre[g[0]], etat = 'details')
#     else:
#         return "hi"

# @app.route('/', methods=['POST'])

data =  pd.read_csv("./db.csv")
def calcPrix(region_val,commune_val,type_val,surface_val):
    if type_val == "appart":
        _type = "Prix_m2_appart_regression"
    else:
        _type = "Prix_m2_villa_regression"
    _prix = data[_type][data.Region==region_val][data.Commune==commune_val].values.item()
    return float(surface_val) * float(_prix.replace('MAD', '').replace(' ', '')) 

@app.route("/", methods =["GET", "POST"])
def funPrix():
    if request.method == "POST":
       region_val = request.form.get("region")
       commune_val = request.form.get("commune")
       surface_val = request.form.get("surface")
       type_val = request.form.get("type")
       return jsonify("prix: " + str(calcPrix(region_val,commune_val,type_val,surface_val)))
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
