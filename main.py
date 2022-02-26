from flask import Flask,jsonify
import os


app = Flask(__name__)

data = {
    "title" : "Homem Aranha",
    "url" : "https://homemaranha.com.br"
}

@app.route("/",methods =["GET"])
def api():
    return jsonify(data)

if(__name__ == '__main__'):
    port = int(os.environ.get("PORT",5000))
    app.run(host='0.0.0.0', debug=True,port=port)
    