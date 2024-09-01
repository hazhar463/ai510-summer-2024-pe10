class ClassModule:
    def __init__(self, global_init_param):
        self.global_init_param = global_init_param

    def add(self, value):
        return self.global_init_param + value

    # New multiply function
    def multiply(self, value):
        return self.global_init_param * value