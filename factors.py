import sys

def factorize(number):
    factors = []
    divisor = 2
    while divisor <= number:
        if number % divisor == 0:
            factors.append(divisor)
            number //= divisor
        else:
            divisor += 1
    return factors

def main():
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        sys.exit(1)

    input_file = sys.argv[1]

    try:
        with open(input_file, "r") as file:
            for line in file:
                number = int(line.strip())
                factors = factorize(number)
                p, q = factors[0], factors[1]
                print(f"{number}={p}*{q}")
    except FileNotFoundError:
        print(f"File '{input_file}' not found.")
        sys.exit(1)
    except ValueError:
        print("Invalid number in the input file.")
        sys.exit(1)

if __name__ == "__main__":
    main()
