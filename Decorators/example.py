from decorators import Decorators

@Decorators.timer
@Decorators.check_connectivity
def main():
    return True

if __name__ == '__main__':
    '''
    Assert statements to check functionality is working as expected
    '''

    assert main("google.com", 443) is True
    assert main("google.com", 1000) is False
    assert main("google.com", 0) is False
    assert main("google.com", 80) is True