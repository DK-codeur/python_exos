# heritage de class
class Univ(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Univ created")

    def univName(self):
        print('UNIV\'s NAME IS '+ self.name)

    def univAge(self):
        print('UNIV\'s AGE IS', self.age)
        
    def welc(self):
        print('welcom to our school')

#school() extend Univ()   
class school(Univ):
    def __init__(self):
        Univ.__init__(self, name='fontaine', age=5)
        print("la fontaine created")

    def fontaine_locat(self):
        print('fontaine is behind cap sud')



lokof = school()
lokof.univName()
lokof.univAge()
lokof.fontaine_locat()
# lokof.welc()