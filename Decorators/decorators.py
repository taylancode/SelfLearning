'''
To contain all decorators to be used for practice
'''
import socket
import secrets
from functools import wraps
from time import time

class Decorators():

    '''
    Decorator class containing all decorators

    Execution for decorators # decorator(function)(func)
    '''

    def check_connectivity(func) -> bool:
        @wraps(func)
        def is_reachable(dest: str , port: int):

            '''
            Function:
                - Decorator to check reachability to host before performing any function

            Params:
                - dest: String containing host address or fqdn
                - port: Port number (Integer)

            Returns:
                - Bool in this instance for testing
            '''
            try:
                sock = socket.socket()
                sock.connect((dest, port))
                return func()
            except (TimeoutError, OSError):
                return False
            finally:
                sock.close()

        return is_reachable

    def api_generator(func) -> str:
        @wraps(func)
        def api_key(byte_size: int) -> str:
            '''
            Function:
                - Decorator to demonstrate API key generation (this is only local for demonstration purposes)
                - Could be used with systems that require actively changing API keys (would be done via their generation process)

            Params:
                - byte_size: size of key to generate in bytes. 32 or higher is recommended.
            
            Returns:
                - String value of key passed to called function
            '''
            key = secrets.token_urlsafe(byte_size)
            return func(key)
        return api_key
    
    def timer(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            '''
            Function:
                - Decorator that can be added to any function to time it

            Params:
                - Takes the function and all its argument

            Returns:
                - Called function and its args
            '''
            start = time()
            result = func(*args, **kwargs)
            end = time()
            print('Function: %r took: %.6f sec' % (func.__name__, end-start))
            return result
        return wrapper