#!/usr/bin/env python
# coding: utf-8

# ## Conditional Basics
# ### a. prompt the user for a day of the week, print out whether the day is Monday or not

# In[13]:


day = input("What day of the week is it: ")
if day.lower() == "monday":
    print("The day is monday")
else:
    print("The day is not monday")


# ### b. prompt the user for a day of the week, print out whether the day is a weekday or a weekend

# In[5]:


day = input("What day of the week is it: ")
if day.lower() in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']:
    print("It is currently a weekday")
else:
    print("It is currently the weekend")


# ### c. create variables and make up values for
# 
# * the number of hours worked in one week
# * the hourly rate
# * how much the week's paycheck will be
# * write the python code that calculates the weekly paycheck. You get paid time and a half if you work more than 40 hours

# In[17]:


hours_worked = float(input("How many hours did you work: "))
hourly_rate = float(input("How much are you paid per hour: "))
overtime = 0.0
paycheck = 0.0
if hours_worked > 40:
    overtime = hours_worked - 40
    hours_worked -= overtime
paycheck = (hours_worked * hourly_rate) + (overtime * (hourly_rate * 1.5))

print(f"Your paycheck comes out to ${paycheck}")


# ## Loop Basics
# ### a. While
# * Create an integer variable i with a value of 5.
# * Create a while loop that runs so long as i is less than or equal to 15
# * Each loop iteration, output the current value of i, then increment i by one.

# In[15]:


i = 5
while i <= 15:
    print(i)
    i += 1


# Create a while loop that will count by 2's starting with 0 and ending at 100. Follow each number with a new line.

# In[18]:


i = 0
while i <= 100:
    print(i)
    i += 2


# Alter your loop to count backwards by 5's from 100 to -10.

# In[1]:


i = 100
while i >= -10:
    print(i)
    i -= 5


# Create a while loop that starts at 2, and displays the number squared on each line while the number is less than 1,000,000. Output should equal:

# In[4]:


i = 2
while i <= 1000000:
    print(i)
    i = i * i


# Write a loop descending from 100 by increments of 5

# In[3]:


i = 100
while i >= 5:
    print(i)
    i -= 5


# ### b. for loops
# Write some code that prompts the user for a number, then shows a multiplication table up through 10 for that number.

# In[18]:


number = int(input("What number would you like to see a multiplication table for: "))
mult = 0
for num in range(1, 11):
    mult = (number * num)
    print(f"{number} x {num} = {mult}")


# Create a for loop that uses print to create the output shown below.

# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777
# 88888888
# 999999999

# In[21]:


count = 1
for num in range(9):
    print(str(count) * count)
    count += 1


# ### C.break and continue
# Prompt the user for an odd number between 1 and 50. Use a loop and a break statement to continue prompting the user if they enter invalid input. (Hint: use the isdigit method on strings to determine this). Use a loop and the continue statement to output all the odd numbers between 1 and 50, except for the number the user entered.

# In[3]:


odd_num = input("Enter an odd number to skip: ")
while(True):
    if odd_num.isdigit() and int(odd_num) % 2 == 1:
        break
    else:
        odd_num = input("That isn't an odd number, input an odd number: ")
odd_num = int(odd_num)
for num in range(1, 51):
    if num % 2 == 0 or num == odd_num:
        continue
    print(f"Here is an odd number: {num}")


# ### d. Input function
# The input function can be used to prompt for input and use that input in your python code. Prompt the user to enter a positive number and write a loop that counts from 0 to that number. (Hints: first make sure that the value the user entered is a valid number, also note that the input function returns a string, so you'll need to convert this to a numeric type.)

# In[10]:


pos_num = input("Please enter a positive number: ")
input_check = True
while(input_check):
    if pos_num.isdigit() and int(pos_num) > 0:
        break
    else:
        pos_num = input("That is an invalid input, please enter a positive number: ")
pos_num = int(pos_num)
for num in range(0, pos_num + 1):
    print(num)


# ### e. Write a program that prompts the user for a positive integer. Next write a loop that prints out the numbers from the number the user entered down to 1.

# In[15]:


pos_num = input("Please enter a positive number: ")
input_check = True
while(input_check):
    if pos_num.isdigit() and int(pos_num) > 0:
        break
    else:
        pos_num = input("That is an invalid input, please enter a positive number: ")
pos_num = int(pos_num)
while pos_num >= 1:
    print(pos_num)
    pos_num -= 1


# ### 3. FizzBuzz
# One of the most common interview questions for entry-level programmers is the FizzBuzz test. Developed by Imran Ghory, the test is designed to test basic looping and conditional logic skills.
# 
# Write a program that prints the numbers from 1 to 100.
# For multiples of three print "Fizz" instead of the number
# For the multiples of five print "Buzz".
# For numbers which are multiples of both three and five print "FizzBuzz".

# In[16]:


for num in range(1, 100):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)


# ### 4. Display a table of powers.
# 
# * Prompt the user to enter an integer.
# * Display a table of squares and cubes from 1 to the value entered.
# * Ask if the user wants to continue.
# * Assume that the user will enter valid data.
# * Only continue if the user agrees to.

# In[1]:


user_check = 'y'
while(user_check.lower() == 'y'):
    num_input = int(input("What number would you like to go up to: "))
    print("Here is your table!")
    print("\nnumber | squared | cubed")
    print("------ | ------- | -----")
    for num in range(1, num_input + 1):
        print("{:<7}|{:<9}|{:<7}".format(num,num**2,num**3))
    user_check = input("Would you like to continue? (y/n): ")


# ### 5. Convert given number grades into letter grades.
# 
# * Prompt the user for a numerical grade from 0 to 100.
# * Display the corresponding letter grade.
# * Prompt the user to continue.
# * Assume that the user will enter valid integers for the grades.
# * The application should only continue if the user agrees to.
# * Grade Ranges:
# 
#     A : 100 - 88
#     B : 87 - 80
#     C : 79 - 67
#     D : 66 - 60
#     F : 59 - 0

# In[7]:


loop_check = 'y'
while(loop_check.lower() == 'y'):
    grade = int(input("Please enter a numerical grade between 0 and 100: "))
    if grade <= 59:
        if grade >= 58:
            print(f"A grade of {grade} is an F+")
        else:
            print(f"A grade of {grade} is an F")
    elif grade <= 66:
        if grade <= 61:
            print(f"A grade of {grade} is a D-")
        elif grade >= 65:
            print(f"A grade of {grade} is a D+")
        else:
            print(f"A grade of {grade} is a D")
    elif grade <= 79:
        if grade <= 68:
            print(f"A grade of {grade} is a C-")
        elif grade >= 78:
            print(f"A grade of {grade} is a C+")
        else:
            print(f"A grade of {grade} is a C")
    elif grade <= 87:
        if grade <= 81:
            print(f"A grade of {grade} is a B-")
        elif grade >= 86:
            print(f"A grade of {grade} is a B+")
        else:
            print(f"A grade of {grade} is a B")
    else:
        if grade <= 89:
            print(f"A grade of {grade} is a A-")
        elif grade >= 99:
            print(f"A grade of {grade} is a A+")
        else:
            print(f"A grade of {grade} is an A")
    loop_check = input("Would you like to continue? (y/n): ")


# ### 6. Create a list of dictionaries where each dictionary represents a book that you have read. Each dictionary in the list should have the keys title, author, and genre. Loop through the list and print out information about each book.
# 
# Prompt the user to enter a genre, then loop through your books list and print out the titles of all the books in that genre.

# In[20]:


books = [
    {
        "title": "Halo: The Fall of Reach",
        "author": "Eric Nylund",
        "genre": "Sci-Fi"
    },
    {
        "title": "Halo: The Flood",
        "author": "William Dietz",
        "genre": "Sci-Fi"
    },
    {
        "title": "Shadows of the Horde",
        "author": "Michael Stackpole",
        "genre": "Fantasy"
    },
    {
        "title": "Out of the Abyss",
        "author": "Steve Kenson",
        "genre": "Fantasy"
    }
]

choice = input("What genre would you like to look at: ")
book_list = []
for book in books:
    if choice == book["genre"]:
        book_list.append(book["title"])
print(book_list)

