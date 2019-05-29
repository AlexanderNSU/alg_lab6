#!/usr/bin/env python
# -*- coding: utf-8 -*-

def is_paranthesis_balanced(s):
    dct={'(':')','[':']','{':'}','<':'>'}
    if len(s)==0:
        return True
    stack = Stack(len(s))
    for i in range(len(s)):
        if s[i] in ['(', '[', '{', '<']:
            stack.push(s[i])
        else:
            if dct.get(stack.pop())==s[i]:
                continue
            else:
                return False
    if stack.__len__() == 0:
        return True
