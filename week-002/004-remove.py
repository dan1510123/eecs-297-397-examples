#!/usr/local/bin/python3

def print_song(song):
    for i in range(len(song)):
        if i % 8 == 0:
            print()
        print(song[i], end = ' ')
    print()


# Only first occurrence of value is removed

song_words = ["na", "na", "na", "na", "na", "na", "na", "na", \
              "na", "na", "na", "na", "na", "na", "na", "na", \
              "na", "Batman"]   # too many!

print_song(song_words)

song_words.remove("na")

print_song(song_words)
