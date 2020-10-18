import csv
import re
symbols = 0
spaces = 0
punctuation_symbols = 0
words = 0
sentences = 0
with open('steam_description_data.csv', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        strings = ','.join(row)
        symbols += len(strings)
        spaces += strings.count(' ')
        punctuation_symbols += strings.count(',') + strings.count('.') + strings.count('?') + strings.count('!')
        punctuation_symbols += strings.count('\"') + strings.count('+"') + strings.count('\"') + strings.count(':') + strings.count(';')
        punctuation_symbols += strings.count('-') + strings.count('(') + strings.count(')')
        words += len(re.findall(r"(\w+'\w+)|(\w+-\w+'\w+)|(\w+-\w+'\w)|\w+", strings))
        sentences += len(re.findall(r"([A-Z][^.!?]*[.!?])", strings))
print("Количество символов (общее):", symbols)
print("Количество символов (без пробелов):", symbols - spaces)
print("Количество символов (без знаков препинания):", symbols - punctuation_symbols)
print("Количество слов:", words)
print("Количество предложений:", sentences)