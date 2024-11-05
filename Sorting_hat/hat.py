
import random
import cowsay
import pyttsx3

class Hat:
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    @classmethod
    def sort(cls, name):
        result = f"{name} you are going to be assigned to {random.choice(cls.houses)} house"
        return result

while True:
    # Get the name and sort the student
    name = input("What's the name: ")
    if not name:
        no_name = f"Don't Be Affraid my Child, you can tell me your name\n"
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)
        """ RATE"""
        rate = engine.getProperty('rate')  # getting details of current speaking rate
        engine.setProperty('rate', 100)
        #MAke the cow say
        cowsay.cow(no_name)

        engine.say(no_name)
        engine.runAndWait()

    else:
        this = Hat.sort(name)

        # Make the cow say the sorting result
        cowsay.cow(this)

        # Use text-to-speech to announce the sorting result
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)
        """ RATE"""
        rate = engine.getProperty('rate')  # getting details of current speaking rate
        engine.setProperty('rate', 100)

        engine.say(this)
        engine.runAndWait()