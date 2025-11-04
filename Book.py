class Book:
    def __init__(self, ID, title, author, publication_year, category, availability, count):
        self._ID = ID
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.category = category
        self.availability = availability
        self.count = count

    def get_ID(self):
        return self._ID

    def set_ID(self, value):
        self._ID = value

    def get_title(self):
        return self.title

    def set_title(self, value):
        self.title = value

    def get_author(self):
        return self.author

    def set_author(self, value):
        self.author = value

    def get_publication_year(self):
        return self.publication_year

    def set_publication_year(self, value):
        self.publication_year = value

    def get_category(self):
        return self.category

    def set_category(self, value):
        self.category = value

    def get_availability(self):
        return self.availability

    def set_availability(self, value):
        self.availability = value

    def get_count(self):
        return self.count

    def set_count(self, value):
        self.count = value

    def display(self):
        print(f"{self._ID} | {self.title} | {self.author} | {self.publication_year} | "
              f"{self.category} | {self.availability} | {self.count} |")

