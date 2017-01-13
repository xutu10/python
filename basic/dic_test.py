class dic:
    def __init__(self):
        self.data = {'1':'arts',
                     '2': 'business',
                     '3':'sports',
                     '4': 'politic' }

    def show(self):
        print self.data.items()
        for key, value in self.data.items():
            # input in one line with ',' after value
            print key, '-', value,


if __name__ == "__main__":
    first_dic = dic()
    first_dic.show()
