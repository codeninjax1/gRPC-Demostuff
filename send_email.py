import smtplib

def email(reciever,message):

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login("demogrpc@gmail.com", "1234haloDell*")
    message = "Subject: Demo \n\n {}".format(message)
    print("in email")
    print("reciever",reciever)
    server.sendmail(
    "from@address.com", 
    reciever,
    message)
    server.quit()

if __name__ == "__main__":
    email("test")
