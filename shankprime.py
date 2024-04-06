def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def find_reciprocal_pattern(prime):
    """Find the repeating pattern in the reciprocal of a prime."""
    remainder = 1
    seen = {}
    pattern = []
    
    while remainder != 0 and remainder not in seen:
        seen[remainder] = len(pattern)
        remainder *= 10
        quotient, remainder = divmod(remainder, prime)
        pattern.append(quotient)
    
    if remainder == 0:
        return None  # No repeating pattern
    
    start_index = seen[remainder]
    repeating_pattern = pattern[start_index:]
    
    return repeating_pattern

if __name__ == "__main__":
    prime = int(input("Enter a prime number: "))
    
    if not is_prime(prime):
        print("Input is not a prime number.")
    else:
        pattern = find_reciprocal_pattern(prime)
        
        if pattern:
            print(f"Repeating pattern in 1/{prime}:")
            print("".join(map(str, pattern)))
            print(f"The pattern has a length of {len(pattern)}")
        else:
            print(f"1/{prime} is a terminating decimal.")
