from albums_list_tuple import albums

SONG_LIST_TRACK = 3
SONG_TRACK = 1

music = input("Do you wan to hear the music")
while music.lower() == "yes":
    print("Choose the movie you want to hear:")
    for index, album in enumerate(albums):
        title, artistry, year, songs = album
        print("{} : {}".format(index + 1, title))
    movie = int(input("Choose the song you want to hear:"))
    if 1 <= movie <= len(albums):
        songs_list = albums[movie - 1][SONG_LIST_TRACK]
        for song_list in songs_list:
            track_no, song = song_list
            print("{} : {}".format(track_no, song))
        play = int(input(""))
        if 1 <= play <= len(songs_list):
            print("Playing {}".format(songs_list[play - 1][SONG_TRACK]))
        print("=" * 20);


    else:
        print("Invalid movie");
        break;
