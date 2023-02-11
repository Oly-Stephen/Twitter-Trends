import csv


class SentimentWords:
    def __init__(self, file_path):
        self.file_path = file_path

    def process_file(self):
        self.data = {}
        with open(self.file_path, "r") as file:
            contents = csv.reader(file)
            for row in contents:
                self.data[row[0]] = float(row[1])

        return self.data
