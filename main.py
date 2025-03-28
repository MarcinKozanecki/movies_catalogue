from flask import Flask, render_template, request  # Upewnij się, że 'request' jest zaimportowane
import tmdb_client

app = Flask(__name__)

@app.context_processor
def utility_processor():
    def tmdb_image_url(path, size):
        return f"https://image.tmdb.org/t/p/{size}{path}" if path else ""
    return {"tmdb_image_url": tmdb_image_url}

@app.route('/')
def homepage():
    selected_list = request.args.get('list_type', 'popular')  # Pobieranie parametru 'list_type' z URL
    print(f"Selected list: {selected_list}")  # Debugowanie wybranej listy
    movies = tmdb_client.get_movies(how_many=8, list_type=selected_list)  # Przekazywanie 'list_type' do funkcji
    return render_template("homepage.html", movies=movies, current_list=selected_list)

@app.route("/movie/<movie_id>")
def movie_details(movie_id):
    details = tmdb_client.get_single_movie(movie_id)
    cast = tmdb_client.get_movie_cast(movie_id) 
    return render_template("movie_details.html", movie=details, cast=cast)

if __name__ == "__main__":
    app.run(debug=True)
