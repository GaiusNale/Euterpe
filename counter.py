import re
import math

def load_lyrics(lyrics_file):
    """
    Load lyrics from the specified text file.
    """
    try:
        with open(lyrics_file, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: The file {lyrics_file} was not found.")
        return None

def count_words_in_song(song_lyrics, word):
    """
    Count the occurrences of a word in a single song's lyrics.
    """
    song_lyrics = song_lyrics.lower()
    word = word.lower()
    pattern = re.escape(word)
    matches = re.findall(pattern, song_lyrics)
    return len(matches)

def calculate_standard_deviation(counts, average):
    """
    Calculate the standard deviation of word occurrences.
    """
    if len(counts) <= 1:
        return 0  # Avoid division by zero when there's only one song
    variance = sum((x - average) ** 2 for x in counts) / len(counts)
    return math.sqrt(variance)

def word_frequency(lyrics_file, word):
    """
    Analyze the frequency of a word in the lyrics file and provide detailed analytics.
    """
    lyrics = load_lyrics(lyrics_file)
    if lyrics:
        # Split lyrics into individual songs
        songs = lyrics.split("###")[1:]  # Skip the first split part, which is the header
        song_counts = []
        total_count = 0
        songs_with_word = 0

        for song in songs:
            song_title = song.split("\n")[0].strip()
            song_lyrics = "\n".join(song.split("\n")[1:]).strip()
            count = count_words_in_song(song_lyrics, word)
            song_counts.append((song_title, count))
            total_count += count
            if count > 0:
                songs_with_word += 1

        # Calculate statistics
        average_count = total_count / len(song_counts) if song_counts else 0

        # Find the song with the most occurrences
        most_frequent_song = None
        max_count = -1
        for song_title, count in song_counts:
            if count > max_count:
                most_frequent_song = (song_title, count)
                max_count = count

        # Find the song with the least occurrences (ignoring zero counts)
        least_frequent_song = None
        min_count = float('inf')
        for song_title, count in song_counts:
            if 0 < count < min_count:
                least_frequent_song = (song_title, count)
                min_count = count

        percentage_songs_with_word = (songs_with_word / len(song_counts) * 100) if song_counts else 0
        counts = [count for _, count in song_counts]
        std_deviation = calculate_standard_deviation(counts, average_count) if song_counts else 0

        # Print results
        print(f"The word/phrase '{word}' appears {total_count} times in total.")
        print(f"Average occurrences per song: {average_count:.2f}")
        if most_frequent_song:
            print(f"The song with the most occurences has {most_frequent_song[1]} occurrences.")
        else:
            print("No song has the most occurrences.")
        if least_frequent_song:
            print(f"The song with the least occurrences has {least_frequent_song[1]} occurrences.")
        else:
            print("No song qualifies for the least occurrences.")
        print(f"Percentage of songs containing the word: {percentage_songs_with_word:.2f}%")
        print(f"Standard deviation of occurrences: {std_deviation:.2f}")

if __name__ == "__main__":
    # Update this to match your lyrics file
    lyrics_file = ""
    # Word or phrase to search for
    search_word = ""
    word_frequency(lyrics_file, search_word)
