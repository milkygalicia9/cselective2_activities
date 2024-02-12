def divide_numbers(num1, num2):
    try:
        result = num1 / num2
        print(f"The result of {num1} / {num2} is: {result}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
    except TypeError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("This block is always executed, regardless of whether an exception occurred or not.")

try:
    divide_numbers(10, 2)
    divide_numbers(5, 0) 
    divide_numbers("abc", 2)  
except Exception as e:
    print(f"Caught an exception: {e}")
