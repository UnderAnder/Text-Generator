from collections import Counter, defaultdict
from random import choices
from re import fullmatch

from nltk.tokenize import WhitespaceTokenizer
from nltk.util import bigrams


def markov_chain(tokens):
    model = defaultdict(Counter)
    for head, tail in bigrams(tokens):
        model[head][tail] += 1

    return model


def corpus_statistic(tokens):
    print('Corpus statistics')
    print('All tokens:', len(tokens))
    print('Unique tokens:', len(set(tokens)))


def main():
    with open(input(), "r", encoding="utf-8") as f:
        tokens = WhitespaceTokenizer().tokenize(f.read())

    model = markov_chain(tokens)
    first_word_pattern = r"[A-Z][\w\d']*"
    end_word_pattern = r"[\S]*[.!?]"

    # make 10 sequence
    for _ in range(10):
        # first capitalized word and don't ends with a sentence-ending punctuation mark
        seq = choices(list(model.keys()))
        while not fullmatch(first_word_pattern, seq[0]):
            seq = choices(list(model.keys()))
        # minimal sentence length 5 tokens, with a sentence-ending punctuation mark
        for i in range(100):
            weights = [w for w in model[seq[i]].values()]
            next_word = choices(list(model[seq[i]]), weights)
            seq.extend(next_word)
            if i > 2 and fullmatch(end_word_pattern, next_word[0]):
                break
        print(*seq)


if __name__ == '__main__':
    main()
