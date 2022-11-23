from generators import Generators

def main():
    '''
    Demonstrating generator usage with some sample XML Data
    Will iterate over the data until exhausted
    '''
    xml = Generators.xml()

    while True:
        try:
            print(next(xml))

        except StopIteration:
            raise SystemExit

if __name__ == '__main__':
    main()