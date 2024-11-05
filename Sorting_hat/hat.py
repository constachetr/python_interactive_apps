
import random
import cowsay
import pyttsx3

class Voice_assist:
    def __init__(self, voice_index=0, rate=100):
        self.engine = pyttsx3.init()
        self.set_voice(voice_index)
        self.set_rate(rate)

    def set_voice(self, voice_index):
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[voice_index].id)

    def set_rate(self, rate):
        self.engine.setProperty('rate', rate)

    def say(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

class Hat:
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    @classmethod
    def sort(cls, name):
        result = f"{name} you are going to be assigned to {random.choice(cls.houses)} house"
        return result

        # Voice assist for the output with the parameters
voice_assist = Voice_assist(voice_index=1, rate=100)

while True:
    # Get the name and sort the student
    name = input("What's the name: ")
    if not name:
        no_name = f"Don't Be Affraid my Child, you can tell me your name\n"

        #MAke the cow speak
        cowsay.cow(no_name)

        #Voice assist output
        voice_assist.say(no_name)

    else:
        this = Hat.sort(name)
         # Make the cow say the sorting result
        cowsay.cow(this)

        # Voice assist output
        voice_assist.say(this)


