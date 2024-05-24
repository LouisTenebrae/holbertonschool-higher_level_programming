#!/usr/bin/python3
from abc import ABC, abstractmethod
'''Importing ABC, abstractmethod'''


class Animal(ABC):
    '''Creating Animal class'''
    @abstractmethod
    def sound(self):
        '''Sound method'''
        pass


class Dog(Animal):
    '''Creating Dog class'''

    def sound(self):
        return 'Bark'


class Cat(Animal):
    '''Creating Cat class'''

    def sound(self):
        return 'Meow'
