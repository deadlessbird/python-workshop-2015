# -*- coding: utf-8 -*-
"""
Created on Mon Jun 08 11:03:37 2015

@author: d
"""

print "test all things"

for i in range(5):
    print i
    
def flip_a_string(my_str):
        """
          Take a string and invert it, ie:
          >>> flip_a_sting("Jeb")
          "beJ"
        """
        my_list=list(my_str)
        my_list.reverse()
        my_str="".join(my_list)
        return my_str          # or return "".join(my_list)  

def am_i_greater_than_forty(num):
    """ check whether a number is indeed greater than forty
    Returns a Boolean """
    return num>40
    

def is_this_greater_than_forty(num):
    """ Return 'Yes" if the number is greater than 40, 'No' otherwise 
    """
    if am_i_greater_than_forty(num):
        return "Yes"
    else:
        return "No"

def the_third_element(my_list):
    """
    Return the 3rd element in a mapping
    """
    #1: return my_list[2]
    try:
        return my_list[2]
    except TypeError:
        print "Ooops, what are you thinking?"
        """ or:
        user_val=raw_input("Type something in here")
        print "You typed:"+user_val
        """
    
def which_numbers_are_greater_than_forty(num_list):
    """
    Returns a list of Boolean objects depending on
    whether each number is greater than 40
    """
    """
    for i in len(num_list):
        if num_list[i-1]>40:
            return "Yes"
        else:
            return "No"
    """
    my_list=[]
    for i in num_list:
        my_list.append(am_i_greater_than_forty(i))
    return my_list
    
    
    
    
    
    
