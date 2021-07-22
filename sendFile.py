import ftplib
import requests

FTP_HOST = "192.168.188.40"
FTP_USER = "admin"
FTP_PASS = "admin"

ftp = ftplib.FTP(FTP_HOST, FTP_USER, FTP_PASS)
ftp.encoding = "utf-8"

#filename = "a.mp4"

def send_msg(text):
    token = "1852837311:AAFQgaagHOZQzVzl2qSLTmRWa67SZVHWhcU"
    chat_id = "717810574"
    url_req = "https://api.telegram.org/bot" + token + "/SendMessage" + "?chat_id=" + chat_id + "&text=" + text
    results = requests.get(url_req)
    
    if results.json():
        print("Alert Sent!")

def sendFile(filename, location):
    
    loc = location
    
    with open(filename, "rb") as file:
        ftp.storbinary("STOR "+filename, file)

    #send_msg("an accident occur!")
    send_msg(location)
    #ftp.dir()
    ftp.quit()



