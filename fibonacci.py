def fibonacci(n):
    """
    Recursive function to return the nth Fibonacci number.
    """
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def main():
    """
    Main function to welcome the user, get the number of terms, and generate the Fibonacci sequence.
    """
    # Welcome the user
    print("Welcome to the Fibonacci Sequence Generator!")

    # Ask the user how many Fibonacci terms they want to generate
    while True:
        try:
            n = int(input("How many Fibonacci terms would you like to generate? Please enter a positive integer: "))
            if n <= 0:
                print("Please enter a positive integer greater than 0.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid positive integer.")

    # Generate and display the Fibonacci sequence up to the n-th term
    print(f"\nFibonacci sequence up to the {n}-th term:")
    for i in range(n):
        print(f"Term {i}: {fibonacci(i)}")

if __name__ == "__main__":
    main()