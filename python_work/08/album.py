def make_album(singer, album_name, number=None):
    album = {}
    if number:
        album['singer'] = f"{singer}"
        album['album_name'] = f"{album_name}"
        album['number'] = number
    else:
        album['singer'] = f"{singer}"
        album['album_name'] = f"{album_name}"

    return album

album = make_album("Yanni", "In the mirror", 8)
for key, value in album.items():
    print(f"{key}: {value}")
