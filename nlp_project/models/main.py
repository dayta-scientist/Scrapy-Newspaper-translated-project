import pandas as pd
import numpy as np
from googletrans import Translator, constants
# init the Google API translator
translator = Translator()
# pip install googletrans==3.1.0a0

def main():
    df = read_data()
    df = extract_title(df)
    df = clean_body(df)
    df = translate_body(df)
    df = tokenize_English_body(df)
    df = df_to_csv(df)
    





def read_data():
    df = pd.read_csv("../data/quotes.csv")

    return df


def extract_title(df):
    title = df["url"].apply(lambda x: x.split('/')[-1])

    title = title.apply(lambda x: x.replace('-', ' '))

    title = title.apply(lambda x: x.capitalize())

    df["title"] = title

    return df


def clean_body(df):
    df["body"] = df["body"].replace(to_replace ='(\.,)', value = '. ', regex = True) 

    return df


def translate_body(df):
    df['English_body'] = df["body"].apply(translator.translate, src='es', dest='en').apply(getattr, args=('text',))

    return df


def tokenize_English_body(df):
    import nltk
    nltk.download('punkt')
    nltk.download('averaged_perceptron_tagger')
    from nltk import word_tokenize
    df['tokens'] = df['English_body'].apply(lambda x: word_tokenize(x))

    return df


def df_to_csv(df):
    df.to_csv('df.csv')




if __name__ == '__main__':
    main()
