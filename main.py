import smtplib
import datetime as dt
import random

MY_EMAIL = "o2real@gmail.com"
MY_PASSWORD = "qwerasdf1234"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Monday Motivation\n\n{quote}"
        )



# import smtplib
#
# my_email = "jiohqwer@gmail.com"
# password = "qwer1234asdf"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email , password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="o2rela@naver.com",
#         msg="Subject:Hello\n\nThis is the body of my email."
#     )

#
# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# print(day_of_week)
#
# date_of_birth = dt.datetime(year=1997, month=1, day=14)
# print(date_of_birth)
#
