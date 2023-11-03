import smtplib
import datetime as dt
import random 

#
# my_email = "aooddy892@gmail.com"
# password = "vdvsfdllevjzjwme"                 # passwords : '8,8j<w56kkAGj:AV1E8QE'     #app passwords : # vdvs fdll evjz jwme  #redx lgha zyzw rctm

# # #
# my_email = "aooddytest@yahoo.com"
# password = "dxzfnsfgdqibagcg"
# # # # #
# # #
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email,password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="aooddytest@yahoo.com",
#         msg="Subject:Hello\n\nThis is body do my email.")

# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
#
# print(day_of_week)
#
# # date_of_birth = dt.datetime(year=1991, month=6, day=18,hour=6,minute=55)
#
# # print(date_of_birth)

# now = dt.datetime.now()
# weekday = now.weekday()

#yahoo to gmail
# if weekday == 3:
#     with open("quotes.txt") as quote_file:
#         all_quotes = quote_file.readlines()
#         quote = random.choice(all_quotes)
#     print(quote)
#     with smtplib.SMTP("smtp.mail.yahoo.com") as connection:             # yahoo  "smtp.mail.yahoo.com"  gmail use  smtp.gmail.com
#         connection.starttls()
#         connection.login(user=my_email,password=password)
#         connection.sendmail(
#             from_addr=my_email,
#             to_addrs="constant.eng.cmu@gmail.com",
#             msg=f"Subject:Tuesday \n\n{quote}")

# gmail to yahoo

# if weekday == 4:
#     with open("quotes.txt") as quote_file:
#         all_quotes = quote_file.readlines()
#         quote = random.choice(all_quotes)
#     print(quote)
#     with smtplib.SMTP("smtp.gmail.com") as connection:             # yahoo  "smtp.mail.yahoo.com"  gmail use  smtp.gmail.com
#         connection.starttls()
#         connection.login(user=my_email,password=password)
#         connection.sendmail(
#             from_addr=my_email,
#             to_addrs="constant.eng.cmu@gmail.com",
#             msg=f"Subject:Tuesday \n\n{quote}")
# #
#
# import datetime as dt
# import random
#
# my_email = "aooddy892@gmail.com"
# password = "vdvsfdllevjzjwme"
#
#
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
#
# # print(day_of_week)
#
# date_of_birth = dt.datetime(year=1991, month=6, day=18,hour=6,minute=55)
# # print(date_of_birth)
#
# if day_of_week == 4:
#     with open("quotes.txt") as quote_file:
#         all_qoute = quote_file.readlines()
#         qoute = random.choice(all_qoute)
#     print(qoute)
#
#     with smtplib.SMTP("smtp.gmail.com") as connetion:
#         connetion.starttls()
#         connetion.login(my_email,password)
#         connetion.sendmail(from_addr=my_email,
#                            to_addrs="aooddytest@yahoo.com",
#                            msg=f"Subject:Monday Motivtion\n\n{qoute}")
#
import pandas as pd

df = pd.read_csv('birthdays.csv')
df.head()






