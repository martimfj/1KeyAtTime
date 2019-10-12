class SymbolTable():
    def __init__(self, ancestor):
        self.table = {}
        self.ancestor = ancestor

    def getter(self, variable_name):
        if variable_name in self.table.keys():
            return self.table[variable_name]
        elif self.ancestor != None:
            return self.ancestor.getter(variable_name)
        else:
            raise ValueError(f"error: Variable {variable_name} does not exist")

    def setter(self, variable_name, variable_value):
        self.table[variable_name] = variable_value
