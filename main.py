import requests
from bs4 import BeautifulSoup
from decouple import config
import os

# Load Genius API token
ACCESS_TOKEN = config("ACCESS_TOKEN", default=None)

# Genius API base URL
BASE_URL = "https://api.genius.com"

def get_artist_id(artist_name):
    """
    Fetch the Genius artist ID for a given artist name.
    """
    headers = {"Authorization": f"Bearer {ACCESS_TOKEN}"}
    search_url = f"{BASE_URL}/search"
    params = {"q": artist_name}

    response = requests.get(search_url, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()
        for hit in data["response"]["hits"]:
            if hit["result"]["primary_artist"]["name"].lower() == artist_name.lower():
                return hit["result"]["primary_artist"]["id"]
    else:
        print(f"Error: {response.status_code} - {response.text}")
    return None

def fetch_artist_songs(artist_id, max_songs=100):
    """
    Fetch all songs for a given artist using the Genius API artist ID.
    """
    headers = {"Authorization": f"Bearer {ACCESS_TOKEN}"}
    songs_url = f"{BASE_URL}/artists/{artist_id}/songs"
    params = {"per_page": 50, "page": 1}
    
    songs = []
    while len(songs) < max_songs:
        response = requests.get(songs_url, headers=headers, params=params)
        if response.status_code == 200:
            data = response.json()
            for song in data["response"]["songs"]:
                song_title = song["title"]
                lyrics_url = song["url"]
                songs.append((song_title, lyrics_url))
                
                if len(songs) >= max_songs:
                    break

            if not data["response"]["songs"]:
                break
            
            params["page"] += 1
        else:
            print(f"Error: {response.status_code} - {response.text}")
            break
    
    return songs

def fetch_lyrics(song_url):
    """
    Fetch song lyrics from a Genius song URL by scraping the HTML.
    """
    response = requests.get(song_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Find the lyrics section
        lyrics_div = soup.find("div", class_="lyrics")  # Old Genius layout
        if not lyrics_div:
            # For the newer Genius layout
            lyrics_div = soup.find("div", {"data-lyrics-container": "true"})
        
        if lyrics_div:
            return lyrics_div.get_text(separator="\n").strip()
        else:
            print(f"Lyrics not found on page: {song_url}")
            return None
    else:
        print(f"Error fetching lyrics: {response.status_code} - {response.text}")
        return None

def save_lyrics(artist_name, songs_with_lyrics, output_file="all_lyrics.txt"):
    """
    Save all lyrics from an artist into a single text file.
    
    :param artist_name: Name of the artist.
    :param songs_with_lyrics: A list of tuples containing song titles and their lyrics.
    :param output_file: The file to save all the lyrics to.
    """
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(f"Lyrics Collection for {artist_name}\n")
        f.write("=" * 50 + "\n\n")
        
        for song_title, lyrics in songs_with_lyrics:
            f.write(f"### {song_title} ###\n")
            f.write(lyrics)
            f.write("\n\n")
    
    print(f"All lyrics saved to: {output_file}")

# Example usage
artist_name = "Kendrick Lamar"
artist_id = get_artist_id(artist_name)
if artist_id:
    print(f"Fetching songs for artist ID: {artist_id}")
    songs = fetch_artist_songs(artist_id, max_songs=100)  # Adjust max_songs as needed
    print(f"Found {len(songs)} songs by {artist_name}.")
    
    all_lyrics = []
    for title, url in songs:
        print(f"Fetching lyrics for: {title}")
        lyrics = fetch_lyrics(url)
        if lyrics:
            all_lyrics.append((title, lyrics))
    
    # Save all lyrics to a single file
    save_lyrics(artist_name, all_lyrics, output_file=f"{artist_name.replace(' ', '_')}_lyrics.txt")
else:
    print("Artist not found.")
