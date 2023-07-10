from zipfile import ZipFile
import os

EXCEPT_WORLDS = ['pun', 'w', 'cat', 'get', 'had', 'say', 'red', 'off', 'obj', 'own', 'yes', 'due', 'arg', 'kw', 'api',
                 'd', 'sum', 'str', 'ham', 'pi', 'job', 'via', 'z', 'old', 'tic', 'tac', 'toe', 'bit', 'let', 'int',
                 'var', 'how', 'top', 'did', 'saw', 'u', 'num', 'put', 'add', 'f', 'ok', 'was', 'row', 'y', 'pep',
                 'now', 'fib', 'l', 'got', 'vec', 't', 'v', 'out', 'n', 'try', 'odd', 'tel', 'c', 'its', 'way', 'up',
                 'do', 'end', 'set', 'key', 'has', 'i', 'one', 'see', 'del', 'new', 'any', 'so', 'we', 'two', 'no', 'b',
                 'at', 'but', 'all', 'may', 'x', 'on', 'def', 'use', 'not', 'you', 'by', 'can', 'as', 'it', 'an', 'if',
                 'or', 'are', 'be', 'for', 'and', 'of', 'is', 'to', 'in', 'a', 'the', 'that', 'with', 'this', 'from',
                 'when', 'which', 'like', 'there', 'have', 'will', 'must', 'after', 'some', 'while', 'than', 'look',
                 'about', 'also', 'is also', 'over', 'using', 'just', 'such'
                 ]
REPEAT_TIME = 50
ZIPFILE_NAME = "python-3.11.4-docs-text.zip"
CLIPBOARD_NAME = "clipboard.txt"

# Переносим текст из файлов архива в один документ
with ZipFile(ZIPFILE_NAME, "r") as myzip:
    for item in myzip.infolist():
        if not item.is_dir():
            content = myzip.read(item.filename)
            with open(CLIPBOARD_NAME, "ab") as text:
                text.write(content)

# Читаем файл, занося слова в список
text = open(CLIPBOARD_NAME, "r", encoding="utf-8")
text_list = []
for line in text:
    line_list = line.split()
    text_list.extend(line_list)
text.close()
os.remove(CLIPBOARD_NAME)

# Получаем словарь из слов с количеством повторов
text_lib = {}
preview_word = ""
for word in text_list:
    word = word.lower()
    if word in EXCEPT_WORLDS:
        preview_word = word + " "
        continue
    elif word.isalpha():
        word = preview_word + word
        preview_word = ""
    else:
        preview_word = ""
        continue
    if word in text_lib:
        text_lib[word] += 1
    else:
        text_lib[word] = 1

# Получаем минисловарь из слов, повторяющихся более чем REPIT_TIME
mini_text_lib = {}
for word in text_lib:
    if text_lib[word] > REPEAT_TIME:
        mini_text_lib[word] = text_lib[word]

# Сортируем слова по количеству упоминаний
sorted_values = sorted(mini_text_lib.values(), reverse=True)
sort_mini_text_lib = {}
for i in sorted_values:
    for k in mini_text_lib.keys():
        if mini_text_lib[k] == i:
            sort_mini_text_lib[k] = mini_text_lib[k]

# Помещаем слова в отдельный файл
with open("result.txt", "w") as result:
    for word in sort_mini_text_lib:
        result.write(word + "\n")
print(sort_mini_text_lib.keys())