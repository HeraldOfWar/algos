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
for i in range(len(report) - 3):
    res += len(report[i])
    ex_report = ''.join(report[i:i + 3])
    for j in range(len(wiki) - 3):
        ex_wiki = ''.join(wiki[j:j + 3])
        if ex_wiki == ex_report:
            plag += len(ex_report)

print(f'Процент плагиата – {round(plag / res * 100, 2)}%')