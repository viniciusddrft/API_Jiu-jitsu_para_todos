from flask import Flask,jsonify,request
import os

app = Flask(__name__)

data = {
    "title" : "Homem Aranha",
    "url" : "https://homemaranha.com.br"
}

@app.route("/",methods =["GET"])
def apiGet():
    return jsonify(data)

@app.route("/",methods =["POST"])
def apiPost():
    result = request.get_json()
    if(result.get('title')):
        return jsonify({
            'statusCode': 200,
            'body':result,
        })
    else:
        return jsonify({
            'statusCode': 404,
            'body':{},
        })

if(__name__ == '__main__'):
    port = int(os.environ.get("PORT",5000))
    app.run(host='0.0.0.0', debug=True,port=port)
    