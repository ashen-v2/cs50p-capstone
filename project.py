from fastapi import FastAPI
from fastapi import HTTPException
from fastapi.responses import HTMLResponse
from http import HTTPStatus
from dbmodels import Playlist, PlaylistRead, Videos, VideoRead, TranscriptRead, Transcripts
from database import SessionDep, create_db_and_tables
from sqlmodel import select


HTML_DOC = """
<!DOCTYPE html>
<html>
<head>
    <title>CS50 YTVideo Transcript API</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; line-height: 1.6; }
        h1 { color: #333; }
        h2 { margin-top: 30px; }
        code { background: #f4f4f4; padding: 2px 6px; border-radius: 4px; }
        .endpoint { margin-bottom: 15px; }
    </style>
</head>
<body>
    <h1>📺 CS50 YTVideo Transcript API</h1>
    <p>This API allows you to fetch playlists, videos, and transcripts from 
    the CS50 video transcripts database.</p>

    <h2>Endpoints</h2>
    
    <div class="endpoint">
        <b>Root:</b><br>
        <code>GET /api</code><br>
        Returns a simple HTML Documentation response.
    </div>

    <div class="endpoint">
        <b>Playlists:</b><br>
        <code>GET /api/playlists</code><br>
        Returns a list of all playlists. limit 50.\n
        adjust <code>?skip=0&limit=50</code> to adjust output 
    </div>

    <div class="endpoint">
        <b>Videos:</b><br>
        <code>GET /api/videos</code><br>
        Returns a list of all videos (id + name). limit 100.\n
        adjust <code>?skip=0&limit=100</code> to adjust output 
    </div>

    <div class="endpoint">
        <b>Transcripts by Video ID:</b><br>
        <code>GET /api/videos/{videoid}</code><br>
        Returns the transcript for the given video ID.
    </div>

    <div class="endpoint">
        <b>Transcripts by Video Title:</b><br>
        <code>GET /api/videotitle/{videotitle}</code><br>
        Returns the transcript for the given video title.
    </div>

    <hr>
    <p><i>Built with FastAPI 🚀 For CS50P Final Project</i></p>
    <p>GitHub 👾 <a href="https://github.com/ashen-v2">ashen-v2</a></p>
</body>
</html>
"""


def get_playlists(session : SessionDep, skip : int, limit : int) -> list:
    
    playlists : list = session.exec(select(Playlist).limit(limit).offset(skip)).all()
    return playlists

def get_videos(session : SessionDep, skip : int, limit : int):
        videos : list = session.exec(select(Videos).limit(limit).offset(skip)).all()
        return videos

def get_transcripts(videoid : str, session : SessionDep):
    video = session.exec(select(Videos).where(Videos.video_id == videoid)).first()

    if video == None:
        raise(HTTPException(status_code=404, detail="Invalid Video id"))
    # transcripts = video.transcript
    transcripts = session.exec(select(Transcripts).where(Transcripts.video_id == videoid)).all()
    return transcripts

def get_transcripts_byname(videotitle : str, session : SessionDep):
    video = session.exec(select(Videos).where(Videos.title == videotitle)).first()

    if video == None:
        raise(HTTPException(status_code=404, detail="Invalid Video title"))
    videoid = Videos.video_id
    # transcripts = video.transcript
    transcripts = session.exec(select(Transcripts).where(Transcripts.video_id == videoid)).all()
    return transcripts


def create_app():
    app = FastAPI()
    create_db_and_tables()


    @app.get("/api" ,response_class=HTMLResponse  ,status_code=HTTPStatus.OK)
    def root():
        return HTML_DOC

    
    # returns list of playlists
    @app.get("/api/playlists", response_model=list[PlaylistRead],  status_code=HTTPStatus.OK)
    def playlists(session : SessionDep, skip : int = 0, limit : int = 50) -> list:
        return get_playlists(session, skip, limit)
        

    # returns video name and id
    @app.get("/api/videos", response_model=list[VideoRead],  status_code=HTTPStatus.OK)
    def videos(session : SessionDep, skip : int = 0, limit : int = 100):
        return get_videos(session, skip, limit)

    # returns full transcripts
    @app.get("/api/videos/{videoid}", response_model=list[TranscriptRead], status_code=HTTPStatus.OK)
    def transcripts(videoid : str, session : SessionDep):
        return get_transcripts(videoid, session)
    
    # returns transcript by videotitle
    @app.get("/api/videotitle/{videotitle}", response_model=list[TranscriptRead], status_code=HTTPStatus.OK)
    def transcripts_byname(videotitle : str, session : SessionDep):
        return get_transcripts_byname(videotitle, session)

    return app

def main():
    import uvicorn
    app = create_app()
    uvicorn.run(app, host="127.0.0.1", port=8000,) 


if __name__ == "__main__":
    main()
