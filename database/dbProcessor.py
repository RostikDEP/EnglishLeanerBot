import sqlite3


class dbProcessor:
    def __init__(self, path):
        self.db_path = path
        self.db = sqlite3.connect(path)
        self.cursor = self.db.cursor()


    def AddWord(self, word_, translate, sentence, user):
        self.cursor.execute(f"INSERT INTO words(word, translate, sentence, user, entered, complete) VALUES (?, ?, ?, ?, ?, ?)", (word_, translate, sentence ,user, 0, 0))
        self.db.commit()

    def GetRandomWord(self):
        data = self.cursor.execute("SELECT * FROM words ORDER BY RANDOM() LIMIT 1")
        return data.fetchone()



# if __name__ == "__main__":
#     dbProc = dbProcessor("../data/words.db")
#     print(dbProc.GetRandomWord())
#   dbProc.AddWord("Hello", "Hello", "Sentence","User")