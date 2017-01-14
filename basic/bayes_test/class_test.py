class son:
    def __init__(self):
        self.data = [1,2,3,4]

class father:
    def __init__(self):
        self.son = son()

if __name__ == "__main__":

    first = father()
    print first.son.data
