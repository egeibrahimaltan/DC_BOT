import random
import string

def gen_pass(pass_length):
    elements = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(elements) for _ in range(pass_length))
    return password

def yazi_tura():
    result = random.choice(["YAZI", "TURA"])
    return result
def emoji_olusturucu():
    emoji = ["\U0001f600", "\U0001f642", "\U0001F606", "\U0001F923","\U0001f601" ,"\U0001F603", "\U0001F604	" ,"\U0001F605" ,"\U0001F608" ,"\U0001F60A" ,"\U0001F60B" ,"\U0001F60E	"]
    return random.choice(emoji)