import re


BOLD_RE = re.compile(r"__(.*?)__")
ITALICS_RE = re.compile(r"_(.*?)_")
HEADER_RE = re.compile(r"(#+) (.*)")
LIST_RE = re.compile(r"\* (.*)")


def parse(markdown):
    result = ''
    lines = markdown.split('\n')
    for line in lines:
        line = BOLD_RE.sub(r'<strong>\1</strong>', line)
        line = ITALICS_RE.sub(r'<em>\1</em>', line)

        is_header = HEADER_RE.match(line)
        is_list = LIST_RE.match(line)
        
        if is_header:
            result += "<h{0}>{1}</h{0}>".format(len(is_header.group(1)), 
                                                is_header.group(2))
        elif is_list:
            if result[-5:] == "</ul>":
                result = result[0:-5]
            else:
                result += "<ul>"
            result += "<li>{}</li></ul>".format(is_list.group(1))
        else:
            result += "<p>" + line + "</p>"
    return result
