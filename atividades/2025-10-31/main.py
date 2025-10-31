import numpy as np

if __name__ == "__main__":
    while True:
        try:
            n_input = input("Digite a ordem do vetor: ")
            n = int(n_input)
            if n < 0:
                raise Exception
            break
        except ValueError as e:
            print(f"{n_input} não é um inteiro.")

        except:
            print(f"{n} precisa ser maior que 0.")
