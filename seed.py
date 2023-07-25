from app import app
from models import db, Playlist, Song, PlaylistSong

app.app_context().push()

db.drop_all()
db.create_all()

p1 = Playlist(
    name="Beach Playlist",
    description="Good Beach Vibes"
)

s1 = Song(
    title="Three Little Birds",
    artist="Bob Marley"
)

s2 = Song(
    title="Owl Song",
    artist="Of The Trees"
)

db.session.add(p1)
db.session.add_all([s1, s2])
db.session.commit()