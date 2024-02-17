import datetime
def print_header():
    print("---------------------------------")
    print("\t Birthday App")
    print("---------------------------------")

def get_birthday_from_user():
    print("Please enter your birthday: ")
    year= int(input('Year [YYYY]: '))
    month = int(input("Month [MM]: "))
    day = int(input ("Day [DD]: "))

    birthady = datetime.datetime(year,month,day)
    return birthady


def compute_days_between_days(original_date,now):
    date1=now
    date2 = datetime.datetime(now.year,original_date.month,original_date.day)
    dt= date1-date2
    days=int(dt.total_seconds()/60/60/24)
    return days
    

def print_birthday_information(days):
    if days<0:
        print('Your birthday is in {} days!'.format(-days))
    elif days >0:
        print("you had your birthday already this year! {} days ago".format(days))
    else:
        print("Happy Birthday")
def main():
    print_header()
    bday=get_birthday_from_user()
   
    now = datetime.datetime.now()
    number_of_days=compute_days_between_days(bday,now)
   
    print_birthday_information(number_of_days)

main()