# import smtplib


#
# my_email = "aooddy892@gmail.com"
# password = "vdvsfdllevjzjwme"                 # '8,8j<w56kkAGj:AV1E8QE'     #vdvs fdll evjz jwme
# #
# my_email = "aooddytest@yahoo.com"
# password = "dxzfnsfgdqibagcg"
# # #
# #
# with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email,password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="aooddy892@gmail.com",
#         msg="Subject:Hello\n\nThis is body do my email.")

import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()

# print(day_of_week)

# date_of_birth = dt.datetime(year=1991, month=6, day=18,hour=6,minute=55)

# print(date_of_birth)


print(type(year))

