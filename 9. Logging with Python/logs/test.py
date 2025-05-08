from logger import logging

def add(a,b):

    logging.debug("The addition is taking place")
    return a+b

logging.debug('The function add is called')
print(add(1,2))
