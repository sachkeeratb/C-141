from flask import Flask,jsonify,request
import csv

all_movies = []
liked_movies = []
not_liked_movies = []
did_not_watch_movies = []

app = Flask(__name__)

with open('movies.csv') as f:
    reader = csv.reader(f)
    data = list(reader)
    all_movies = data[1:]

@app.route("/get-movie")
def get_movie():
    return jsonify({
        "data" : all_movies[0],
        "status" : "success"
        })

# @app.route("/liked-movies",methods=["POST"])
# def liked_movie():
#     movie = all_movies[0]
#     all_movies = all_movies[1:]
#     liked_movies.append(movie)
#     return jsonify({
#         "status" : "success"
#     }), 201

# @app.route("/unliked-movies",methods=["POST"])
# def liked_movie():
#     movie = all_movies[0]
#     all_movies = all_movies[1:]
#     not_liked_movies.append(movie)
#     return jsonify({
#         "status" : "success"
#     }), 201

# @app.route("/did-not-watch-movies",methods=["POST"])
# def liked_movie():
#     movie = all_movies[0]
#     all_movies = all_movies[1:]
#     did_not_watch_movies.append(movie)
#     return jsonify({
#         "status" : "success"
#     }), 201

if __name__ == "__main__":
    app.run()