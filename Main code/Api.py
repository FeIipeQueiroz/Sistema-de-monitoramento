from flask import Flask
from flask import render_template
import Server

app = Flask(__name__)

#Definição da rota da aplicação
@app.route('/', methods=['GET'])
def home():
    return render_template("index.html", Patients=Server.Patients), 200

if __name__ == '__main__':
    app.run()