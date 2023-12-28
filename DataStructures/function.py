a2 = 10     # Globally declaring a2

def foo():
    print(a2)
    a2 += 1
    print(a2)

a2 = 12
foo()
print(a2)