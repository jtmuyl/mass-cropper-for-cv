# (c) Jean-Thomas MUYL
# jeanthomasmuyl@gmail.com
# MIT License

__author__ = 'jt'
import random

def randomID():
    return ''.join(random.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz') for i in range(15))
