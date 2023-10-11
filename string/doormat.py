'''
Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

Mat size must be X. ( is an odd natural number, and  is  times .)
The design should have 'WELCOME' written in the center.
The design pattern should only use |, . and - characters.

Sample Designs

    Size: 7 x 21 
    ---------.|.---------
    ------.|..|..|.------
    ---.|..|..|..|..|.---
    -------WELCOME-------
    ---.|..|..|..|..|.---
    ------.|..|..|.------
    ---------.|.---------
    
    Size: 11 x 33
    ---------------.|.---------------
    ------------.|..|..|.------------
    ---------.|..|..|..|..|.---------
    ------.|..|..|..|..|..|..|.------
    ---.|..|..|..|..|..|..|..|..|.---
    -------------WELCOME-------------
    ---.|..|..|..|..|..|..|..|..|.---
    ------.|..|..|..|..|..|..|.------
    ---------.|..|..|..|..|.---------
    ------------.|..|..|.------------
    ---------------.|.---------------

Input Format
A single line containing the space separated values of  and .


Output Format
Output the design pattern.

Sample Input
9 27

Sample Output
------------.|.------------
---------.|..|..|.---------
------.|..|..|..|..|.------
---.|..|..|..|..|..|..|.---
----------WELCOME----------
---.|..|..|..|..|..|..|.---
------.|..|..|..|..|.------
---------.|..|..|.---------
------------.|.------------

'''


def doormat(n, m):
    pattern = '.|.'
    pattern_len = len(pattern)
    j = 1
    for i in range(1, n+1):
        if i < n/2:
            print('-'*((m-(pattern_len*j))//2) + (pattern*j) + '-'*((m-(pattern_len*j))//2))
            j += 2
        elif i == int(n/2)+1:
            print('-'*int((m-7)/2) + 'WELCOME' + '-'*int((m-7)/2))
            j -= 2
        else:
            print('-'*((m-(pattern_len*j))//2) + (pattern*j) + '-'*((m-(pattern_len*j))//2))
            j -= 2
    

if __name__ == '__main__':
    n, m = map(int, input().split())
    doormat(n ,m)


