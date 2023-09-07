"""
You are given a music application's data. Everytime a song is played, an entry is made into
your system (song name and time at which the song is played). At any point when asked,
you have to return top k songs from the given time.
Music player is given with two operations:
- play(String song, Timestamp playedAt)
● It takes two parameters:
○ song = Name of the Song
○ playedAt = When the song was played at (yyyy-MM-dd HH:mm:ss format)

- top(Integer k, Timestamp startTime)
● It takes two parameters:
○ k which is the ask for top k songs
○ startTime: from this time(yyyy-MM-dd HH:mm:ss format, inclusive of this
value) you have to return the song name and the number of times it was
played

● It returns the list of top k songs and their count from startTime
○ In case count is same for multiple songs, include the song which was played
more recently
○ In case count and time are same, return the one coming in later in the play
input

Input format:
For play Operation (all in new line):
play
Song Name (only a-z + space(s))
Played at (yyyy-MM-dd HH:mm:ss format)
For top Operation(all in new line):
top
k (integer: 0 <= k <= 10^6)
startTime (yyyy-MM-dd HH:mm:ss format)

Output format:
(for every input operation: top; output should be given in this format):
song1, count1
song2, count2
...
songk, countk
"""
from collections import defaultdict
from heapq import heappop, heappush

class MusicPlayer:
    def __init__(self):
        self.play_history = []

    def play(self, song, played_at):
        self.play_history.append((played_at, song))

    def top(self, k, start_time):
        song_count = defaultdict(int)
        # Calculate the count of songs played from start_time
        for played_at, song in self.play_history:
            if played_at >= start_time:
                song_count[song] += 1
        # Create a maxHeap to get the top k songs based on count, timestamp, and song name
        # in that order to resolve the tiebreaker as per provided conditions (most recent
        # song to be returned first), we need to multiply with -1 as python's heap module
        # is by default minHeap..
        top_songs = []
        for song, count in song_count.items():
            heappush(top_songs, (-count, played_at, song))
        # Retrieve the top k songs from the heap
        top_k = []
        for _ in range(k):
            if top_songs:
                count, timestamp, song = heappop(top_songs)
                top_k.append((song, -count))

        return top_k


def main():
    music_player = MusicPlayer()

    # Input data
    input_data = [
        ("play", "uptown funk", "2023-08-01 15:17:14"),
        # ("play", "counting stars", "2023-08-10 16:17:14"),
        # ("play", "uptown funk", "2023-08-13 19:13:14"),
        # ("play", "thinking out loud", "2023-08-14 16:17:14"),
        # ("top", 2, "2023-08-01 00:00:00"),
        # ("play", "counting stars", "2023-08-15 15:17:14"),
        ("top", 2, "2023-07-31 15:17:14"),
    ]

    # Process input data
    for item in input_data:
        command = item[0]
        if command == "play":
            song, played_at = item[1], item[2]
            music_player.play(song, played_at)
        elif command == "top":
            # print(music_player.song_data)
            k, start_time = item[1], item[2]
            top_k_songs = music_player.top(k, start_time)
            for song, count in top_k_songs:
                print(f"{song}, {count}")

if __name__ == "__main__":
    main()
