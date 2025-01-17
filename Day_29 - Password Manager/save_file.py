import pandas, os

class SaveFile():
    '''
    saves credentials to a file
    '''
    def __init__(self):
        self.filename = os.path.join(os.path.dirname(__file__), 'local.txt')

    def save_to_disk(self, website: str, email: str, password: str):
        values = [website, email, password]
        headers = ['Website', 'Email', 'Password']
        # new_learnen - saving to disk
        df = pandas.DataFrame(data=[values], columns=headers)
        df.to_csv(self.filename, mode='a', header=not os.path.exists(self.filename), index=False)
        # only sets header when the file is newly created - header=not os.path.exists(self.filename)


