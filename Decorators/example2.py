from decorators import Decorators
import time

@Decorators.timer
@Decorators.api_generator
def main(key):
    return key

if __name__ == '__main__':
    '''
    Couple examples to demonstrate work
    '''
    print(f"Printing 16 byte size URL safe key {main(16)}")
    print(f"Printing 32 byte size URL safe key {main(32)}")
    