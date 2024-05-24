#!/usr/bin/python3

class Fish:
    '''Creating Fish class'''

    def swim(self):
        '''Swim method'''
        print('The fish is swimming')

    def habitat(self):
        '''Habitat method'''
        print('The fish lives in water')


class Bird:
    '''Creating Bird class'''

    def fly(self):
        '''Fly method'''
        print('The bird is flying')

    def habitat(self):
        '''Habitat method'''
        print('The bird lives in the sky')


class FlyingFish(Fish, Bird):
    '''Creating FlyingFish class'''

    def fly(self):
        '''Re-writes fly class'''
        print('The flying fish is soaring!')

    def swim(self):
        '''Re-writes swim class'''
        print('The flying fish is swimming!')

    def habitat(self):
        '''Re-writes habitat class'''
        print('The flying fish lives both in water and the sky!')
