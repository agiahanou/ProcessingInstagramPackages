import emoji
import regex
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
import re
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import time


class sentiment:
    lst = []
    analyzer = SentimentIntensityAnalyzer()
    sleepTime = 10

    def __init__(self):

        all_emojis = list(emoji.UNICODE_EMOJI.keys())

    def VADER(self,singleText):
        vaderScores = self.analyzer.polarity_scores(singleText)
        return([vaderScores['pos'], vaderScores['neu'], vaderScores['neg'], vaderScores['compound']])

    def one_vector_sentiment(self, sentences):

        for sentence in sentences:
            global_vec = []
            global_vec.append(sentence)
            global_vec.extend(self.VADER(sentence))

            # sleep time to avoid API access errors
            time.sleep(self.sleepTime)
            self.lst.append(global_vec)

        df = pd.DataFrame(self.lst, columns =['text', 'Vpos', 'Vneut', 'Vneg', 'Vcompound'])

        return df

if __name__ == '__main__':
    df = pd.read_csv('outputFiles/mediaPhotos.csv')
    df = pd.Series(df["texts"])
    sentDF = sentiment()

    dfTextual = sentDF.one_vector_sentiment(df)

    dfTextual.to_csv('mediaPhotosSentiment2.csv')

