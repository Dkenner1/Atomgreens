from db import query
from SQL import MOST_RECENT, MEASURMENTS

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
    for item in query(MEASURMENTS):
        print(item)

