import spacy
import re


def lemm(sp, item):
    sentence = sp(item)
    l = []
    for word in sentence:
        l.append(str(word.lemma_))
    l = ' '.join(l)
    return l


def stopwords(sp, item):
    stopwords = sp.Defaults.stop_words
    sentence = sp(item)
    l = []
    for word in sentence:
        if word.text not in stopwords:
            l.append(str(word.text))
    l = ' '.join(l)
    return l


def puncuation(item):
    for pun in [',', '.', "'", '"', '-', ':', ";", "/", "{", "}", '[', ']', '#', '%', '&', '*', '(', ')', '@', '!', '~',
                '`', '$', '?', '^', '_', '=', '-']:
        item = item.replace(pun, '')
    return item


def remove_entity(sp, item):
    sentence = sp(item)
    l = []
    for entity in sentence.ents:
        if entity.label_ in (
        'MONEY', 'TIME', 'DATE', 'CARDINAL', 'ORDINAL', 'QUANTITY', 'GPE', 'ORG', 'NORP', 'PERSON', 'FAC', 'LOC',
        'LANGUAGE', 'WORK_OF_ART'):
            l.append(str(entity.text))
    l.append('PRON')
    for x in l:
        item = item.replace(' ' + x + ' ', ' ')
    return item


def remove_spaces(item):
    item = str(re.sub(' +', ' ', item))
    item = " ".join(item.split())
    return item


def removing_non_ascii(item):
    item = item.encode('ascii', 'ignore')
    item = item.decode()
    return item


def to_lower(item):
    item = item.lower()
    return item


def remove_number(item):
    for number in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'PRON']:
        item = item.replace(number, '')
    return item


def remove_alphabat(item):
    for alphabat in [' a ', ' b ', ' c ', ' d ', ' e ', ' f ', ' g ', ' h ', ' i ', ' j ', ' k ', ' l ', ' m ', ' n ',
                     ' o ', ' p ', ' q ', ' r ', ' s ', ' t ', ' u ', ' v ', ' w ', ' x ', ' y ', ' z ']:
        item = item.replace(alphabat, ' ')
    return item


def remove_freq(item, words):
    for word in words:
        item = item.replace(' ' + str(word) + ' ', ' ')
    return item


def main(sp, item):
    item = to_lower(item)
    item = removing_non_ascii(item)
    item = lemm(sp, item)
    item = puncuation(item)
    item = stopwords(sp, item)
    # item = remove_entity(sp, item)
    item = remove_number(item)
    item = remove_spaces(item)
    item = remove_alphabat(item)
    return item