def main():
    num = int(input())
    base = int(input())
    print(decimal(num, base))

def decimal(num, base):
    result = 0
    power = 0
    while num > 0:
        x = num % 10
        result += x * check_pow(base, power)
        power += 1
        num //= 10
    return result

def check_pow(base, x):
    if x == 0:
        return 1
    return base * check_pow(base, x - 1)

if __name__ == "__main__":
    main()
