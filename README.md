# 🎧 Spotify Music Mood Recommender

## 📌 Project Overview
Spotify Music Mood Recommender is a Python-based application that uses the Spotify Web API to recommend and automatically create playlists based on a user's current mood.

Users simply enter their mood, and the application searches Spotify for relevant playlists, extracts songs, and creates a personalized playlist in their Spotify account.

---

## 🎯 Project Objectives
- Recommend music based on user mood
- Automate Spotify playlist creation
- Learn real-world API usage
- Understand OAuth authentication
- Build a practical Python project

---

## ✨ Features
- 🎵 Mood-based music recommendations
- 🔐 Spotify OAuth authentication
- 🔍 Searches real Spotify playlists
- ➕ Automatically creates private playlists
- 👤 Personalized for each user

---

## 🛠 Technologies Used
- Python 3
- Spotipy (Spotify Web API Wrapper)
- Spotify Developer API
- OAuth 2.0

---

## 🧠 How It Works
1. User logs in using Spotify OAuth
2. User enters a mood (happy, sad, chill, energetic, romantic)
3. The system searches Spotify playlists related to the mood
4. Tracks are extracted from multiple playlists
5. A new private playlist is created
6. Recommended songs are added automatically

---

## 📂 Project Structure
spotify-mood-recommender/
│
├── mood_recommender.py
└── README.md

---

## ▶️ How to Run the Project

### 1️⃣ Install Dependencies
```bash
pip install spotipy
Update Credentials in Code
```
## Create a Spotify Developer App

Visit Spotify Developer Dashboard

Create a new application

Copy Client ID and Client Secret

Set Redirect URI

``` bash
CLIENT_ID = "your_client_id"
CLIENT_SECRET = "your_client_secret"
REDIRECT_URI = "http://127.0.0.1:8888/callback/"
```
## Run
``` bash
python mood_recommender.py
---
```
## Example
``` 
Enter your mood (happy, sad, chill, energetic, romantic): happy
```

Output:
```bash
✅ Logged in as: User Name
🎵 Playlists for mood 'happy'
✅ Playlist 'Happy Vibes' created!
```

---
## ⚠️ Notes

Playlist is created as private

Spotify login popup appears on first run

Do not share your client secret publicly

---

## 🚀 Future Enhancements

AI-based emotion detection

Audio feature analysis

Web interface

Mood history tracking

---

## 📚 Learning Outcomes

API integration

OAuth authentication

Python automation

Spotify API usage

---

## 👩‍💻 Author

Krishna Priya R
B.E Computer Science Engineering
