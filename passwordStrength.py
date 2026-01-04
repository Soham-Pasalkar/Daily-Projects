uppercase = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'}
lowercase = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}
digits = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
special_characters = {'!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+'}

score = set()

def strength_checker(password):
    for char in password:
        if char in uppercase:
            score.add('U')
            break
        if char in lowercase:
            score.add('L')
            break
        if char in digits:
            score.add('D')
            break
        if char in special_characters:
            score.add('S')
            break
    if len(password) >= 12:
        score.add('Length')
    return score

password = input("Enter your password: ")
s = strength_checker(password)
result = len(s)

quality = ["Very Weak", "Weak", "Moderate", "Strong", "Very Strong"]
print(f"Password Strength: {quality[result]}")
