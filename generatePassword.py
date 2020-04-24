def generatePasswords(lengthOfPasswords, numberOfPasswords):
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@.'
    passwords = []
    # For loop to make number of passwords user wants
    for p in range(numberOfPasswords):
        password = ''
        # For loop to make one password
        for c in range(lengthOfPasswords):
            password += (random.choice(chars))
        # Adds to an array
        passwords.append(password)
    # The array is returned
    return passwords
