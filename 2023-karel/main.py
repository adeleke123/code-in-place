from karel.stanfordkarel import *

"""
File: 2021.py
--------------------
When you finish writing this file, Karel should be able to 
place 20 beepers, then 23 beepers, and end facing East to 
the right of the 23 beepers.
"""

def main():
    # Place 20 beepers
    for i in range(20):
        put_beeper()
    
    # Move one step
    move()
    
    # Place 23 beepers
    for i in range(23):
        put_beeper()
    
    # Move one more step
    move()

if __name__ == '__main__':
    main()
