def is_armstrong(num):
    digits=str(num)
    len_dig=len(digits)
    sum_powers=sum(int(digit) ** len_dig for digit in digits)
    return sum_powers == num

print("Armstrong numbers till 1000 are:")
for numbers in range(1,1000):
    if is_armstrong(numbers):
        print(numbers)