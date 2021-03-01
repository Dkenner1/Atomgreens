
class Process:
    def __init__(self, _return_dict):
        self.steps = []
        self.return_dict = _return_dict

    def add(self, args):
        self.steps.append(args)

    def perform_actions(self, input):
        for item in self.steps:
            item[3] = item[0](input, item[1], item[2])


def test2(*args):
    x=(args)
    print(x)

if __name__ == "__main__":
    testdict = {'Key1': None, 'Key2': 2}
    test2(1,2,3,4,5)

