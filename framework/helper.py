import random
import string
from faker import Faker

fake = Faker()
Faker.seed(0)


def generate_text_field(size):
    return "".join(random.choice(string.ascii_letters) for i in range(size))


def gen_title():
    size = random.randint(1, 11)
    return generate_text_field(size)


def gen_body():
    size = random.randint(1, 31)
    return generate_text_field(size)


def gen_comment_data(post_id):
    data = {
        "postId": str(post_id),
        "name": fake.sentence(nb_words=3),
        "body": fake.paragraph(nb_sentences=3),
        "email": fake.email(),
    }
    return data
