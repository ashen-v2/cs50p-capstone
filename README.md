

# 🎓 CS50P Capstone: CS50 YouTube Video Transcript API

This project is a web API for returning transcripts, playlists, and video metadata from a database that contains transcripts of videos in CS50 youtube channel. It is designed as a capstone project for CS50P made using FastAPI.

## ✨ Features

- **REST API Endpoints**:
		- 📋 List all playlists (`/api/playlists`) with pagination: `?skip=0&limit=50`
		- 🎬 List all videos (`/api/videos`) with pagination: `?skip=0&limit=100`
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

- **Playlist**: includes playlist ID and name
- **Videos**: includes video ID, title, URL, transcript status, and links to transcripts
- **Transcripts**: includes transcript text, start time, and links to videos

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
	 http://127.0.0.1:8000/api - use Postman or web Browser
     (Web browser recommended for this specific endpoint to view the documentation)

## 🧪 Testing

- Run tests with pytest or your preferred test runner. Example test file: `test_project.py`.
- tests has written with pytest in mind


## 📚 Usage Example

- To get all playlists (default limit 50, use skip/limit for pagination):
	```
	GET /api/playlists?skip=0&limit=20
	```
- To get all videos (default limit 100, use skip/limit for pagination):
	```
	GET /api/videos?skip=0&limit=20
	```
- To get transcripts for a video by ID:
	```
	GET /api/videos/{videoid}
	```
## Note

Data in db_example.sqlite3 just data of one video for demonstration purposes
reach out to me if you in need of complete database 
