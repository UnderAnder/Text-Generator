from collections import Counter, defaultdict
from random import choices

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

    # make 10 sequence of 10 words
    for _ in range(10):
        # first word
        seq = choices(list(model.keys()))

        for i in range(9):
            weights = [w for _, w in model[seq[i]].most_common()]
            next_word = choices(list(model[seq[i]]), weights)
            seq.extend(next_word)
        print(*seq)


if __name__ == '__main__':
    main()
