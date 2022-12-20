class Article:
    def __init__(self, title: str):
        self.title = title
        self.url = self.__get_url(self.title)


# imaginary_numbers = Article("put in title of article")

# I want to be able to access the following attributes/methods
# - url
# - soup
# - what_links_here()
