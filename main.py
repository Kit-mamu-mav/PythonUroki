class Human:
  def __init__(self):
    self.name = 'None'
    self.age = 0
    self.gender = 'None'
  def introduce(self):
    print('Hello, my name is', self.name)
  def add_info(self):
    self.name = input('Name: ')
    self.age = int(input('Age: '))
    self.gender = input('Gender: ')

obj = Human()
obj.introduce()
obj.add_info()
obj.introduce()