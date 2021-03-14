from nltk.util import bigrams
from nltk.tokenize import WhitespaceTokenizer


def corpus_statistic(tokens):
    print('Corpus statistics')
    print('All tokens:', len(tokens))
    print('Unique tokens:', len(set(tokens)))


def main():
    with open(input(), "r", encoding="utf-8") as f:
        tokens = WhitespaceTokenizer().tokenize(f.read())

    bigrams_list = list(bigrams(tokens))
    print('Number of bigrams:', len(bigrams_list))

    while True:
        command = input().strip().lower()
        if command == 'exit':
            exit()
        try:
            print(f'Head: {bigrams_list[int(command)][0]} \t Tail: {bigrams_list[int(command)][1]}')
        except (TypeError, ValueError):
            print('Typ Error. Please input an integer.')
        except IndexError:
            print('Index Error. Please input an integer that is in the range of the corpus.')
        else:
            continue


if __name__ == '__main__':
    main()
