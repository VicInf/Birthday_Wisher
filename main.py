import pandas
import datetime as dt
import smtplib
import random
##################### Hard Starting Project ######################

# Check if today matches a birthday in the birthdays.csv

df = pandas.read_csv("birthdays.csv")
birthdays_dict = df.to_dict(orient="records")
now = dt.datetime.now()
month = now.month
day = now.today().day

# See if today's month/day matches one of the keys in birthday_dict
for data in birthdays_dict:
    if data["day"] == day and data["month"] == month:
        with open(f"letter_templates/letter_{random.randint(1,3)}.txt", "r") as letter:
            file_contents = letter.read()
            birthday_letter = file_contents.replace("[NAME]", f"{data["name"]}")

# Sends the Email
        my_email = "infernorealempire@gmail.com"
        password = "igmdhovnrkrwdqbk"

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=email["email"],
                                msg="Subject: Happy Birthday \n\n"
                                    f"{birthday_letter}")



