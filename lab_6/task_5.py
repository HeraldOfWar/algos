import timeit
import wikipediaapi
from docx import Document

s = ['\n', '–', '.', '...', ':', '\"', '\"', '!', '@', '#', '№', '$', ';', '%', '^', '?', '&', '*', '(', ')', '[', ']',
     '{', '}', '<', '>', '/', '|', '-', '—', '\t', ' ']


def get_text_from_doc(filename):
    doc = Document(filename)
    text = []
    for p in doc.paragraphs:
        for i in p.text.split():
            word = i
            if word:
                for j in s:
                    word = word.strip(j)
                if word:
                    text.append(word)
    return text


def get_text_from_wiki(page_name):
    wiki_wiki = wikipediaapi.Wikipedia(
        language='ru',
        extract_format=wikipediaapi.ExtractFormat.WIKI
    )
    p_wiki = wiki_wiki.page(page_name)
    text = []
    for i in p_wiki.text.split():
        word = i
        if word:
            for j in s:
                word = word.strip(j)
            if word:
                text.append(word)
    return text


plag, res = 0, 0
report, wiki = get_text_from_doc('Научный метод.docx'), get_text_from_wiki('Научный метод')
for word in report:
    res += len(word)
reports = []
for i in range(len(report) - 3):
    ex_report = report[i:i + 3]
    reports.append(ex_report)
wikis = []
for j in range(len(wiki) - 3):
    ex_wiki = wiki[j:j + 3]
    wikis.append(ex_wiki)
start = timeit.default_timer()
for ex_report in reports:
    for ex_wiki in wikis:
        if ex_wiki == ex_report:
            plag += sum([len(ex_report[k]) for k in range(3)])
end = timeit.default_timer() - start
print(f'Наивный алгоритм: {end}с')
print(f'Процент плагиата – {round(plag / res * 100, 2)}%')

alphabet = list(set(wiki))
plag = 0
ex_wiki_hashes = []
start = timeit.default_timer()
for j in range(len(wiki) - 3):
    ex_wiki = wiki[j:j + 3]
    ex_wiki_hashes.append(sum([alphabet.index(ex_wiki[i]) * len(alphabet) ** (2 - i) for i in range(3)]))
for i in range(len(report) - 3):
    hash_ex_report = sum(
        [alphabet.index(report[i + j]) * len(alphabet) ** (2 - j) for j in range(3) if report[i + j] in alphabet])
    if hash_ex_report in ex_wiki_hashes:
        for j in range(len(ex_wiki_hashes)):
            hash_ex_wiki = ex_wiki_hashes[j]
            if hash_ex_report == hash_ex_wiki:
                if report[i:i + 3] == wikis[j]:
                    plag += sum([len(report[i + k]) for k in range(3)])
end = timeit.default_timer() - start
print(f'Алгоритм Рабина-Карпа: {end}с')
print(f'Процент плагиата – {round(plag / res * 100, 2)}%')

plag = 0

start = timeit.default_timer()
for i in range(len(report) - 3):
    for j in range(len(wiki) - 3):
        if wiki[j + 2] == report[i + 2]:
            if wiki[j + 1] == report[i + 1]:
                if wiki[j] == report[i]:
                    plag += sum([len(report[i + k]) for k in range(3)])
            elif wiki[j + 1] != report[i]:
                j += 1
        elif wiki[j + 2] == report[i]:
            j += 1
        else:
            j += 2
end = timeit.default_timer() - start
print(f'Алгоритм Бойера-Мура: {end}с')
print(f'Процент плагиата – {round(plag / res * 100, 2)}%')

plag = 0
start = timeit.default_timer()
for ex_report in reports:
    prefix = [0, 0, 0]
    if ex_report[0] == ex_report[1]:
        prefix[1] += 1
    if ex_report[0] == ex_report[2]:
        prefix[2] += 1
    for j in range(len(wikis)):
        ex_wiki = wikis[j]
        if ex_wiki == ex_report:
            plag += sum([len(ex_report[k]) for k in range(3)])
        elif ex_wiki[0] == ex_report[0]:
            if ex_wiki[1] == ex_report[1]:
                j += 2 - prefix[2]
            else:
                j += 1 - prefix[1]
end = timeit.default_timer() - start
print(f'Алгоритм Кнута-Морриса-Пратта: {end}с')
print(f'Процент плагиата – {round(plag / res * 100, 2)}%')
