def is_palindrome_recursive(A):
    if len(A) <= 1:
        return 1
    else:
        if A[0] == A[-1]:
            return is_palindrome_recursive(A[1:-1])
        else:
            return 0
if __name__ == "__main__":
    try:
        input_string = input("Enter a string to check if it's a palindrome: ")
        result = is_palindrome_recursive(input_string)
        if result:
            print("1")
        else:
            print("0")
    except ValueError:
        print("Invalid input. Please enter a valid string.")
