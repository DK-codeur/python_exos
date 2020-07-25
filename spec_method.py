#special method
class book():
    def __init__(self, title, author, page):
        self.title = title
        self.author = author
        self.page = page

    #default sentence 
    def __str__(self):
        return 'Book Title : {0}\nBook Author : {1}\nBook  Page : {2}'.format(self.title, self.author, self.page)

myBook = book('coding learning', 'Dk-codeur', 100)
print(myBook)