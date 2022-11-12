#pip install pymusixmatch
from musixmatch import Musixmatch
#pip install vaderSentiment
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd

musixmatch_api_key = "95f7e1aa1421c9807a18a2abdef5ce6e"
# Musixmatch API
musixmatch_machine = Musixmatch(musixmatch_api_key)

analyser = SentimentIntensityAnalyzer()

playlist_df= pd.read_csv("my_playlist.csv")

lyric_list = []
sentiment_list = []
sentiment_score_list = []

for track0 in playlist_df[['artist_name','track_name']].values:


    try:
        song = musixmatch_machine.matcher_lyrics_get(track0[0], track0[1])
        song = song['message']['body']['lyrics']['lyrics_body']
        sentiment_score = analyser.polarity_scores(song)

        if sentiment_score['compound'] >= 0.05:
            sentiment_percentage = sentiment_score['compound']
            sentiment = 'Positive'
        elif sentiment_score['compound'] > -0.05 and sentiment_score['compound'] < 0.05:
            sentiment_percentage = sentiment_score['compound']
            sentiment = 'Neutral'
        elif sentiment_score['compound'] <= -0.05:
            sentiment_percentage = sentiment_score['compound']
            sentiment = 'Negative'

        sentiment_list.append(sentiment)
        sentiment_score_list.append((abs(sentiment_percentage) * 100))

    except:
        sentiment_list.append('None')
        sentiment_score_list.append(0)
    lyric_list.append(song)
playlist_df['lyric'] = lyric_list
playlist_df['sentiment'] = sentiment_list
playlist_df['sentiment_score'] = sentiment_score_list
playlist_df.to_csv('my_playlist_sentiment1.csv',header=True, index=False)