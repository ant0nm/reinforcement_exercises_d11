# exercise 1 - emotions
human_emotions = {"happiness": 2, "sadness": 1, "fear": 2, "anger": 1,
                    "surprise": 3, "disgust": 1, "shame": 1}
# print out the emotions
print("Exercise 1:")
for emotion, degree in human_emotions.items():
    print("{} felt at level {}".format(emotion, degree))

# exercise 2 - person class
class Person:

    """ A class representing a person """

    def __init__(self, name, emotions):
        self.name = name
        self.emotions = emotions

    def __str__(self):
        return "Person: {}\nPerson's Emotions: {}".format(self.name, self.emotions)

    # exercise 3 - adding an instance method
    def display_emotions(self):
        for emotion, degree in self.emotions.items():
            converted_degreee = None
            if degree == 1:
                converted_degreee = "low"
            elif degree == 2:
                converted_degreee = "medium"
            elif degree == 3:
                converted_degreee = "high"
            print("I am feeling a {} amount of {}.".format(converted_degreee, emotion))
# create an instance of the Person class
print()
print("Exercise 2:")
anton = Person("Anton", human_emotions)
print(anton)

# exercise 3 - state the emotions
print()
print("Exercise 3:")
anton.display_emotions()
