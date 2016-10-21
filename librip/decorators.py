def print_result(func):
    def decorated_func(*args):
        print(func.__name__)
        if len(args) > 0:
            a = func(args[0])
        else:
            a = func()
        if type(a) is list:
            print("\n".join(map(str,a)))
        elif type(a) is dict:
            print('\n'.join([str(x)+"="+str(a[x]) for x in a]))
        else:
            print(a)
        return(a)
    return decorated_func

