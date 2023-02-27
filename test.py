def divisible(num1, num2):
	return num1 % num2 == 0

def user_even():
    shut_down = False
    while (shut_down == False):
        try:
            user_input = int(input("Enter a number: "))
            if (divisible(user_input, 2)):
                print("It's even")
            else:
                print("It's odd")
            shut_down = True
        except:
            print("Invalid input")
            
user_even()
