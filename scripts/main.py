from sys import exit
from package_A import exampleAOne, exampleATwo
from package_B import exampleBOne


def main():
    exampleAOne.hello_world()
    exampleATwo.hello_world()
    exampleBOne.hello_world()
    return 0


if __name__ == "__main__":
    exit(main())
