from generators import Generators

def main():
    '''
    Simple example of generator, adding 1 from 0 until exhaustion (in this case 1000)
    '''
    new_num = 0
    plus1 = Generators.plus_1(new_num)

    while True:
        try:
            new_num = next(plus1)
            print(new_num)
        except StopIteration:
            raise SystemExit

if __name__ == '__main__':
    main()