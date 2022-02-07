"""
1) Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them
Solution:  Python: Print first and last name in reverse order with a space between them - w3resource

2)  Write a Python program to display the current date and time.
Sample Output :
Current date and time :
2014-07-05 14:34:14

Solution:  Python: Display the current date and time - w3resource

3)  Write a Python program to accept a filename from the user and print the extension of that. Go to the editor
Sample filename : abc.java
Output : java
Solution:  Python: Input a filename and print the extension of that - w3resource
"""
import datetime


def get_datetime():
    i = 0
    while True:
        if i % 56 == 0:
            print(datetime.datetime.now())
        i += 1

def steal_file_from_person():
    user_input = input("File name please(I will not do anything bad with it): ")
    print(user_input)

def main():
#    get_datetime()
    steal_file_from_person()






if __name__ == "__main__":
    main()