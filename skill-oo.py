"""Object Oriented Programming Assessment"""

"""Answer each question in your own words.

1. What are the three main design advantages that object orientation can provide?
    A: Three main advantages are encapsulation (the data is near the functions), 
    polymorphism (easy to make changes and make things different), and
    abstraction (you don't need to know how something works for it to work).

2. Explain each concept.

    a. What is a class?


    b. What is an instance attribute?
    A: an attribute that is specifically tied to an instance and not necessarily
    an entire class. 

    c. What is a method?
    A: a method is a function that works within the class structure and can be 
    applied to its subclasses.

    d. What is an instance in object orientation?
    A: an instance is the object made within a class or subclass.
    ex: Snowball McCatFace is an instance in the subclass Cat, of the class Pets

3. How is a class attribute different than an instance attribute? Give an example of when you might use each.
    A: a class attribute is something that is specific to the class as a whole, 
    and can also be thought of as a common attribute of the whole class.
    an instance attribute is an attribute that is tied only to the instance
    and not to the whole class. You might use an instance attribute over a class
    attribute if it is an attribute unique only to that instance."""


class Student(object):
    def __init__ (self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address


class Question(object):
    def __init__ (self, question, correct_answer):
        self.question = question
        self.correct_answer = correct_answer

        #trying to create a dictionary out of the questions/answers
        exam_questions = [exam_questions[question]:correct_answer]

Class Exam(object):
    def __init__ (self, questions, name):      
        self.questions = questions
        self.name = name

    def make_questions():
        """creates a question"""

             




























