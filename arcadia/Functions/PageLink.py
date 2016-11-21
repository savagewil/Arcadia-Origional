import Function
import ArcadiaCleint

class PageLink(Function.Function):
    def __init__(self, page):
        self.page = page

    def run(self):
        return page()

