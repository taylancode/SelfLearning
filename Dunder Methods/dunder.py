
class DunderMethods:

    def __new__(cls):
        print(f"\nCreating class object with name: {cls.__name__}")
        print(f"Demonstrating that __new__ is called before __init__")
        cls_object = object.__new__(cls)
        return cls_object

    def __init__(self):
        print("Instantiating the class, following object creation in __new__")
        self.test1 = None
        self.test2 = None

    # def __str__(self):
    #     attrs = str(list(self.__dict__))
    #     return f"<Overriden repr method: Showing class attributes> {attrs}"


class Test(DunderMethods):

    def __init__(self):
        super().__init__()
    
    def __repr__(self) -> str:
        attrs = str(list(self.__dict__))
        return f"<Overriden repr method: Showing class attributes> {attrs}"

if __name__ == '__main__':

    d = DunderMethods()
    print(d.__str__())

    t = Test()
    print(t.__repr__())
    print(t.__str__())
