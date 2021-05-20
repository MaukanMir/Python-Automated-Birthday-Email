
import pandas
import smtplib
import datetime as dt
import random


my_email = "maukan.python@gmail.com"
my_password = "Apple1212"


now = dt.datetime.now()
day = now.weekday()
month = now.month
year = now.year


data = pandas.read_csv("birthdays.csv")


def random_letter():
    today = (month, day)
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    birthdays_dict = {(data_row['month'], data_row['day']): data_row for (
        index, data_row) in data.iterrows()}
    if today in birthdays_dict:
        birthday_name = birthdays_dict[today]
        with open(file_path) as file:
            contents = file.read()
            updated_file= contents.replace("[NAME]", birthday_name['name'])
        return f"Subject: Happy birthday!\n\n{updated_file}"


with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(my_email, my_password)
    connection.sendmail(from_addr=my_email,
                        to_addrs=my_email, msg=random_letter())



