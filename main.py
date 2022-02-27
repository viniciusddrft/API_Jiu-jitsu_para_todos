from flask import Flask,jsonify,request
import os

app = Flask(__name__)

data = []

@app.route("/",methods =["GET"])
def apiGetAll():
    return jsonify({
            'statusCode': 200,
            'body':data,
        })


if(__name__ == '__main__'):
    port = int(os.environ.get("PORT",5000))
    app.run(host='0.0.0.0', debug=True,port=port)
    