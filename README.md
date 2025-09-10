

# 🎓 CS50P Capstone: YouTube Video Transcript API

This project is a FastAPI-based web service for serving transcripts, playlists, and video metadata from CS50 YouTube videos. It is designed as a capstone project for CS50P.

## ✨ Features

- **REST API Endpoints**:
	- 📋 List all playlists (`/api/playlists`)
	- 🎬 List all videos (`/api/videos`)
	- 📝 Fetch transcripts by video ID (`/api/videos/{videoid}`)
	- 📝 Fetch transcripts by video title (`/api/videotitle/{videotitle}`)
- **HTML Documentation** at `/api` root endpoint
- **SQLite Database** for persistent storage
- **ORM Models** using SQLModel for Playlists, Videos, and Transcripts

## 🏗️ Architecture

- `project.py`: FastAPI app, endpoint definitions, and server startup
- `dbmodels.py`: SQLModel ORM classes and response schemas
- `database.py`: Database engine setup and session management
- `db.sqlite3`: SQLite database file

### 🗂️ Data Model

- **Playlist**: Stores playlist ID and name
- **Videos**: Stores video ID, title, URL, transcript status, and links to transcripts
- **Transcripts**: Stores transcript text, start time, and links to videos

## 🚀 Getting Started

1. 🐍 **Install Python 3.11+**
2. 📦 **Install dependencies:**
	 ```
	 pip install -r requirements.txt
	 ```
3. ▶️ **Start the API server:**
	 ```
	 python project.py
	 ```
4. 🌐 **Access the API:**
	 [http://127.0.0.1:8000/api](http://127.0.0.1:8000/api)

## 🧪 Testing

- Run tests with pytest or your preferred test runner. Example test file: `test_project.py`.

## 📚 Usage Example

- To get all playlists:
	```
	GET /api/playlists
	```
- To get transcripts for a video by ID:
	```
	GET /api/videos/{videoid}
	```
