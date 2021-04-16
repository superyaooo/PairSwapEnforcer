from random import randint

class Greetings(object):
    greetings = ["Guess what day it is? It's pair swapping day, Sherlock.", "Roses are red, Violets are blue, Who's gonna swap pairs today, Guess it's you.", "What is up? Your time with your current pair partner.", "...pair swap...now!!!!!!!!!!", "Hey, guess who'd be happy to work with you today? Your next pair partner."]

    def get_greeting(self):
        max = len(self.greetings) - 1
        value = randint(0,max)
        greeting = self.greetings[value]
        return greeting