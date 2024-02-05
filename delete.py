from docx import Document
from docx.shared import Pt


def replace_string(filename):
    doc = Document(filename)
    for p in doc.paragraphs:
        if 'old text' in p.text:
            inline = p.runs
            # Loop added to work with runs (strings with same style)
            for i in range(len(inline)):
                if 'old text' in inline[i].text:
                    text = inline[i].text.replace('old text', 'new text')
                    inline[i].text = text
            print(p.text)

    doc.save('dest1.docx')
    return 1
