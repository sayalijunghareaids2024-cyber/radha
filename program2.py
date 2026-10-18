
text = input("Enter a string: ")

reverse_text = text[::-1]

if text == reverse_text:
    print("The string is a palindrome")
else:
text = input("Enter a string: ")

if text.lower().replace(" ", "") == text.lower().replace(" ", "")[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")

    print("The string is not a palindrome")
