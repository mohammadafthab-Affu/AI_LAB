
# laptop trubleshooting

def laptop(turn_on,internet_work,is_slow):
    if turn_on=="no":
         return"check the charger and power cable."
    elif internet_work=="no":
        return"ckeck the wifi & restartthe router."
    elif is_slow=="yes":
        return"close unsend program and restart the laptop."
    else:
        return"The system does not find a common problem."

turn_on=input("does laptop turn on?yes/no: ").lower()
internet_work=input("does the internet work? yes/no:").lower()
is_slow= input(" is the laptop slow?yes/no: ").lower()
advice= laptop(turn_on,internet_work,is_slow)
print("\n expert system advice:")
print(advice)
