class Stud:
    def __init__(self, fio):
        self.fio = fio
        self.spisOtm = list()
    def getFio(self):
        return self.fio
    def setFio(self, fio):
        self.fio = fio
    def getSpisOtm(self):
        return self.spisOtm
    def setSpisOtm(self, spisOtm):
        self.spisOtm = spisOtm
class Theme:
    def __init__(self, theme, date):
        self.theme = theme
        self.date = date

    def getTheme(self):
        return self.theme

    def setTheme(self, theme):
        self.theme = theme

    def getDate(self):
        return self.date

    def setDate(self, date):
        self.date = date