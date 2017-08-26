# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

### Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Lists and tuples are similar because they can hold a sequence values of different types. However, lists are mutable (can be changed) data types, whereas tuples are immutable (cannot be changed). Lists will not work as keys in a dictionary since a dictionary calculates a hash value to store data at a certain place in memory, and relies on that hash to find the data again. Those hashes are re-calculated if the key changes, and the original hash is lost.

---

### Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Lists and sets differ in that a list will allow duplicate values, while a set will not. Additionally, lists are ordered sequences of values while sets do not retain order.  

```python
>>> list_example = ['a', 'b', 1, 2, 1.0, 1.5]
>>> print list_example
['a', 'b', 1, 2, 1.0, 1.5]
>>> set_example = set(list_example)
>>> print set_example
set(['a', 1, 2, 'b', 1.5])
```

>> Sets are faster than lists when it comes to finding if an element exists because sets create hashes for each element in the set similarly to how a dictionary stores hashes for its keys.

---

### Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> `lambda` is a keyword that allows creation of a nameless function without use of the traditional definition of a function. Lambda functions can have any number of arguments, but only one expression. It can be used to perform operations that will likely not be used again later in a body code (e.g. use as a key function argument to the `sorted()` function). For example:  

```python
people = [('John', 44), ('Mary', 29), ('Steven', 12), ('Raj', 31)] # if x is each tuple, x[0] is name and x[1] is age
print(sorted(people, key=lambda x: x[1])) # returns a sorted list of tuples by age
```

---

### Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehensions are part of the Python syntax used for transforming a list into another list, where list elements can be conditionally included in the new list. This is similar to combining the capability of `lambda`, `map()` and `filter()` functions into a more concise, readable syntax. In this way, we can write a list comprehension that returns a filtered new list that has been transformed by a given expression. For example:  

```python
# transform list of ints to string results of the int divided by 2, only if the int is divisible by 2
int_list = range(1,11)
div_by_two = [str(x/2) for x in int_list if x%2 == 0]
print(div_by_two) #returns ['1', '2', '3', '4', '5']

# equivalent to above list comprehension using built-in map(), filter(), and lambda functions
div_by_two = map(lambda x: str(x/2), conditionals, filter(lambda x: x%2 == 0, int_list))
print(div_by_two)

# dictionary comprehension that stores an int key and cube of key as value
dict_comp = {x : x**3 for x in range(10)}

# dictionary comprehension that stores names (as tuples of strings) and ages if age is less than 25
names_and_ages = [('Robert', 'Johnson', 28), ('Otis', 'Redding', 23), ('Mick', 'Jagger', 26), ('Muddy', 'Waters', 25), ('Etta', 'James', 19)]
names_ages_dict = {(first_name, last_name) : age for (first_name, last_name, age) in names_and_ages if age < 25} # returns {('Otis', 'Redding'): 23, ('Etta', 'James'): 19}

# set comprehension that stores unique cubes of randomly generated ints between 1 and 10
from random import randint
randoms = [randint(1,10) for x in range(20)]
set_comp = {x**3 for x in randoms}
```

>> It should also be noted that list comprehensions provide an easy syntax for creating new nested lists, where nested for loops, `lambda`, `map()` and `filter()` cannot do so. For example:  

```python
foods = ['ham', 'eggs', 'spam']
drinks = ['water', 'tea', 'juice']
calories = {'ham' : 19, 'eggs' : 48, 'spam' : 35, 'water' : 0, 'tea': 4, 'juice' : 20}

possible_choices = [ [food, drink, calories[food] + calories[drink]] for drink in drinks for food in foods ]
print(possible_choices) # returns nested list of the possible combinations of drinks and foods along with total calories for each combination
```

---

### Complete the following problems by editing the files below:

### Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> 937

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> 513

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> 7850

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

### Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

### Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

### Q8. Parsing
Write a script as indicated (using the football data) in [q8_parsing.py](python/q8_parsing.py)





