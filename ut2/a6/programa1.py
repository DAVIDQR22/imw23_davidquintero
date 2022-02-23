import sys


def count_words(sentence):
    summary = {}
    docket = sentence.split()
    for a_word in docket:
        summary[a_word] = 0
        for b_word in docket:
            if a_word == b_word:
                summary[a_word] += 1
    return summary


if __name__ == '__main__':
    sentence = sys.argv[1]
    report = count_words(sentence)
    for word, count in report.items():
        print(f'{word}: {count}')
