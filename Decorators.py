""" Decorators try """


def fun1(parameter):
    def child_fun():
        print("Before")

        parameter()

        print("After")

    return child_fun


@fun1
def fun2():
    print("Ashish")


fun2()
