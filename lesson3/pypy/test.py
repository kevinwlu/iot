def add(a, b):
    """
    Add two arguments.

    Args:
        a: (int): write your description
        b: (int): write your description
    """
  return a + b

def main():
    """
    Main function.

    Args:
    """
    i = 0
    a = 0.0
    while i < 1000000:
        a += 1.0
        add(a, a)
        i += 1
    print(a)

main()
