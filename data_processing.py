import pandas as pd
from sklearn.model_selection import train_test_split
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
import clean_data as cd
import spacy
def processing_data(file_name):
    dataset = pd.read_csv(file_name)
    dataset = dataset[(dataset['label_num'] == 0) | (dataset['label_num'] == 1)]
    X=[]
    spacy.prefer_gpu()
    sp = spacy.load("en_core_web_sm")

    for x in dataset['text'].values:
        X.append(cd.main(sp, x))
    y = dataset["label_num"].values

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.05, random_state=42)

    tokenizer = Tokenizer(num_words=5000)
    tokenizer.fit_on_texts(X_train)

    X_train = tokenizer.texts_to_sequences(X_train)
    X_test = tokenizer.texts_to_sequences(X_test)
    print(len(X_train))
    print(len(X_test))
    vocab_size = 10000
    maxlen = 500

    x_train = pad_sequences(X_train, padding='post', maxlen=maxlen)
    x_test = pad_sequences(X_test, padding='post', maxlen=maxlen)
    print('Data Processing Complete ... !')
    return x_train,x_test, y_train, y_test, maxlen,vocab_size
