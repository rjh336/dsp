# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0


def match_ends(words):
    """
    Given a list of strings, return the count of the number of strings
    where the string length is 2 or more and the first and last chars
    of the string are the same.
    """
    return len([ x for x in words if len(x) >= 2 and x[0] == x[len(x)-1] ])

print match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']) == 3
print match_ends(['', 'x', 'xy', 'xyx', 'xx']) == 2
print match_ends(['aaa', 'be', 'abc', 'hello']) == 1


def front_x(words):
    """
    Given a list of strings, return a list with the strings in sorted
    order, except group all the strings that begin with 'x' first.
    e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields
         ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'].
    """
    x_words = sorted([word for word in words if word[0] == 'x'])
    words = sorted([word for word in words if word[0] != 'x'])
    return x_words + words

print front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']) == ['xaa', 'xzz', 'axx', 'bbb', 'ccc']
print front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']) == ['xaa', 'xcc', 'aaa', 'bbb', 'ccc']
print front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']) == ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
    

def sort_last(tuples):
    """
    Given a list of non-empty tuples, return a list sorted in
    increasing order by the last element in each tuple.
    e.g. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields
         [(2, 2), (1, 3), (3, 4, 5), (1, 7)].
    """
    return sorted( tuples, key=lambda x: x[len(x)-1] )

print sort_last([(1, 3), (3, 2), (2, 1)]) == [(2, 1), (3, 2), (1, 3)]
print sort_last([(2, 3), (1, 2), (3, 1)]) == [(3, 1), (1, 2), (2, 3)]
print sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)]) == [(2, 2), (1, 3), (3, 4, 5), (1, 7)]


def remove_adjacent(nums):
    """
    Given a list of numbers, return a list where all adjacent equal
    elements have been reduced to a single element, so [1, 2, 2, 3]
    returns [1, 2, 3]. You may create a new list or modify the passed
    in list.
    """
    if len(nums) < 2: return nums

    i = 1
    new = []

    while i < len(nums):
        if nums[i] != nums[i-1] and i != (len(nums) -1):
            new.append(nums[i-1])
            i += 1
        elif nums[i] != nums[i-1] and i == (len(nums) -1):
            new.append(nums[i-1])
            new.append(nums[i])
            i += 1
        elif nums[i] == nums[i-1] and i == (len(nums) -1):
            new.append(nums[i])
            i += 1
        else:
            i += 1

    return new

print remove_adjacent([1, 2, 2, 3]) == [1, 2, 3]
print remove_adjacent([2, 2, 3, 3, 3]) == [2, 3]
print remove_adjacent([3, 2, 3, 3, 3]) == [3, 2, 3]
print remove_adjacent([]) == []
    

def linear_merge(list1, list2):
    """
    Given two lists sorted in increasing order, create and return a
    merged list of all the elements in sorted order. You may modify
    the passed in lists. Ideally, the solution should work in "linear"
    time, making a single pass of both lists.
    """
    merged_list = []
    i = 0
    j = 0
    total = len(list1) + len(list2)

    while len(merged_list) != total:
        if len(list1) == i:
            merged_list += list2[j:]
            break
        elif len(list2) == j:
            merged_list += list1[i:]
            break
        elif list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1

    return merged_list

print linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc']) == ['aa', 'bb', 'cc', 'xx', 'zz']
print linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz']) == ['aa', 'bb', 'cc', 'xx', 'zz']
print linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb']) == ['aa', 'aa', 'aa', 'bb', 'bb']
