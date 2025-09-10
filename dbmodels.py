from sqlmodel import Field, SQLModel, select, Relationship



class Playlist(SQLModel, table=True):
    __tablename__ = "transcripts_playlist"
    id: int = Field(primary_key=True)
    playlist_id : str = Field(index=True)
    playlist_name : str



class Videos(SQLModel, table=True):
    __tablename__ = "transcripts_video"
    id : int = Field(primary_key=True)
    video_id : str = Field(index=True)
    title : str
    url : str
    transcripted : bool = Field(default=False)
    transcript : list["Transcripts"] = Relationship(back_populates="video")


class Transcripts(SQLModel, table=True):
    __tablename__ = "transcripts_transcript"
    id : int = Field(primary_key=True)
    start_time : float
    text : str
    indexed : bool = Field(default=False)
    video_id : str = Field(foreign_key="transcripts_video.id")
    video : Videos = Relationship(back_populates="transcript")


# response model for Playlists
class PlaylistRead(SQLModel):
    playlist_id : str
    playlist_name : str

# response model for videos
class VideoRead(SQLModel):
    video_id : str
    title : str
    url : str

class TranscriptRead(SQLModel):
    start_time : float
    text : str
