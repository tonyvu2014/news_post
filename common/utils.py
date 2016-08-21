import uuid
from functools import wraps


def generate_uuid():
    return uuid.uuid4()
    
    
def unpack_args(func):
    @wraps(func)
    def wrapper(args):
        if isinstance(args, dict):
            return func(**args)
        else:
            return func(*args)
    return wrapper
    
    
if __name__ == '__main__':
    print generate_uuid()