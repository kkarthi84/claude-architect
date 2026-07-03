def is_prime(n):
    """
    Check if a given number is a prime number.
    
    Args:
        n (int): The number to check
        
    Returns:
        bool: True if the number is prime, False otherwise
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n < 2:
        return False
    
    if n == 2:
        return True
    
    if n % 2 == 0:
        return False
    
    # Check odd divisors up to the square root of n
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    
    return True


def main():
    """Main function to demonstrate prime number checking."""
    test_numbers = [2, 3, 4, 5, 10, 17, 20, 29, 100, 97]
    
    print("Prime Number Checker")
    print("-" * 40)
    
    for num in test_numbers:
        result = is_prime(num)
        status = "PRIME" if result else "NOT PRIME"
        print(f"{num:3d} is {status}")


if __name__ == "__main__":
    main()
