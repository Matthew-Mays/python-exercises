#!/usr/bin/env python
# coding: utf-8

# ### 1. Define a function named is_two. It should accept one input and return True if the passed input is either the number or the string 2, False otherwise.

# In[142]:


# is_two defines a single parameter, num that is either a string or an int, and will return a boolean value.
def is_two(num):
    # check to see if the argument is either a string or an int
    assert type(num) == str or type(num) == int, "input must be a str or int"
    # if the arguement is an int, it then checks to see if said arguement is equal to 2
    if num == 2:
        # returns true if the num is equal to 2
        return True
    # if the arguement is a string, it then checks to see if the string is "two" regardless of case
    elif str(num) == "2":
        #returns true if the string is equal to two
        return True
    # if neither of these are true the function returns false
    else:
        return False


# In[143]:


print(is_two(2))
print(is_two("2"))
print(is_two(3))
print(is_two("two"))


# ### 2. Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.

# In[23]:


# is_vowel defines a single parameter, ltr that is a str, it then returns a boolean value
def is_vowel(ltr):
    # assert to check if the input, ltr, is a string
    assert type(ltr) == str, "input must be a str"
    # checks ltr to see if it is in any of the letters a, e, i, o, u
    if ltr in "aeiou":
        # if it
        return True
    else:
        return False
    


# In[25]:


print(is_vowel("a"))
print(is_vowel("b"))
print(is_vowel("and"))


# ### 3. Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. Use your is_vowel function to accomplish this.

# In[42]:


def is_consonant(ltr):
    if is_vowel(ltr) == False:
        return True
    else:
        return False


# In[43]:


print(is_consonant("a"))
print(is_consonant("b"))


# ### 4. Define a function that accepts a string that is a word. The function should capitalize the first letter of the word if the word starts with a consonant.

# In[13]:


def con_cap(word):
    assert type(word) == str
    if is_consonant(word[0:1]) == True:
        cap_word = word.capitalize()
        return cap_word


# In[14]:


print(con_cap("banana"))
print(con_cap("apple"))


# ### 5. Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.

# In[34]:


def calculate_tip(percent, bill):
    assert type(percent) == float, "input must be a float"
    assert type(bill) == float, "input must be an int"
    tip = (bill * percent)
    return tip


# In[45]:


print(f"The amount you should tip is ${calculate_tip(.25, 50.0)}")


# ### 6. Define a function named apply_discount. It should accept a original price, and a discount percentage, and return the price after the discount is applied.

# In[40]:


def apply_discount(price, disc):
    assert type(price), type(disc) == float
    disc_price = price - (price * disc)
    return disc_price


# In[46]:


print(f"The discounted ammount is : ${apply_discount(250.0, .5)}")
print(f"The discounted ammount is : ${apply_discount(233.5, .35)}")


# ### 7. Define a function named handle_commas. It should accept a string that is a number that contains commas in it as input, and return a number as output.

# In[48]:


def handle_commas(str_num):
    no_comma = str_num.replace(",", "")
    no_comma = int(no_comma)
    return no_comma


# In[50]:


print(handle_commas("1,000,000"))
print(type(handle_commas("1,000,000")))


# ### 8. Define a function named get_letter_grade. It should accept a number and return the letter grade associated with that number (A-F).

# In[53]:


def get_letter_grade(grade):
    assert type(grade) == int, "The input must be an int"
    if grade >= 88:
        return 'A'
    elif grade >= 80:
        return 'B'
    elif grade >= 67:
        return 'C'
    elif grade >= 60:
        return 'D'
    else:
        return 'F'


# In[54]:


print(get_letter_grade(89))
print(get_letter_grade(73))
print(get_letter_grade(42))


# ### 9. Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.

# In[55]:


def remove_vowels(string):
    assert type(string) == str, "The input must be a str"
    new_string = string
    for letter in new_string:
        if letter in "aeiou":
            new_string = new_string.replace(letter, "")
    return new_string


# In[56]:


print(remove_vowels("banana"))


# ### 10. Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:

# In[62]:


def normalize_name(name):
    assert type(name) == str, "The input must be a str"
    normalized = name
    for letter in name:
        if letter in "!@#$%^&*()+=-[]{}\/|?.<>,`~":
            normalized = normalized.replace(letter, '')
    normalized = normalized.lstrip()
    normalized = normalized.rstrip()
    normalized = normalized.replace(' ', '_')
    normalized = normalized.lower()
    return normalized


# In[63]:


print(normalize_name("Name"))
print(normalize_name("First Name"))
print(normalize_name("% Completed"))


# ### 11. Write a function named cumulative_sum that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.

# In[57]:


def cumulative_sum(num_list):
    assert type(num_list) == list, "The input must be a list"
    for ele in num_list:
        assert type(ele) == int, "Every element in the list must be an int"
    sum_list = []
    hold = 0
    for num in num_list:
        sum_list.append(num + hold)
        hold += num
    return sum_list


# In[144]:


print(cumulative_sum([1, 1, 1]))
print(cumulative_sum([1, 2, 3, 4]))


# ### Bonus: Create a function named twelveto24. It should accept a string in the format 10:45am or 4:30pm and return a string that is the representation of the time in a 24-hour format.

# In[136]:


# Here's a way to create this function without imports.
# def twelveto24(time):
#     new_time = ""
#     if time[-2:] == "am":
#         time = time.strip("am")
#         time = time.split(":")
#         if len(time[0]) == 1:
#             time[0] = "0" + time[0]
#         time.insert(1, ":")
#         for ele in time:
#             new_time += ele 
#         return new_time
#     elif time[-2:] == "pm":
#         time = time.strip("pm")
#         time = time.split(":")
#         time[0] = str(int(time[0]) + 12)
#         time.insert(1, ":")
#         for ele in time:
#             new_time += ele 
#         return new_time


# In[137]:


# print(twelveto24("10:23pm"))


# In[1]:


# This is a function that does the same with imports.
from datetime import datetime as dt

def twelveto24(time):
    assert type(time) == str, "The input must be a str"
    raw_time = dt.strptime(time, "%I:%M%p")
    true_time = dt.strftime(raw_time, "%H:%M")
    return true_time


# In[2]:


print(twelveto24("10:45pm"))


# ### Bonus: Write a function that does the opposite.

# In[4]:


def twelvefrom24(t):
    assert type(t) == str, "The input must be a str"
    raw_time = dt.strptime(t, "%H:%M")
    new_time = raw_time.strftime("%-I:%M%p")
    return new_time
print(twelvefrom24("14:34"))


# ### Bonus: Create a function named col_index. It should accept a spreadsheet column name, and return the index number of the column.
# * col_index('A') returns 1
# * col_index('B') returns 2
# * col_index('AA') returns 27

# In[136]:


def excel_col(col):
    letters = 'A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z'
    letters = letters.split(',')
    col = col.upper()
    if len(col) == 1:
        for ele in letters:
            if ele == col:
                index = letters.index(ele) + 1
    elif len(col) == 2:
        for ele in letters:
            if ele == col[1]:
                index = letters.index(ele) + 1
                for ele in letters:
                    if ele == col[0]:
                        index = index + (26 * (letters.index(ele) + 1))
    elif len(col) == 3:
        for ele in letters:
            if ele == col[2]:
                index = letters.index(ele) + 1
                for ele in letters:
                    if ele == col[1]:
                        index = index + (26 * (letters.index(ele) + 1))
                        for ele in letters:
                            if ele == col[0]:
                                index = index + (26**2 * (letters.index(ele) + 1))
    return index


# In[139]:


excel_col('baa')


# In[ ]:




