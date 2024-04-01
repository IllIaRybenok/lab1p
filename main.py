import sys

print("Hello World")

name = input("Please, give your name")
print("Hello " + name)

print("Size of basic Python types in bytes:")
print("=======================================")
print(f"Int: {sys.getsizeof(int())}")
print(f"Float: {sys.getsizeof(float())}")
print(f"Bool: {sys.getsizeof(bool())}")
print(f"String: {sys.getsizeof('')}")
print(f"Tuple: {sys.getsizeof(()):>7}")
print(f"List: {sys.getsizeof([]):>7}")
print(f"Dict: {sys.getsizeof({}):>7}")
print(f"Set: {sys.getsizeof(set()):>7}")