try:
    import random
except ModuleNotFoundError:
    print('Module not found.')
    exit()


def ps_gen(length=1):
    """
    Generates a random password from the string 's'
    """
    s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*/?abcdefghijklmnopqrstuvwxyz"
    pw = "".join(random.sample(s, length))
    return pw
