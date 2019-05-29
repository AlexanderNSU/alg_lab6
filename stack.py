#!/usr/bin/env python
# -*- coding: utf-8 -*-


class StackOverflowError(RuntimeError):
    pass


class StackIsEmptyError(RuntimeError):
    pass


class Stack:
    def __init__(self, size):
        self.storage = [0] * size
        self.head = -1
        self.size=size

    def push(self, v):
        if self.head >= self.size - 1: 
            raise StackOverflowError(RuntimeError)        
        self.head += 1
        self.storage[self.head] = v
        return self.storage

    def pop(self):
        if self.head == -1:
            raise StackIsEmptyError(RuntimeError)
        d = self.storage[self.head]
        self.head -= 1
        return d

    def __len__(self):
        return self.head + 1
