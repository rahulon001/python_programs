def numberOfSteps(num: int) -> int:
    steps = 0
    while num != 0:
        if num % 2 == 0:
            num /= 2
            steps += 1
        elif num % 2 != 0:
            num -= 1
            steps += 1
        else:
            return -1
    return steps

if __name__ == "__main__":
    print(numberOfSteps(23))