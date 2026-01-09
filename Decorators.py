def decorator(func):
    def inner():
        print('Decorator is running')
        func()
        print('Decorator is finished')

    return inner
@decorator
def greet():
    print('Hello Python')


greet()
