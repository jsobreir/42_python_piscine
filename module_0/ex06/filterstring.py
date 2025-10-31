import sys


def filterstring(N):
    return lambda string: len(string) > N


try:
    assert len(sys.argv) == 3, "Assertion error: The arguments are bad"
    S = sys.argv[1].split()
    N = int(sys.argv[2])
    filtered_string = [x for x in S if filterstring(N)(x)]
    print(filtered_string)
except AssertionError as error:
    print(error)
