#!/usr/bin/env python3

class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        return f"{self.name} says Woof!"
    
    def __init__(self, name, breed="Mutt"):
        self.name = name
        self.breed = breed