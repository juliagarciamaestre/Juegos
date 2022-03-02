
class Message:
    def __init__(self):
        self.message = ""

    def colide_gem(self):
        self.message = "Hurrah! You got 1 point!"
        return self.message

    def colide_rock(self):
        self.message = "Ups! You lost 1 point!"
        return self.message
