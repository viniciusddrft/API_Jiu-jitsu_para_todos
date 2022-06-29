from flask import Flask, jsonify
import os
from src.db.quiz.data_english_white_belt import dataEnglishWhiteBelt
from src.db.quiz.data_english_blue_belt import dataEnglishBlueBelt
from src.db.quiz.data_english_black_belt import dataEnglishBlackBelt
from src.db.quiz.data_english_all import dataEnglishAll
from src.db.quiz.data_portuguese_white_belt import dataPortugueseWhiteBelt
from src.db.quiz.data_portuguese_blue_belt import dataPortugueseBlueBelt
from src.db.quiz.data_portuguese_black_belt import dataPortugueseBlackBelt
from src.db.quiz.data_portuguese_all import dataPortugueseAll
from src.db.quiz.data_all import dataAll
from src.db.wallpapers.data_wallpaper import wallpapers

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route("/quiz", methods=["GET"])
def apiGetAll():
    return jsonify({
        'statusCode': 200,
        'body': dataAll,
    })


@app.route("/quiz/english", methods=["GET"])
def apiGetEnglish():
    return jsonify({
        'statusCode': 200,
        'body': dataEnglishAll,
    })


@app.route("/quiz/english/whitebelt", methods=["GET"])
def apiGetEnglishWhiteBelt():
    return jsonify({
        'statusCode': 200,
        'body': dataEnglishWhiteBelt.toJson(),
    })


@app.route("/quiz/english/bluebelt", methods=["GET"])
def apiGetEnglishBlueBelt():
    return jsonify({
        'statusCode': 200,
        'body': dataEnglishBlueBelt.toJson(),
    })


@app.route("/quiz/english/blackbelt", methods=["GET"])
def apiGetEnglishBlackBelt():
    return jsonify({
        'statusCode': 200,
        'body': dataEnglishBlackBelt.toJson(),
    })


@app.route("/quiz/portuguese", methods=["GET"])
def apiGetPotuguese():
    return jsonify({
        'statusCode': 200,
        'body': dataPortugueseAll,
    })


@app.route("/quiz/portuguese/whitebelt", methods=["GET"])
def apiGetPotugueseWhiteBelt():
    return jsonify({
        'statusCode': 200,
        'body': dataPortugueseWhiteBelt.toJson(),
    })


@app.route("/quiz/portuguese/bluebelt", methods=["GET"])
def apiGetPotugueseBlueBelt():
    return jsonify({
        'statusCode': 200,
        'body': dataPortugueseBlueBelt.toJson(),
    })


@app.route("/quiz/portuguese/blackbelt", methods=["GET"])
def apiGetPotugueseBlackBelt():
    return jsonify({
        'statusCode': 200,
        'body': dataPortugueseBlackBelt.toJson(),
    })


@app.route("/wallpapers", methods=["GET"])
def apiGetWallpapers():
    return jsonify({
        'statusCode': 200,
        'body': wallpapers.toJson(),
    })


if(__name__ == '__main__'):
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', debug=True, port=port)
