import os
import requests
from dotenv import load_dotenv


def fetch_data(title):
    """
    Fetch movie data for a given title.
    Return a dictionary with movie details.
    Return an empty dictionary if the movie is not found or an error occurs.
    """
    load_dotenv()
    API_KEY = os.getenv('API_KEY')

    if not API_KEY:
        raise ValueError(
        "API_KEY not found. Please add your API key to the .env file."
        )

    url = f"http://www.omdbapi.com/?apikey={API_KEY}&t={title}"
    try:
        data = requests.get(url).json()
    except requests.exceptions.RequestException:
        print("No connection to the API. Try again later.")
        return {}
    #response means movie not found
    if data.get("Error"):
        print(f'Movie "{title}" not found in API database.')
        return {}

    return data
