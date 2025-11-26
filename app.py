def addition(a, b):
    """Fonction qui additionne deux nombres"""
    return a + b

def soustraction(a, b):
    """Fonction qui soustrait deux nombres"""
    return a - b

def multiplication(a, b):
    """Fonction qui multiplie deux nombres"""
    return a * b

def main():
    print("Application Python TP2")
    print(f"2 + 2 = {addition(2, 2)}")
    print(f"5 - 3 = {soustraction(5, 3)}")
    print(f"4 * 3 = {multiplication(4, 3)}")

if __name__ == "__main__":
    main()