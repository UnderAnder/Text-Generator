from nltk.tokenize import WhitespaceTokenizer

def main():
    tokens = []
    with open(input(), "r", encoding="utf-8") as f:
        for line in f:
            tokens.extend(WhitespaceTokenizer().tokenize(line))
    print('Corpus statistics')
    print('All tokens:', len(tokens))
    print('Unique tokens:', len(set(tokens)))

    while True:
        command = input()
        if command == 'exit':
            exit()
        try:
            print(tokens[int(command)])
        except TypeError:
            print('Type Error. Please input an integer.')
        except IndexError:
            print('Index Error. Please input an integer that is in the range of the corpus.')
        except ValueError:
            print('Type Error.')
        else:
            continue


if __name__ == '__main__':
    main()
