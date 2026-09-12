"""Heron's formula for triangle area calculation."""


def main(a:int, b:int, c:int)->int:
    """Return the area of a triangle using Heron's formula.

    Args:
        a: Length of the first side.
        b: Length of the second side.
        c: Length of the third side.

    Returns:
        The area of the triangle.
    """
    s = (a + b + c)/2
    area = (s * ((s-a)*(s-b)*(s-c))) ** 0.5
    return area



if __name__=='__main__':
    a = int(input(f'Enter the first length: '))
    b = int(input(f'Enter the second length: ' ))
    c = int(input(f'Enter a third length (must be less than {a + b}): '))
    print(f'a = {type(a)}, b = {type(b)}, c = {type(c)}')
    while c > (a + b):
        print(f'The value {c} is too large')
        c = int(input(f'Enter a length less than {a + b}: '))
    area_of_a_triangle = main(a,b,c)
    output = f'The area is {area_of_a_triangle}'
    print(output)
