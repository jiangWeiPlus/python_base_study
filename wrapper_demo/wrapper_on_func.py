# coding = utf-8

import datetime

def log(func):
    def wrapper(*args, **kv):
        print('current time: ', datetime.datetime.now())
        return func(*args, **kv)
    return wrapper

@log
def main():
    print('I am main.')
    

main()
