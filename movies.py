from flask import Flask, jsonify, request
app = Flask(__name__)
movies = [
        {
            "name": "Spiderman",
            "casts": ["Ana Green","Joshua Moore", "Francis Roles"],
            "genres": ["Drama", "Action"]
        },
            
        {
            "name": "Batman",
            "casts": ["Mammy Miguel","Rose May", "Allan Reyes"],
            "genres": ["SciFi", "Action"]
        },
]
@app.route('/movies', methods=['GET'])
def getMovies():
    return jsonify(movies)

@app.route('/movies', methods=["POST"])
def add_Movie():
    movie = request.get_json()
    movies.append(movie)
    return {'id': len(movies)}, 200

@app.route('/movies/<int:index>', methods=['DELETE'])
def delete_Movie(index):
    movies.pop(index)
    return "Successfully deleted", 200

@app.route('/movies/<int:index>', methods=['PUT'])
def update_Movie(index):
    name = request.json.get("name")
    casts = request.json.get("casts")
    genres = request.json.get("genres")
    movies[index] = {"name":name,"casts":casts,"genres":genres}
    return "Successfully updated", 200

@app.route('/movies/<int:index>', methods=['GET'])
def display_Movie(index):
    return jsonify(movies[index])

@app.route('/movies', methods=['DELETE'])
def delete_all_Movies():
    movies.clear()
    return "Successfully deleted all records", 200

if __name__ == "__main__":
    app.run()