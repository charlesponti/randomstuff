from lessons.classes import Person, SpecialPerson

def setup_function():
    print("setting up state...")

def test_person():
    person = Person(name="John", age=35, job="Python Developer")
    assert person.get() == {"name": "John", "age": 35}

def test_special_person():
    person = SpecialPerson(name="John Doe", age=35, job="Python Developer")
    assert person.get() == {"name": "John Doe", "age": 35, "type": "special"}
    assert person.email == "john_doe@email.com"
    assert person.get_display() == "John Doe is 35 and works as a Python Developer"

def teardown_function():
    print("tearing down state...")