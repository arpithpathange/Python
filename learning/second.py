#usr/bin/python

import os


def main():
    print "In the Main function"
    first()
    
    
def first():
    print "In first function"
    sec()
    
def sec():
    print "In sec"
    


if __name__ == '__main__':
    for x in range(0,5):
        main()