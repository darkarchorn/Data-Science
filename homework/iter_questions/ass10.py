def uppercase(cls):
    class Wrapper(cls):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.s = self.s.upper()
    return Wrapper

@uppercase
class ReverseString:
    def __init__(self, s):
        self.s = s
        self.current = len(s) - 1 
        # print(f"Self.current: {self.current}")

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current < 0:
            # print("STOP")
            raise StopIteration
        else:
            self.current -= 1
            # print("DEDUCTED")
        # print(f"Self.current: {self.current}")
        return self.s[self.current + 1]
    
rs = ReverseString("abc")
for i in rs:
    print(i)