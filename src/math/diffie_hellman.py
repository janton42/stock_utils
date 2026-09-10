import random
random.seed(42)

def generate_shared_key(h, exp, p):
    k = (h ** exp) % p
    return k

class Initiator:
    def __init__(self):
        self.p = random.randint(1, 50) # prime
        self.g = random.randint(1, 50) # base
        self.secret_x = random.randint(1, 50)

    def calculate_ha(self):
        self.ha = (self.g ** self.secret_x) % self.p

    def send_p_and_g(self):
        return self.p, self.g

    def make_shared_key(self, hb):
        self.shared_key = generate_shared_key(hb, self.secret_x, self.p)

class Receiver:
    def __init__(self):
        self.secret_y = random.randint(1, 50)

    def calculate_hb(self, **kwargs):
        self.g = kwargs['g']
        self.p = kwargs['p']
        self.hb = (self.g ** self.secret_y) % self.p

    def make_shared_key(self, ha):
        self.shared_key = generate_shared_key(ha, self.secret_y, self.p)

def main():
    i = Initiator()
    r = Receiver()
    i.calculate_ha()
    r.calculate_hb(g=i.g, p=i.p)
    i.make_shared_key(r.hb)
    r.make_shared_key(i.ha)
    print(f'Initiator Diffie Hellman: {i.ha}')
    print(f'Receiver Diffie Hellman: {r.hb}')
    print(f'Shared key match?')
    return i.shared_key == r.shared_key

if __name__ == '__main__':
    print(main())
