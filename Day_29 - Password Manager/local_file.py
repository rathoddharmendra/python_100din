import pandas, os

class LocalFile(pandas.DataFrame):
    def __init__(self):
        super().__init__()
        self.filename = os.path.join(__file__, 'local.txt')

    def save_to_disk(self, website, email, password):
        values = [website, email, password]
        headers = ['Website', 'Email', 'Password']
        row = self()


