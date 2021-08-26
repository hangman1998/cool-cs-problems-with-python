from __future__ import annotations


class State:

    def __init__(self) -> None:

        self.canoe_location = 'left'
        self.left_miss = 3
        self.left_can = 3
        self.right_miss = 0
        self.right_can = 0

    def __str__(self) -> str:
        if self.canoe_location == 'left':
            return f"M: {self.left_miss}  C: {self.left_can} <-->      M: {self.right_miss}  C: {self.right_can}"
        else:
            return f"M: {self.left_miss}  C: {self.left_can}      <--> M: {self.right_miss}  C: {self.right_can}"

    def action(self, num_can, num_miss):
        if not (num_can >= 0 and num_miss >= 0 or 1 <= (num_miss + num_can) <= 2):
            return None
        next_state = State()
        if self.canoe_location == 'left':
            next_state.canoe_location = 'right'
            next_state.left_miss = self.left_miss - num_miss
            next_state.left_can = self.left_can - num_can
            next_state.right_miss = self.right_miss + num_miss
            next_state.right_can = self.right_can + num_can
        else:
            next_state.canoe_location = 'left'
            next_state.left_miss = self.left_miss + num_miss
            next_state.left_can = self.left_can + num_can
            next_state.right_miss = self.right_miss - num_miss
            next_state.right_can = self.right_can - num_can

        if not (next_state.left_miss >= 0 and next_state.left_can >= 0 and next_state.right_miss >= 0 and next_state.right_can >= 0):
            return None
        if 0 < next_state.left_miss < next_state.left_can or 0 < next_state.right_miss < next_state.right_can:
            return None
        return next_state

    def __eq__(self, o: object) -> bool:
        return self.canoe_location == o.canoe_location and self.left_can == o.left_can and self.left_miss == o.left_miss\
            and self.right_miss == o.right_miss and self.right_can == o.right_can

    def check_goal(self):
        return self.left_can == 0 and self.left_miss == 0
        # return self.right_can == 0 and self.right_miss == 0


class Node:

    def __init__(self, state: State, parent: Node):
        self.state = state
        self.parent = parent
        self.child = []
        self.seen = False

    def __eq__(self, o: object) -> bool:
        return self.state == o.state

    def num_of_node():
        print(Node.c)

    def creat_child(self):
        if self.child == []:
            l = [self.state.action(0, 1), self.state.action(1, 1), self.state.action(
                1, 0), self.state.action(2, 0), self.state.action(0, 2)]
            for state in l:
                if state is not None:
                    self.child.append(Node(state, self))


if __name__ == '__main__':
    root = State()
    node_root = Node(root, None)
    frontier = [node_root]
    explore = []
    goal = []
    while len(goal) == 0:
        frontier[0].creat_child()
        for child in frontier[0].child:
            if child.state.check_goal():
                goal.append(child)

            if child not in frontier and child not in explore:
                frontier.append(child)

        explore.append(frontier[0])
        frontier.remove(frontier[0])

    print(f"number of solutions :{len(goal)}")
    for g in goal:
        print("-----------------------------")
        itr = g
        while itr is not None:
            print(itr.state)
            itr = itr.parent
