from fastapi import FastAPI
from dbmodels import Playlist, PlaylistRead, Videos, VideoRead
from database import SessionDep, create_db_and_tables
from sqlmodel import select


app = FastAPI()
create_db_and_tables()


@app.get("/api")
def root():

    return {"something" : "in the way"} 

 
 # returns list of playlists
@app.get("/api/playlists", response_model=list[PlaylistRead])
def playlists(session : SessionDep) -> list:
    
    playlists : list = session.exec(select(Playlist)).all()
    return playlists

# returns video name and id
@app.get("/api/videos", response_model=list[VideoRead])
def videos(session : SessionDep):
    videos : list = session.exec(select(Videos)).all()
    print("videos", videos)
    return videos

# returns full transcripts
# TODO only return time and text or just text
@app.get("/api/videos/{videoid}")
def transcripts(videoid : str, session : SessionDep):
    print(videoid)
    video = session.exec(select(Videos).where(Videos.video_id == videoid)).first()
    return video.transcript
