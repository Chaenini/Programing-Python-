import pickle

class FileManager():
    def __init__(self, filename):
        self.filename = filename

    def save(self, data):
        with open(self.filename, "wb") as f :
            pickle.dump(data,f) #끝나면 알아서 close 해줌

    def load(self):
        try :
            with open(self.filename, "rb") as f :
                data = pickle.load(f)
        except FileNotFoundError:
            raise FileNotFoundError

        return data