import random
import string


def rand_str(N=10):
    return ''.join(random.choices(string.ascii_lowercase+ string.ascii_uppercase + string.digits, k=N))
