import random
import string

def get_userDetails():
    first_name = input('Enter your First Name: ')
    last_name = input('Enter your Last Name: ')
    email = input('Enter your Email Address: ')
    userDetails = [first_name,last_name,email]
    return userDetails 


def create_Password(userDetails):
    characters = string.ascii_letters
    length = 5
    randomPassword = ''.join(random.choice(characters) for i in range(length))
    password = userDetails[0][0:2] + userDetails[1][-2: ] + randomPassword
    return password

status = True
collectData = []
while status: 
    userDetails = get_userDetails()
    password = create_Password(userDetails)
    print ("Your password is " + password)

    password_okay = input('Are you okay with the password? "Yes/No": ')

    password_status = True
    while password_status:
        if password_okay.upper() == "YES":
            userDetails.append(password)
            collectData.append(userDetails)
            password_status = False
        else:
            new_password = input('Enter new password, password must be more than or equal to 7 characters: ')
            password_length = True
            while password_length:
                userDetails.append(new_password)
                collectData.append(userDetails)
                password_length = False
                password_status = False
            else:
                print('Your password is less than 7')
                new_password = input('Enter password more than or equal to 7 characters: ')
                password_length = False
                password_status = True
                  
    new_user = input('Would you like to enter a new user? Yes/No: ')
    if(new_user.upper() == "NO"):
        status = False
        print(collectData)
    else:
        status = True 

            




