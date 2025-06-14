from langchain_community.tools.ddg_search.tool import DuckDuckGoSearchRun
from langchain_community.tools.wikipedia.tool import WikipediaQueryRun

class WebRetriever:
    def __init__(self):
        self.search = DuckDuckGoSearchRun()
    def retrieve(self, query):
        results = self.search.run(query)
        return [type("Doc",(),{"page_content": results})()]

class WikipediaRetriever: # need for some structured querying from OG Wiki :P !  Cant trust em all!
    def __init__(self):
        self.search = WikipediaQueryRun()
    def retrieve(self, query):
        results = self.search.run(query)
        return [type("Doc", (), {"page_content": results})()]
