from collections import Counter
from nltk.util import bigrams
from nltk.tokenize import WhitespaceTokenizer


def markov_chain(tokens):
    simple_model = {}
    model = {}

    for head, tail in bigrams(tokens):
        simple_model.setdefault(head, []).append(tail)
    for head, tail in simple_model.items():
        model.setdefault(head, {}).update(Counter(tail))
    return model

def corpus_statistic(tokens):
    print('Corpus statistics')
    print('All tokens:', len(tokens))
    print('Unique tokens:', len(set(tokens)))


def main():
    with open(input(), "r", encoding="utf-8") as f:
        tokens = WhitespaceTokenizer().tokenize(f.read())

    model = markov_chain(tokens)

    while True:
        command = input().strip()
        if command == 'exit':
            exit()
        try:
            print('Head:', command)
            print('\n'.join(f'Tail: {w} Count: {c}' for w, c in model[command].items()))
        except (TypeError, ValueError):
            print('Type Error. Please input an integer.')
        except IndexError:
            print('Index Error. Please input an integer that is in the range of the corpus.')
        except (KeyError, AttributeError):
            print('The requested word is not in the model. Please input another word.')
        else:
            continue


if __name__ == '__main__':
    main()
