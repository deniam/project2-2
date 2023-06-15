class GrammarStats:
    def __init__(self):
        self.checks_completed = 0
        self.good_checks = 0
  
    def check(self, text):
        if text == "":
            raise Exception("This string is empty.")
        self.checks_completed += 1
        if text[0].isupper() and text[-1] in ".?!":
            self.good_checks += 1
            return True
        return False
  
    def percentage_good(self):
            return (self.good_checks / self.checks_completed) * 100