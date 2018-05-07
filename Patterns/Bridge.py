class Writer:
    def write(self, content=None):
        print("Write content: ")


class HtmlWriter(Writer):
    def write(self, content=None):
        super().write()
        print("<b>%s</b>" % content)


class ProcessingMachine:

    def __init__(self, w):
        self.writer = w

    def write(self, content):
        self.writer.write(content)


writer = HtmlWriter()
machine = ProcessingMachine(writer)
machine.write("It is content")
