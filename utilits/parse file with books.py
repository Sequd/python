import xml.etree.cElementTree as ET


def parse_txt():
    file_obj = open('books.txt')
    for line in file_obj:
        print(line.strip())
        break


def parse_xml(xml_file):
    """
        Парсинг XML используя ElementTree
        """
    tree = ET.ElementTree(file=xml_file)
    print(tree.getroot())
    root = tree.getroot()
    print("tag=%s, attrib=%s" % (root.tag, root.attrib))

    # for child in root:
    #     print(child.tag, child.attrib)
    #     if child.tag == "appointment":
    #         for step_child in child:
    #             print(step_child.tag)

    # Парсинг всей XML структуры.
    # print("-" * 40)
    # print("Iterating using a tree iterator")
    # print("-" * 40)
    # iter_ = tree.iter()

    # for elem in iter_:
    #     print(elem.tag)

    # получаем данные используя дочерние элементы.
    print("-" * 40)
    print("Обрабатываем дочерние жлменты getchildren()")
    print("-" * 40)
    appointments = root.getchildren()

    books = []
    for appointment in appointments:
        appt_children = appointment.getchildren()
        book = Book()
        for appt_child in appt_children:
            # print("%s=%s" % (appt_child.tag, appt_child.text))
            if appt_child.tag == "name":
                book.name = appt_child.text
            elif appt_child.tag == "year":
                book.year = appt_child.text
            elif appt_child.tag == "url":
                book.url = appt_child.text
            elif appt_child.tag == "author":
                book.author = appt_child.text
        books.append(book)
        # print(book)

    filer_books = list((book for book in books if filter_book_name(book.name, 'CSS')))
    # filer_books = list(
    #     (book for book in filer_books if filter_book_author(book.author, 'Алан')))  # Мартин Фаулер

    print("Всего книг: %s" % len(books))
    print("-" * 40)
    print("Найдено книг: %s" % len(filer_books))
    print(*filer_books, sep='\n')  # print(p) for p in myList
    print("-" * 40)


def filter_book_name(name, exist):
    if name is None:
        return False
    if exist not in name:
        return False
    elif name is None:
        return True
    else:
        return True


def filter_book_author(author, exist):
    if author is None:
        return False
    if exist not in author:
        return False
    elif author is None:
        return False
    else:
        return True


class Book:
    name = ""
    year = ""
    url = ""
    author = ""

    def __str__(self):
        return "Name: %s\n Author %s\n Year %s\n url: %s" % (self.name, self.author, self.year, self.url)

    # def __init__(self, name, year, url):
    #     self.name = name
    #     self.url = url
    #     self.year = year


parse_xml('books.xml')
