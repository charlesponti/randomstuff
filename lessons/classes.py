#
# Example file for working with classes
#

class myClass():
  def method1(self):
    print("my class method1")

  def method2(self, someString):
    print(f"my class method2 - {someString}")

class myOtherClass(myClass):
  def method1(self):
    myClass.method1(self)
    print("myOtherClass method1")

  def method2(self, someString):
    super().method2("cats")
    # print(f"myOtherClass - {someString}")

class anotherClass():
  def __init__(self, name, age, job):
    self.name = name
    self.age = age
    self.job = job

  def get_display(self):
    return self.name + " is " + str(self.age) + " and works as a " + self.job

def main():
  class1 = myClass()
  class1.method1()
  class1.method2("cats")

  class2 = myOtherClass()
  class2.method1()
  class2.method2("cats")

  class3 = anotherClass("John Doe", 35, "Python Developer")
  print(class3.name, class3.age, class3.job)
  print(class3.get_display())

if __name__ == "__main__":
  main()
