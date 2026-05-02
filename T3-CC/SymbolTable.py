class SymbolTable:
    def __init__(self):
        self.scopes = [{}]
        self.add_type('inteiro')
        self.add_type('real')
        self.add_type('literal')
        self.add_type('logico')
        # Pointers aren't explicit types in the table, they are derived (e.g. ^inteiro)

    def enter_scope(self):
        self.scopes.append({})

    def exit_scope(self):
        if len(self.scopes) > 1:
            self.scopes.pop()

    def add_type(self, name):
        self.scopes[0][name] = {'category': 'tipo', 'type': name}

    def add(self, name, category, var_type=None, params=None):
        if name in self.scopes[-1]:
            return False
        self.scopes[-1][name] = {'category': category, 'type': var_type, 'params': params}
        return True

    def exists(self, name):
        for scope in reversed(self.scopes):
            if name in scope:
                return True
        return False

    def get(self, name):
        for scope in reversed(self.scopes):
            if name in scope:
                return scope[name]
        return None
