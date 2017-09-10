from Students import *
class Ingenieria(Students, object):
    """docstring for Ingenieria."""

    def printFullNameUpperCase(self):
        allData = super(Ingenieria, self).getAllDataOfStudent()
        return allData.upper()
