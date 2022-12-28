name=input('Enter your name:')
email=input('Enter your email:')
mobile=input('Enter your mobile number:')
city= input('Enter your city: ')
# nested if-else
if len(name)>1:
    if '@' in email and len(email) > 11:
        if len(mobile)== 10 and mobile.isnumeric():
            if city in ['lucknow' , 'delhi' , 'Noida']:
                print('Your data is saved, Thankyou')
            else:
                ('We are not available in your city')
        else:
            print('Invalid mobile number ')
    else:
        print('Invalid Email address')
else:
    print('ye kaisa naam hai?😵‍💫😵‍💫')