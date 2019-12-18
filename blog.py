__author__ = "Cate"

class Blog(object):
    def __init__(self, author, title, description, id=None): #Default values can only be at the end
        self.author = author
        self.title = title
        self.description = description
        self.id = uuid.uuid4().hex if id is None else id

    def new_post(self):
        pass

    def get_posts(self):
        pass

    def save_to_mongo(self):
        pass

    def json(self):
        pass

    def get_from_mongo(self):
        pass
