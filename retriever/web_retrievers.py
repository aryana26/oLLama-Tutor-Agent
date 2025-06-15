from langchain_community.tools.ddg_search.tool import DuckDuckGoSearchRun
from langchain_community.tools.wikipedia.tool import WikipediaQueryRun
from langchain_community.utilities.wikipedia import WikipediaAPIWrapper

class WebRetriever:
    def __init__(self):
        self.search = DuckDuckGoSearchRun()

    def retrieve(self, query):
        results = self.search.run(query)
        return [type("Doc", (), {"page_content": results})()]

class WikipediaRetriever:
    def __init__(self):
        api_wrapper = WikipediaAPIWrapper()
        self.search = WikipediaQueryRun(api_wrapper=api_wrapper)

    def retrieve(self, query):
        results = self.search.run(query)
        return [type("Doc", (), {"page_content": results})()]
