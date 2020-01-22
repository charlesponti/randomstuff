#
# Example file for working with classes
#
class Person:
    def __init__(self, name: str, age: int, job: str, **kwargs):
        self.name = name
        self.age = age
        self.job = job

    def get(self):
        return {
          "name": self.name,
          "age": self.age
        }

    @property
    def email(self):
      return f"{self.name.lower().replace(' ', '_')}@email.com"

class SpecialPerson(Person):
  type: str

  def get(self):
    return {
      "name": self.name,
      "age": self.age,
      "type": "special"
    }

  def get_display(self):
    return f"{self.name} is {str(self.age)} and works as a {self.job}"
