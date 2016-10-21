def print_result(func):
    def decorated_func(*args, **kwargs):
        print(func.__name__)
        a = func(*args, **kwargs)
        if type(a) is list:
            print("\n".join(map(str,a)))
        elif type(a) is dict:
            print('\n'.join([str(x)+"="+str(a[x]) for x in a]))
        else:
            print(a)
        return a
    return decorated_func



