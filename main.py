from random import *

class Student:
  def __init__(self, name):
    self.name = name
    self.gladness = 50
    self.progress = 0
    self.alive = True

  def study(self):
    print('study time')
    self.progress += 0.12
    self.gladness -= 5

  def sleep(self):
    print('Sleep time')
    self.gladness += 3

  def chill (self):
    print('Chill time')
    self.gladness += 5
    self.progress -= 0.1

  def is_alive(self):
    if self.progress < -0.5:
      print('So bad')
      self.alive = False
    elif self.gladness <= 0:
      print('Depression...')
      self.alive = False
    elif self.progress > 5:
      print('Mission passed')
      self.alive = False

  def end(self):
    print('Gladness:', self.gladness)
    print('Progress:', self.progress)
    
  def live(self, day):
    print('Day:',day)
    live_cube = randint(1,3)
    if live_cube == 1:
      self.study()
    elif live_cube == 2:
      self.sleep()
    elif live_cube == 3:
      self.chill()
    self.end()
    self.is_alive()

obj = Student('Bob')

for day in range(365):
	if obj.alive == False:
		break
	obj.live(day)