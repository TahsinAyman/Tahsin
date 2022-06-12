import smtplib
import json

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)

with open("personal_data.json") as file:
    person_data = json.load(file)

server.login(person_data['user'], person_data['password'])
server.sendmail(person_data['user'], "mail4rashed@gmail.com", "hello")
server.close()

print("Finished")
