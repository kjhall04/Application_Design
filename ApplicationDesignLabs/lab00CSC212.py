# -*- coding: utf-8 -*-
"""
CSC 122, 212, 222 LAB 3

Created by KALEB HALL
20 AUG 2024

Collaborators:
    NONE

This program asks whether you enjoyed the lecture, and returns the answer 'YES'.

Output:

    Did you enjoy the lecture? (Y/N)

    YES
    
NOTE: Replace NAME after 'Created by' with your name. Replace NAME under 
'Collaborators' with the names of students that helped you or that you helped.
Use docstrings in your functions. Remember to delete 'pass' after you type code
in the functions, the try block, or the except block. DO NOT SUBMIT THE SAME 
CODE AS ANOTHER STUDENT.

"""

import time

# global variables


# functions

def run(strg = 'Did you enjoy the lecture? (Y/N)\n'):
    print(strg)
    time.sleep(1.5)
    print('YES\n')

# main
    
if __name__=='__main__':
      
    try:

        run()

    except KeyboardInterrupt:  

        pass
