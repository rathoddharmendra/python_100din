def is_prime(num):
    """
    checks prime number
    """
    for i in range(2, num):
        if num % i == 0:
            return False
        
    return True