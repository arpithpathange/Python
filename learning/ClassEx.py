class Dog():
    def __init__(self,dogName,dogAge,dogBread):
        self.Name = dogName
        self.Age = dogAge
        self.Bread = dogBread
        
    def setName(self,Name):
        self.Name = Name

    def removeName(self):
     	self.Name = 'NoName'
        

lab = Dog('Berry','Pug','12')
print lab.Name
print lab.Age
print lab.Bread

German = Dog('German','GS','12')
print German.Name
print German.Age
print German.Bread

lab.setName('Kurry')
print lab.Name
print lab.Age
print lab.Bread 

lab.removeName()
print lab.Name
print lab.Age
print lab.Bread 