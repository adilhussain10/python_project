#Random password generator

import random
import string
print("welcome to random password generator")
     
def main():
    length=int(input("Enter the length-"))
    lower=string.ascii_uppercase
    upper=string.ascii_lowercase
    digit=string.digits
    symbol=string.punctuation
    combine=lower+upper+digit+symbol
    x=random.sample(combine,length)
    password="".join(x)
    print(password)
    main()

main()