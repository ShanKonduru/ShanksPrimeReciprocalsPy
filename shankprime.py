import csv

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
    with open('./prime_reciprocals.csv', 'w', newline='') as csvfile:
        fieldnames = ['Prime#', 'Prime Reciprocal', 'Pattern Length']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        
        for num in range(1, 100001):
            if is_prime(num):
                reciprocal = 1 / num
                pattern = find_reciprocal_pattern(num)
                
                if pattern:
                    pattern_length = len(pattern)
                else:
                    pattern_length = 0
                
                writer.writerow({
                    'Prime#': num,
                    'Prime Reciprocal': reciprocal,
                    'Pattern Length': pattern_length
                })
