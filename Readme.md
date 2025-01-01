# Word Frequency Analyzer (Euterpe)

## Overview
This project is a Python-based tool designed to analyze the frequency of specific words or phrases in a collection of song lyrics. Originally inspired by a fixation on 21 Savage’s iconic adlibs, it can be adapted for any artist or text dataset.

---

## Features
- **Word Count Analysis**: Determine how many times a word or phrase appears in the lyrics.
- **Per-Song Breakdown**: Identify the songs with the highest and lowest occurrences of a specific word.
- **Flexible Input**: Works with any properly formatted lyrics file, making it versatile beyond a single artist.
- **Fun Exploration**: Dive into the quirks of your favorite lyrics.

---

## Setup and Usage
### Requirements
- Python 3.6+
- Required libraries: `requests`, `bs4`, `decouple`, `re`, `math`

### Steps to Get Started
1. Clone or download the repository.
2. Install the required libraries:
```bash
pip install requests beautifulsoup4 python-decouple
```
3. Create a `.env` file in the project directory and add your Genius API access token:
```
ACCESS_TOKEN=your_genius_api_access_token
```
4. Run `main.py` to fetch and save the lyrics for the desired artist. Update the `artist_name` variable in the script to match the artist of your choice:
```bash
python3 main.py
```
5. After running the script, you should be left with a `.txt` file containing the lyrics, separated by a "###" delimiter.
6. Run `counter.py` to analyze the word frequency in the lyrics file. Update the `search_word` variable in the script to match the word or phrase you want to analyze:
```bash
python3 counter.py
```
7. View the results, including total word occurrences and song breakdowns.

---

## Why This Project?
This started as a fun way to explore 21 Savage’s lyrical tendencies but quickly evolved into a general-purpose word analysis tool. Whether you’re curious about adlibs, themes, or repetition in any artist’s lyrics,wall of text or even movie scripts this tool has you covered.

---

## Licensing
This project is licensed under the MIT License. Feel free to modify and use it for your own creative explorations.

---

Happy analyzing!

