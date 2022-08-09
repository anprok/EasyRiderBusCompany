prime_numbers = [num for num in range(2,1000) if True not in [True for divisor in range(2,(int(num/2)+1)) if num % divisor == 0 and num != 2]]
