import re

def is_valid_email(addr):
    valid_str=r'^[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}$'
    if re.match(valid_str,addr):
        return True
    else :
        return False

if __name__ == "__main__":
    while True:
        a = input("email:")
        if(is_valid_email(a)):
            print("yes")
        else:
            print("no")