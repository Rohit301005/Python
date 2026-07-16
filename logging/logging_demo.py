
import logging

logging.basicConfig(level=logging.DEBUG,filename="demo.log")

def nameCheck(name):

    if len(name) < 2:
        logging.debug("Short name")
        return "Invalid name"
    elif name.isspace():
        logging.debug("Name is space")
        return "Invalid name"
    elif name.isdigit():
        logging.debug("Name is digit")
        return "Invalid name"
    else:
        logging.debug("Valid name")
        return "Valid name"
    

print(nameCheck("John"))

        

