#!/usr/bin/env python3
import re
import sys
from collections import deque
from urllib.parse import unquote, quote

try:
    import httpx
except ModuleNotFoundError:
    import pip

    pip.main(['install', '--quiet', 'httpx'])
    import httpx


# для обращения к веб-странице можно использовать примеры
# https://www.python-httpx.org

class Node:
    def __init__(self, parent_node, link):
        self._parent = parent_node
        self._link = link

    @property
    def parent(self):
        return self._parent

    @property
    def link(self):
        return self._link


def extract_title(url):
    return unquote(url.split("/wiki/")[-1]).lower()


def get_content(link):
    """
    Функция возвращает содержимое вики-страницы name из русской Википедии.
    В случае ошибки загрузки или отсутствия страницы возвращается None.
    """
    try:
        if not link.startswith("http"):
            link = "https://" + link
        response = httpx.get(link, timeout=10.0)
        return response.text
    except (httpx.RequestError, httpx.HTTPStatusError):
        return None


def extract_content(page):
    """
    Функция принимает на вход содержимое страницы и возвращает 2-элементный
    tuple, первый элемент которого — номер позиции, с которой начинается
    содержимое статьи, второй элемент — номер позиции, на котором заканчивается
    содержимое статьи.
    Если содержимое отсутствует, возвращается (0, 0).
    """
    start_tag = '<div id="bodyContent"'
    start_index = page.find(start_tag)

    if start_index == -1:
        return 0, 0

    index = start_index + len(start_tag)
    open_divs = 1

    while open_divs > 0:
        next_open = page.find('<div', index)
        next_close = page.find('</div>', index)

        if next_close == -1:
            return start_index, 0

        if next_open != -1 and next_open < next_close:
            open_divs += 1
            index = next_open + 4
        else:
            open_divs -= 1
            index = next_close + 6

    end_index = index
    return start_index, end_index


def extract_links(page, begin, end):
    """
    Возвращает уникальные имена статей Википедии из указанного диапазона
    текста.
    Декодирует URL и учитывает регистр. Возвращает только имя статьи,
    без префикса.
    """
    text = page[begin:end + 1]
    pattern = re.compile(
        r"""<\s*a[^>]*\s+href\s*=\s*['"](/wiki/[^'":#]+)['"]""",
        re.IGNORECASE
    )
    matches = pattern.findall(text)
    decoded_titles = {unquote(link.split("/wiki/")[1]) for link in matches}
    return sorted(decoded_titles)


def create_chain(node):
    path = [extract_title(node.link)]
    current = node.parent
    while current.parent is not None:
        path.append(extract_title(current.link))
        current = current.parent
    path.append(extract_title(current.link))
    return path[::-1]


def find_chain(start, finish):
    """
    Функция принимает на вход название начальной и конечной статьи и возвращает
    список переходов, позволяющий добраться из начальной статьи в конечную.
    Первым элементом результата должен быть start, последним — finish.
    Если построить переходы невозможно, возвращается None.
    """
    finish_lower = finish.lower()
    start_lower = start.lower()
    start_lower = start_lower.replace('ё', 'е')
    finish_lower = finish_lower.replace('ё', 'е')

    if start_lower == finish_lower:
        return [start]

    wiki_url = "https://ru.wikipedia.org/wiki/"
    start_url = f"{wiki_url}{quote(start)}"

    visited = set()
    queue = deque([Node(None, start_url)])
    while queue:
        node = queue.popleft()
        wiki_page = node.link
        if wiki_page in visited:
            continue
        if extract_title(wiki_page).lower() == finish_lower:
            return create_chain(node)

        visited.add(wiki_page)
        article_content = get_content(wiki_page)

        if article_content is None:
            continue

        content_indexes = extract_content(article_content)
        links = extract_links(article_content, content_indexes[0],
                              content_indexes[1])
        queue.extend(
            [Node(node, f"https://ru.wikipedia.org/wiki/{quote(link)}")
             for link in links]
        )


def main():
    args = sys.argv[1:]
    path = find_chain(args[0], f"Философия")
    for link in path:
        print(link)


if __name__ == '__main__':
    main()
