"""Multiplication table generator."""


def multiplication_table(n):
    """Return an ``n x n`` multiplication table.

    Args:
        n: Size of the table to generate.

    Returns:
        A list of rows where each entry is the product of its row and column
        indices, starting at 1.
    """
    table = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append((i + 1) * (j + 1))
        table.append(row)
    return table


if __name__ == '__main__':
    num = int(input('Enter an integer:'))
    table = multiplication_table(num)
    for k in range(num):
        print(k + 1, table[k])
