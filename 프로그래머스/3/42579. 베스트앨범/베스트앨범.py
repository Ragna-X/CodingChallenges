def solution(genres, plays):
    genres_count_by_play = {}
    for genre, play in zip(genres, plays):
        if genre in genres_count_by_play:
            genres_count_by_play[genre] += play
        else:
            genres_count_by_play[genre] = play
    
    music_count_by_genre = {}
    for idx, (genre, play) in enumerate(zip(genres, plays)):
        if genre in music_count_by_genre:
            music_count_by_genre[genre].append((idx, play))
        else:
            music_count_by_genre[genre] = [(idx, play)]
    
    for genre in music_count_by_genre:
        music_count_by_genre[genre].sort(key=lambda x: (-x[1], x[0]))

    best_album = []
    for genre in sorted(genres_count_by_play, key=lambda x: genres_count_by_play[x], reverse=True):
        best_album.extend([idx for idx, _ in music_count_by_genre[genre][:2]])
    
    return best_album