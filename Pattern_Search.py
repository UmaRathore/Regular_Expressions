import re

text = 'Search for a word in Regular Expression! For each Search say hurry!!'

# here is a simple operation in String but Regular Expression can do more than just search and return true
print('Search' in text)

# saving the object return by re.search so that certain operations can be performed
expression_obj_one = re.search('Search', text)
print(f'Pattern match returns object : {expression_obj_one}')

# returns the start and end point of the pattern as a tuple
print(f'Span of the pattern : {expression_obj_one.span()}')

# returns the start index
print(f'start index : {expression_obj_one.start()}')

# returns the end index
print(f'End index : {expression_obj_one.end()}')

# return the Pattern to be searched
print(f'{expression_obj_one.group()}')

expression_obj_two = re.search('Serch', text)
print(f'Pattern does not match returns : {expression_obj_two}')

# compile the pattern and several operations can be performed
pattern = re.compile('Search')
expression_obj_three = pattern.search(text)
print(f'Searched pattern is : {expression_obj_three.group()}')

# returns list of all searched patterns that is 'Search'
expression_obj_four = pattern.findall(text)
print(f'All searched pattern : {expression_obj_four}')

text_fullmatch = 'Hello there! Hey'
pattern_fullmatch = re.compile('Hello there!')

# Returns None as it does not match the exact string
expression_obj_five = pattern_fullmatch.fullmatch(text_fullmatch)
print(f'Exact match of String : {expression_obj_five}')

# returns search object as it matches some part of the string
expression_obj_six = pattern_fullmatch.match(text_fullmatch)
print(f'Match of String : {expression_obj_six}')
