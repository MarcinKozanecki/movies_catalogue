import requests

API_TOKEN = "e1895c9c27ab079b2254dcedb85e65b6"

# Funkcja do pobierania filmów z listy na podstawie typu (np. popular)
def get_movies_list(list_type="popular"):
    endpoint = f"https://api.themoviedb.org/3/movie/{list_type}?api_key=e1895c9c27ab079b2254dcedb85e65b6"
    response = requests.get(endpoint)
    response.raise_for_status()  
    return response.json()

# Funkcja do pobierania filmów, która akceptuje argument `list_type`
def get_movies(how_many, list_type="popular"):
    data = get_movies_list(list_type)
    return data["results"][:how_many]

# Funkcja do pobierania pojedynczego filmu
def get_single_movie(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=e1895c9c27ab079b2254dcedb85e65b6"
    response = requests.get(endpoint)

    if response.status_code != 200:
        print(f"Error fetching movie details: {response.text}")

    return response.json()

# Funkcja do pobierania obsady filmu
def get_movie_cast(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key=e1895c9c27ab079b2254dcedb85e65b6"
    response = requests.get(endpoint)
    if response.status_code != 200:
        return []
    data = response.json()
    return data.get("cast", [])[:8]

def get_poster_url(path, size):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}{path}"
