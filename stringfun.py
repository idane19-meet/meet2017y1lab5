def string_test(s):
    if len(s) > 2 and s[0] == s[-1]:
       return True
    else:
        return False


def add_x(s):
    s = 'x' + s + 'x'
    return(s)
