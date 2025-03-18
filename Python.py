l_alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
u_alphabet=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
def encryption(message,num):
    cipher=""
    for i in message:
        if i in l_alphabet:
            if i not in l_alphabet:
                cipher += i
            else:
                position = l_alphabet.index(i)
                position = (position + num) % 26
                cipher += l_alphabet[position]
        else:
            if i not in u_alphabet:
                cipher += i
            else:
                position = u_alphabet.index(i)
                position = (position + num) % 26
                cipher += u_alphabet[position]
    print(f"The encrypted text is {cipher} ")
def decryption(message,num):
    cipher=""
    for i in message:
        if i in l_alphabet:
            if i not in l_alphabet:
                cipher += i
            else:
                position = l_alphabet.index(i)
                position = (position - num) % 26
                cipher += l_alphabet[position]
        else:
            if i not in l_alphabet:
                cipher += i
            else:
                position = l_alphabet.index(i)
                position = (position - num) % 26
                cipher += l_alphabet[position]
    print(f"The decrypted text is {cipher} ")
game=True
while game:
    key = input("Type 'encrypt' for encryption and 'decrypt' for decryption").lower()
    m = input("Type your message ")
    n = int(input("Type the shift number"))
    if key == 'encrypt':
        encryption(message=m,num=n)
    elif key == 'decrypt':
        decryption(message=m,num=n)
    prompt=input("Type 'yes' if you want to do again.Otherwise type 'no'. ")
    if prompt=='yes':
        game=True
    else:
        game=False
