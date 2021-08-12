class State:

    
    canoe_location = 'left'
    left_miss = 3
    left_can = 3
    right_miss = 0
    right_can = 0

    def action(self, num_can, num_miss):
        assert num_can >= 0 and  num_miss >= 0
        assert  1 <= (num_miss + num_can) <= 2
        next_state = State()
        if self.canoe_location == 'left':
            next_state.canoe_location = 'right'
            self.left_miss -= num_miss
            self.left_can -= num_can
            self.right_miss += num_miss
            self.right_can += num_can
        else:
            next_state.canoe_location = 'left'
            self.left_miss += num_miss
            self.left_can += num_can
            self.right_miss -= num_miss
            self.right_can -= num_can
        assert self.left_miss >= 0 and self.left_can >= 0 and self.right_miss >= 0 and self.right_can >= 0
        return next_state
    
    def check_goal(self):
        return self.left_can == 0 and self.left_miss == 0
    
    def check_fail(self):
        return self.left_miss < self.left_can or self.right_miss < self.right_can

  
if __name__ == '__main__':
    root = State()
