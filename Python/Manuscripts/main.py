# different printing examples
print("Hello world")
print("Hello again")
print("I like typing this")
print("This is fun")
print("Yay! Printing")
print("I'd much rather you 'not'.")
print('I "said" do not touch this.')

# Basic number operations
# Add two numbers
num1 = 3
num2 = 5
sum_of_nums = num1 + num2
print("Sum is equal:", sum_of_nums)

# basics working with strings
s = "hi"
print(s[1])
print(len(s))
print(s + 'there')

pi = 3.14
# text = "the value of pi is " + pi # does not work - string and float cannot be concatenated.
text = "the value of pi is " + str(pi)

raw = r'this\t\n and that'
print(raw)

multi = """It was the best of times.
It was the worst of times"""

# s.lower(), s.upper() This one returns the uppercase or lowercase string's version
print("Original TEXT + 'TEXT'.lower(): " + "TEXT".lower())
print("Original text + 'text'.upper(): " + "text".upper())
# s.strip() returns a string; the whitespace in this case is removed from the beginning and end
print("   Text    ".strip())
# s.isalpha()/s.isdigit()/s.isspace()... this one checks whether all the string chars are in the different character classes
print("check if a is alpha: " + str("a".isalpha()))
print("check if 1 is alpha: " + str("1".isalpha()))
print("check if a is digit: " + str("a".isdigit()))
print("check if 1 is digit: " + str("1".isdigit()))
print("check if 1 is space: " + str("1".isspace()))
print("check if   is space: " + str(" ".isspace()))
# s.startswith('other'), s.endswith('other') it tests or checks whether the string is starting or ending with the other string in questions
print("startswith test 'starttext' if starts with start: " + str("starttext".startswith("start")))
print("startswith test 'starttext'  if starts with end: " + str("starttext".startswith("end")))
print("endswith test 'starttext' if ends with text: " + str("starttext".endswith("text")))
print("endswith test 'starttext' if ends with end: " + str("starttext".endswith("end")))
# s.find('other') this one runs a search fro the other string in question (but not the usual expression) inside s and then returns the initial index where it is beginning or -1 if it's not found
print("find functionality - check other in string 'something other': " + str("something other".find("other")))
# s.replace('old','new') this one returns a string in which the 'old' occurrences have been substituted by 'new'
print("replace functionality replace new to old in 'new world order': " + str("new world order".replace("new", "old")))
# s.split('delim') it returns a substrings list separated by some delimiter. The delimiter is not some regular expression but a text. Consider 'aaa,bbb,ccc'.split(',') -> ['aaa','bbb','ccc'] s.split() without any arguments splits on all the whitespace chars- as a useful special case
print("split with comma example for 'a,b,c,d':" + str("a,b,c,d".split(',')))
# slice example
print("Hello - slice 1:4: " + "Hello"[1:4])
print("Hello - slice :-4: " + "Hello"[:-3])

# Lists example
colors = ['red', 'blue', 'green']
print(colors[0])  # red

# combining lists
colors2 = ['yellow']
colors3 = colors + colors2
print(colors3)

# for example
squares = [1, 4, 9, 16]
sum = 0
for num in squares:
    sum += num
print("suma liczb " + str(squares) + " to: " + str(sum))

# in example
list = ['larry', 'curly', 'moe']
if 'curly' in list:
    print("yay! curly is in list called list")

# tuple
t = 'a', 'b', 'c', 'd', 'e'
print("Typ t = 'a', 'b', 'c', 'd', 'e' to: " + str(type(t)))
# definition of one element tuple
t0 = 'a',
print(type(t))
# different methods of defining tuple
t1 = ('a', 'b', 'c', 'd', 'e')
print(t1)
t2 = tuple("Kot")
print(t2)
t3 = ('a', '2', '.', 'AAA', '-25.12')
print(t3)
# splitting tuple
print(t3[1:3])
# joining tuple
print(t+t3)
