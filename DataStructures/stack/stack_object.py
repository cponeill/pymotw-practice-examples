#!/usr/bin/env python3
# stack_object.py

# Create a Stack Class
# Defined as "first in, last out"

class Stack(object):

    # Initialize stack object with an empty list
    def __init__(self):
        self.lst = []

    # Return a true or false if stack is empty
    def is_empty(self):
        return self.lst == []

    # Push a new value on top of the stack
    def push(self, value):
        return self.lst.append(value)

    # Remove the top value from the stack
    def pop(self):
        return self.lst.pop()

    # Return the value on top of the stack
    def peek(self):
        return self.lst[len(self.lst) - 1]

    # Return the length of the stack
    def length(self):
        return len(self.lst)


def get_binary_digits(number):
    """Return the binary digits of a given number."""
    lst = Stack()

    while number > 0:
        rem = number % 2
        lst.append(rem)
        number //= 2

    binary_digits = ""

    while no lst.is_empty():
        binary_digits += str(lst.pop())

    return binary_digits
