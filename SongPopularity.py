"""
Rank songs given n users and m songs, each user i has preference list,
pref[i] which is a permutation of numbers 0 to m -1, indicating the
user's prefernce for a song. If a < b, the user prefers song
pref[i][a] over song pref[i][b]. To rank the songs, use the apporach
Song x is said to beat song y if song x is preferred over y by more
tha half of the users, if exactly half, id of x is smaller than of y.
Song x is considered more popular than y if it beats more songs than y
if they beat same number of songs, x should be having lower id.
"""
def getPopularityOrder(songsPreferences):
    n = len(songsPreferences)
    m = len(songsPreferences[0])
    def beats(song1, song2):
        count = 0
        for user in songsPreferences:
            if user.index(song1) > user.index(song2):
                count+=1
        return count > n/2 or (count == n/2 and song1 < song2)
    candidate = 0
    count = 1
    for song in range(1, m):
        if count == 0:
            candidate, count = song, 1
        elif beats(candidate, song):
            count+=1
        else:
            count-=1
    songBeats = [(0,0)]*m 
    for song in range(m):
        songBeats[song] = sum((beats(song, otherSong) for otherSong in range(m)), song)
    rankedSongs = sorted(songBeats, key = lambda x:(-x[0], x[1]))
    return [song[1] for song in rankedSongs]