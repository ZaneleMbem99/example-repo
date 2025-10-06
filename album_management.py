import copy


class Album:

    def __init__(self, name, artist_name, num_of_songs):
        self.name = name
        self.num_of_songs = num_of_songs
        self.artist_name = artist_name

    def __str__(self):
        return f"Album: {self.name} by {self.artist_name}, {len(self.num_of_songs)} songs"


albums1 = []
albums1.append(Album("Setup", "Chris", ["seek", "sensation", "kisses", "heaven", "mind"]))
albums1.append(Album("Zans", "Zanele", ["26", "element", "mother", ]))
albums1.append(Album("Inlove", "Odz", ["Desire", "The 40s"]))
albums1.append(Album("Currently", "Micah", ["sadness", "Gqom", "Queens", "Xhosa"]))
albums1.append(Album("13", "Zizo", ["Mnike", "Umshunqo", "Sika"]))

print("before sorting")
for album in albums1:
    print(album)

albums1.sort(key=lambda a: len(a.num_of_songs))
print("\nAfter sorting by number of songs:")
for album in albums1:
    print(album)

albums1[0], albums1[1] = albums1[1], albums1[0]
print("\nAfter swapping elements 1 and 2 in albums1:")
for album in albums1:
    print(album)

albums2 = []
albums2.append(Album("Set", "Denvile", ["ow", "Nick", "needs", "problems", "ask"]))
albums2.append(Album("Alie", "Niyaaz", ["Sick", "pat", "math", ]))
albums2.append(Album("easy", "Luba", ["breath", "try"]))
albums2.append(Album("can", "Sam", ["divide", "super", "people", "Ink"]))
albums2.append(Album("All", "Tyla", ["abantwan", "skorokoro", "keeps"]))

print("\nBefore adding other albums:")
for album in albums2:
    print(album)

albums2 = copy.deepcopy(albums1)
print("\nAlbums2 after copying:")
for album in albums2:
    print(album)

album6_songs = [f"Song {i+1}" for i in range(9)]
album7_songs = [f"Song {i+1}" for i in range(16)]

albums2.append(Album("Dark Side of the Moon", "Pink Floyd", album6_songs))
albums2.append(Album("OOPS!...I Did is Again", "Britney Spears", album7_songs))

albums2.sort(key=lambda a: a.name)
print("\nalbums2 sorted alphabetically")
for album in enumerate(albums2):
    print(album)

search_name = "Dark Side of the Moon"
found_index = -1

for i, album in enumerate(albums2):
    if album.name == search_name:
        found_index = i
        break
print("\nsearch results: ")
if found_index != -1:
    print(f"{search_name} found at index {found_index}")
else:
    print(f"'{search_name}' not found in albums2 ")
