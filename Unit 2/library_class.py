# library class

class Library:
    def __init__(self, name, author):
        self.name = name
        self.author = author
        self.avail = True

    def issue(self):
        if self.avail == True:
            print("book given")
            self.avail = False
        else:
            print("not available")

    def ret(self):
        self.avail = True
        print("book returned")

    def show(self):
        print(self.name, self.author, self.avail)


b = Library("python", "abc")

b.show()
b.issue()
b.ret()