class MatrizInvalidaError(Exception):
    def __init__(self, message="Matriz inválida para esse tipo de operação"):
        self.message = message
        super().__init__(self.message)
