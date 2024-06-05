class A:
    def method_a(self):
        print("Method of class A")

class B:
    def method_b(self):
        print("MEthos of clas B")
class C(A,B):
    def method_c(self):
        print("Method of class C")

cobject=C()
cobject.method_a()
cobject.method_b()
cobject.method_c()
