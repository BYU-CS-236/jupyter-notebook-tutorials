def my_function(my_list):
    print("In function scope")
    for my_variable in my_list:
        print("\tmy_variable =", my_variable)
def main_1():
    my_variable = 37
    my_list = range(4)
    my_function(my_list)
    print("Out of function scope my_variable =", my_variable)

def print_all(predicate):
    for values in predicate:
        print(values)
def main():
    P = {1: True, 2: True, 3: True, 4: True}
    Q = {1: False, 2: True, 3: False, 4: False}
    [print(key,value) for key,value in P]
    print_all(P)
    print(Q)



main()