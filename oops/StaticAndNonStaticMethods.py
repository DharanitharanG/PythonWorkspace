def func_outside():
    print("func outside")


class StaticNonStaticExample:
    var1 = 'var1_value'
    var2 = "var2_value"

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def non_static_method_1(self):
        print("I am inside non_static_method_1 : ", self.a)
        func_outside()

    @staticmethod
    def static_method_1():
        print("I am inside static_method_1 : ")
        func_outside()


s = StaticNonStaticExample(1, 2, 3)
s.non_static_method_1()
s.static_method_1()
StaticNonStaticExample.static_method_1()
func_outside()
