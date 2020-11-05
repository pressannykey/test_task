import random
import string


def generate_text_field(size):
    return "".join(random.choice(string.ascii_letters) for i in range(size))


def gen_title():
    size = random.randint(1, 11)
    return generate_text_field(size)


def gen_body():
    size = random.randint(1, 31)
    return generate_text_field(size)
