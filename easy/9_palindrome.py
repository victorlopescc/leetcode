X = 121


def is_palindrome(x):
    def reverse_number(n):
        length = len(str(n))
        result = 0
        for i in range(length):
            digit = n % 10
            result = int(result) * 10 + int(digit)
            n /= 10

        return result

    if x == reverse_number(x):
        return True

    return False


print(is_palindrome(X))
