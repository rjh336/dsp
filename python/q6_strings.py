# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0


def donuts(count):
    """
    Given an int count of a number of donuts, return a string of the
    form 'Number of donuts: <count>', where <count> is the number
    passed in. However, if the count is 10 or more, then use the word
    'many' instead of the actual count.
    """
    if count >= 10:
        return 'Number of donuts: many'
    else:
        return 'Number of donuts: ' + str(count) 

print(donuts(4) == 'Number of donuts: 4')
print(donuts(9) == 'Number of donuts: 9')
print(donuts(10) == 'Number of donuts: many')
print(donuts(99) == 'Number of donuts: many')


def both_ends(s):
    """
    Given a string s, return a string made of the first 2 and the last
    2 chars of the original string, so 'spring' yields 'spng'.
    However, if the string length is less than 2, return instead the
    empty string.
    """
    if len(s) < 2:
        return ''
    else:
        return s[:2]+s[len(s)-2:]

print(both_ends('spring') == 'spng')
print(both_ends('Hello') == 'Helo')
print(both_ends('a') == '')
print(both_ends('xyz') == 'xyyz')
    
def fix_start(s):
    """
    Given a string s, return a string where all occurences of its
    first char have been changed to '*', except do not change the
    first char itself. e.g. 'babble' yields 'ba**le' Assume that the
    string is length 1 or more.
    """
    first = s[0]
    new_word = s[0]
    i = 1

    while i < len(s):
        if s[i] == first:
            new_word = new_word + '*'
        else:
            new_word = new_word + s[i]
        i += 1
        
    return new_word

print(fix_start('babble') == 'ba**le')
print(fix_start('aardvark') == 'a*rdv*rk')
print(fix_start('google') == 'goo*le')
print(fix_start('donut') == 'donut')


def mix_up(a, b):
    """
    Given strings a and b, return a single string with a and b
    separated by a space '<a> <b>', except swap the first 2 chars of
    each string. Assume a and b are length 2 or more.
    """
    return str(b[:2] + a[2:] + " " + a[:2] + b[2:])

print(mix_up('mix', 'pod') == 'pox mid')
print(mix_up('dog', 'dinner') == 'dig donner')
print(mix_up('gnash', 'sport') == 'spash gnort')
print(mix_up('pezzy', 'firm') == 'fizzy perm')


def verbing(s):
    """
    Given a string, if its length is at least 3, add 'ing' to its end.
    Unless it already ends in 'ing', in which case add 'ly' instead.
    If the string length is less than 3, leave it unchanged. Return
    the resulting string.
    """
    if len(s) >= 3:
        if s[len(s) - 3:] == 'ing':
            return str(s + 'ly')
        else:
            return str(s + 'ing')
    else:
        return s

print(verbing('hail') == 'hailing')
print(verbing('swiming') == 'swimingly')
print(verbing('do') == 'do')


def not_bad(s):
    """
    Given a string, find the first appearance of the substring 'not'
    and 'bad'. If the 'bad' follows the 'not', replace the whole
    'not'...'bad' substring with 'good'. Return the resulting string.
    So 'This dinner is not that bad!' yields: 'This dinner is
    good!'
    """
    import re
    tokens = re.split('(\W+)',s)
    bad_regex = "bad"
    not_regex = "not"

    if bad_regex in tokens and not_regex in tokens:
        not_index = tokens.index(not_regex)
        bad_index = tokens.index(bad_regex)
        if not_index < bad_index:

            return str("".join(tokens[:not_index]) + "good" + "".join(tokens[bad_index+1:]))
        else:
            return s
    else:
        return s

print(not_bad('This movie is not so bad') == 'This movie is good')
print(not_bad('This dinner is not that bad!') == 'This dinner is good!')
print(not_bad('This tea is not hot') == 'This tea is not hot')
print(not_bad("It's bad yet not") == "It's bad yet not")


def front_back(a, b):
    """
    Consider dividing a string into two halves. If the length is even,
    the front and back halves are the same length. If the length is
    odd, we'll say that the extra char goes in the front half. e.g.
    'abcde', the front half is 'abc', the back half 'de'. Given 2
    strings, a and b, return a string of the form a-front + b-front +
    a-back + b-back
    """
    a_front = ""
    a_back = ""
    b_front = ""
    b_back = ""

    if len(a) % 2 == 0:
        a_front = a[:(len(a)//2)]
        a_back = a[(len(a)//2):]
    else:
        a_front = a[:(len(a)//2)+1]
        a_back = a[(len(a)//2)+1:]
    if len(b) % 2 == 0:
        b_front = b[:(len(b)//2)]
        b_back = b[(len(b)//2):]
    else:
        b_front = b[:(len(b)//2)+1]
        b_back = b[(len(b)//2)+1:]

    return str(a_front + b_front + a_back + b_back)

print(front_back('abcd', 'xy') == 'abxcdy')
print(front_back('abcde', 'xyz') == 'abcxydez')
print(front_back('Kitten', 'Donut') == 'KitDontenut')
