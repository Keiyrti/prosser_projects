"""Module for storing PLAYER values."""

class Player(dict):
    def __init__(self):
        self['level'] = 1

        self['gold'] = 0

        self['strength'] = 1
        self['dexterity'] = 1
        self['agility'] = 1
        self['defense'] = 1
