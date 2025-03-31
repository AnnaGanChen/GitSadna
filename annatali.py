def calculate1(operation, a, b):
    pass  # To be implemented by the team

if __name__ == "__main__":
    
    op = input("Enter operation (+, -, *, /): ")
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    result = calculate1(op, a, b)
    print(f"Result: {result}")

if op is '+':
        result=a+b
        print(result)
        if op is '-':
          result=a-b
        print(result)