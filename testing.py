import math

'''This function determines the volume of a sphere'''


def volume_sphere(radius):
    pie = math.pi
    vol = 4/3*3.14*pie*radius**3
    return vol
    # print(f"The volume is {vol:.2f}")

# print(volume_sphere(5))


volume = volume_sphere(4)

'''This function determines the volume of a cylinder'''


def volume_cylinder(r, h):
    pie = math.pi
    vol = pie*r**2*h
    return vol


volume = volume_cylinder(5, 12)
print(volume)
print(help)


def main():
    print(volume_cylinder(1, 5))
    print(volume_sphere(5))
    print(__name__)


if __name__ == "__main__":
    main()

# The user's number should be increased by 1 and printed.
def increase(x):
    x = input("Enter a number: ")
    sum = x+1
    return sum

increase(sum)
print("Your number has been increased to", sum)