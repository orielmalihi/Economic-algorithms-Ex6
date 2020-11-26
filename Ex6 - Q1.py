from typing import List

import networkx as nx


class Agent:
    def __init__(self, name, values: List[int]):
        self.name = name
        self.values = values

    def __str__(self):
        return str(self.name) + " , " + str(self.values)

    def __repr__(self):
        return str(self.name) + " , " + str(self.values)

    def value(self, result: int)->float:
        if result >= len(self.values):
            return
        else:
            return self.values[result]


def vgc(agents: List[Agent], num_options: int):
    """"
    >>> ami = Agent("Ami", [8,4,3])
    >>> tami = Agent("Tami", [5,8,1])
    >>> rami = Agent("Rami", [3,5,3])
    >>> agents_test = [ami, tami, rami]
    >>> vgc(agents_test, 3)
    The chosen option is 2
    Ami pays 0
    Tami pays 2
    Rami pays 1
    >>> ami = Agent("Ami", [8,4,3])
    >>> tami = Agent("Tami", [5,3,1])
    >>> rami = Agent("Rami", [3,5,3])
    >>> agents_test = [ami, tami, rami]
    >>> vgc(agents_test, 3)
    The chosen option is 1
    Ami pays 0
    Tami pays 0
    Rami pays 0
    >>> ami = Agent("Ami", [7,8,4])
    >>> tami = Agent("Tami", [1,5,8])
    >>> rami = Agent("Rami", [7,3,5])
    >>> agents_test = [ami, tami, rami]
    >>> vgc(agents_test, 3)
    The chosen option is 3
    Ami pays 0
    Tami pays 5
    Rami pays 1
    """
    original_sums = sum_without(agents, num_options, None)
    chosen_result = get_max_index(original_sums)
    print("The chosen option is " + str(chosen_result + 1))

    for agent in agents:
        partial_sums = sum_without(agents, num_options, agent)
        chosen_virtual_result = get_max_index(partial_sums)
        payment = partial_sums[chosen_virtual_result] - (original_sums[chosen_result] - agent.value(chosen_result))
        print(agent.name + " pays " + str(payment))

def sum_without(agents: List[Agent], num_options: int, without_agent: Agent)->List[int]:
    sums = []
    for i in range(num_options):
        sum = 0
        for agent in agents:
            if agent == without_agent:
                continue
            sum += agent.value(i)
        sums.append(sum)
    return sums


def get_max_index(arr: List[int]):
    max = float('-inf')
    index = -1
    for i, value in enumerate(arr):
        if value > max:
            max = value
            index = i
    return index



if __name__ == "__main__":
    import doctest
    doctest.testmod()
