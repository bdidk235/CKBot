import random
from youtubesearchpython import SearchVideos

def unique_random_unicode(length):
    random_ints = random.sample(range(0x07FF), length)
    random_unicodes = [chr(x) for x in random_ints]
    return u"".join(random_unicodes)

def youtube_search(search, max_results:int = 10):
    return [video for video in SearchVideos(search, mode = "dict", max_results = max_results).result()['search_result']]

class Element:
    def __init__(self, *, header, short_desc=None, long_desc=None, elements=None):
        self._parent = None
        self.header = header
        self.short_desc = short_desc or ""
        self.long_desc = long_desc or ""
        self.elements = elements or []
        self.current = 0
        # Set parents
        for elem in self.elements:
            elem._parent = self
    
    @property
    def parent(self):
        return self if self._parent is None else self._parent

    @property
    def element(self):
        if len(self.elements) == 0:
            return self
        return self.elements[self.current]

    def next_elem(self):
        if len(self.elements) > 0:
            self.current = (self.current + 1) % len(self.elements)
    
    def prev_elem(self):
        if len(self.elements) > 0:
            self.current = (self.current - 1) % len(self.elements)
    
    def display_elements(self, sep="\n"):
        table = ""
        for i, elem in enumerate(self.elements):
            table = f"{table}{sep}{elem.display(1, i == self.current)}"
        return table[len(sep):]

    def display(self, depth=0, highlight=False):
        header = f"**{self.header}**" if not highlight else f"> **{self.header}**"
        content = self.long_desc if depth == 0 else self.short_desc
        content = f"{header}\n{content}"
        # Also display children
        if len(self.elements) > 0 and depth < 1:
            content = f"{content}\n{self.display_elements()}"
        return content.strip()