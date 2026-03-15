def make_pretty(func):
    def inner():
        print("I got decorated")
        func()

    return inner


@make_pretty
def ordinary():
    print("I am ordinary")


def smart_divide(func):
    def inner(a, b):
        print("I am going to divide ", a, "and", b)
        if b == 0:
            print("Whoops! cannot divide")
            return
        return func(a, b)

    return inner


def star(func):
    def inner(*args, **kwargs):
        print("*" * 15)
        func(*args, **kwargs)
        print("*" * 15)

    return inner


@star
@smart_divide
def divide(a, b):
    print(a / b)


ordinary()

divide(5, 10)
divide(5, 0)
