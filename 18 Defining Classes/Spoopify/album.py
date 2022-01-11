class Album:
    def __init__(self, name, *tracks):
        self.name = name
        self.songs = []
        for song in tracks:
            self.songs.append(song)
        self.published = False

    def add_song(self, song_name):
        for song in self.songs:
            if song.name == song_name.name:
                return f"Song is already in the album."
        if self.published:
            return f"Cannot add songs. Album is published."
        elif song_name.single:
            return f"Cannot add {song_name.name}. It's a single"
        else:
            self.songs.append(song_name)
            return f"Song {song_name.name} has been added to the album {self.name}."

    def remove_song(self, song_name):
        if self.published:
            return f"Cannot remove songs. Album is published."
        else:
            for song in self.songs:
                if song_name == song.name:
                    self.songs.remove(song)
                    return f"Removed song {song_name} from album {self.name}."
        return f"Song is not in the album."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."
        else:
            self.published = True
            return f"Album {self.name} has been published."

    def details(self):
        result = f"Album {self.name}\n"
        for song in self.songs:
            result += f"== {song.name} - {song.length}\n"
        return result