#8. Creating class about programming language details.

class Language:
    #state
    def __init__(self, language, founded, creator):
        self.language = language
        self.founded = founded
        self.creator = creator
    #behaviour
    def lang_history(self):
        print("'Name of the Language' 'Year' 'Created By': ", self.language, self.founded, self.creator)

details = Language("Python", 1991, "Guido Von Rossum")
details.lang_history()