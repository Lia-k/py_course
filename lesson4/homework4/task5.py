# у вас есть текст разбейте текст по предложениям. В качестве результата вы
# должны получить список из предложений.

import re
import codecs

with codecs.open('text.txt', encoding='utf-8') as file:
    text = file.read()
    sentences = re.findall(r"[А-Я].*?[\.!?](?=\s|$)", text)

    print(sentences)

# Best solution and looks almost like mine. Good job.
