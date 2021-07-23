hour = input('What time is it? ')

if hour.isnumeric():
    hour = int(hour)

    if hour <= 11:
        print('Good Morning')
    elif hour > 11 and hour <=17:  # or  11 < hour <= 17
        print('Good Afternoon')
    else:
        print('Good Night')