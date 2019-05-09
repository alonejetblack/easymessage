class EasyMessage:
    def __init__(self, text=None):
        if text is not None:
            self.text = text
            self.default = text

    def __call__(self, text=''):
        if not hasattr(self, 'text'):
            self.text = text
            self.default = text
        else:
            if self.text == '': self.text += f"{text}"
            else: self.text += f"\n{text}"

    def split(self, text):
        return self.text.split(text)

    def isChange(self):
        if not hasattr(self, 'default'):
            return True
        return len(self.default) == len(self.text)

    def __repr__(self):
        return '%s(%s)' % (self.__class__.__name__, ', '.join(['%s=%r' % (key, value) for key, value in self.__dict__.items()]))

if __name__ == '__main__':
    message = EasyMessage("Hello world")
    message("What are you looking for?")
    message("Is this is your looking for?")
    #print(message.text)
    print(message)
