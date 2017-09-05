

class FileLogger:

    def __init__(self, filename):
        self.filename = filename
        self.file = ""
        self.create_file()

    def create_file(self):
        self.file = open(self.filename, 'w+')

    def add_to_file(self, txt, nl=True):
        with open(self.filename, "a") as f:
            f.write(txt)
            if nl:
                f.write("\n")
