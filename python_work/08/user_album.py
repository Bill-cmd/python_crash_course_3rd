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
while True:
    prompt_singer = "\nPlease enter the singer, enter 'q' to quit: "
    prompt_album_name = "\nPlease enter the album_name, enter 'q' to quit: "
    prompt_album_number = "\nPlease enter the album_number, enter 'q' to quit: "

    singer = input(prompt_singer)
    if singer.lower() == 'q':
        break

    album_name = input(prompt_album_name)
    if album_name.lower() == 'q':
        break

    album_number = input(prompt_album_number)
    if album_number.lower() == 'q':
        break

    album = make_album(singer, album_name, album_number)
    for key, value in album.items():
        print(f"{key}: {value}")
    
