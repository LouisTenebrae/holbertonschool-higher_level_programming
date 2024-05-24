#!/usr/bin/python3
class SwimMixin:
    '''Creates SwimMixin class'''

    def swim(self):
        '''Swim method'''
        print('The creature swims!')


class FlyMixin:
    '''Creating FlyMixin class'''

    def fly(self):
        '''Fly method'''
        print('The creature flies!')


class Dragon(SwimMixin, FlyMixin):
    '''Creating Dragon class'''

    def roar(self):
        '''Roar method'''
        print('The dragon roars!')
