"""Diffie-Hellman key exchange example implementation."""

import random
random.seed(42)


def generate_shared_key(h, exp, p):
    """Return the shared secret computed via modular exponentiation.

    Args:
        h: Public value received from the peer.
        exp: Secret exponent used to derive the shared value.
        p: Prime modulus used in the exchange.

    Returns:
        The computed shared key value.
    """
    k = (h ** exp) % p
    return k


class Initiator:
    """Diffie-Hellman initiator that generates a public value and key."""

    def __init__(self):
        """Initialize the initiator with a random modulus, base, and secret."""
        self.p = random.randint(1, 50) # prime
        self.g = random.randint(1, 50) # base
        self.secret_x = random.randint(1, 50)

    def calculate_ha(self):
        """Compute the initiator's public value."""
        self.ha = (self.g ** self.secret_x) % self.p

    def send_p_and_g(self):
        """Return the prime modulus and generator for the peer.

        Returns:
            A tuple of ``(p, g)`` values.
        """
        return self.p, self.g

    def make_shared_key(self, hb):
        """Compute the shared secret using the receiver's public value.

        Args:
            hb: Public value sent by the receiver.
        """
        self.shared_key = generate_shared_key(hb, self.secret_x, self.p)


class Receiver:
    """Diffie-Hellman receiver that derives a shared secret."""

    def __init__(self):
        """Initialize the receiver with a random secret exponent."""
        self.secret_y = random.randint(1, 50)

    def calculate_hb(self, **kwargs):
        """Compute the receiver's public value from the shared parameters.

        Args:
            **kwargs: Keyword arguments containing ``g`` and ``p``.
        """
        self.g = kwargs['g']
        self.p = kwargs['p']
        self.hb = (self.g ** self.secret_y) % self.p

    def make_shared_key(self, ha):
        """Compute the shared secret using the initiator's public value.

        Args:
            ha: Public value sent by the initiator.
        """
        self.shared_key = generate_shared_key(ha, self.secret_y, self.p)


def main():
    """Run a simple Diffie-Hellman exchange and report whether keys match.

    Returns:
        True if the initiator and receiver compute the same shared key.
    """
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
