import string
import nltk
import csv
from nltk import word_tokenize
def clean_data(text, stopword_removal=True, stopwords_domain=[], lower_case=True,
                       punctuation_removal=True):

    processed_tokens = word_tokenize(text)

    if stopword_removal:
        stopwords = [x.lower() for x in nltk.corpus.stopwords.words('english')]
        domain_stopwords = [x.lower() for x in stopwords_domain]
        processed_tokens = [word for word in processed_tokens if word.lower() not in domain_stopwords + stopwords]

    if punctuation_removal:
        processed_tokens = [word for word in processed_tokens if word not in string.punctuation]

    if lower_case:
        processed_tokens = [word.lower() for word in processed_tokens]
    else:
        processed_tokens = [word for word in processed_tokens]

    return processed_tokens



def find_stop_words(all_text : list[str], dictionary: dict, num_token=30):
    dictionary = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)
    stop_words = {}
    for i in range(0, num_token):
        stop_words[dictionary[i][0]] = dictionary[i][1]
    return stop_words



##### Indexing


def get_posting_for_one_doc(tokens):
    posting = {}
    position = 0
    for token in tokens:
        if posting.__contains__(token):
            posting.get(token).append(position)
        else:
            posting[token] = [position]
        position += 1
    return posting


def construct_positional_indexes(corpus : list):
    for item in corpus:

        for word, posting in get_posting_for_one_doc(item["abs_token"]).items():
            if list_of_stop_words.__contains__(word):
                continue
            if not positional_indices.__contains__(word):
                positional_indices[word] = [[], []]
            positional_indices.get(word)[1].append([item["id"], posting])

        for word, posting in get_posting_for_one_doc(item["title_token"]).items():
            if not positional_indices.__contains__(word):
                positional_indices[word] = [[], []]
            positional_indices.get(word)[0].append([item["id"], posting])
    return positional_indices
