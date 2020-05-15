from flask import Flask, request
import africastalking
import os

'''
app = Flask(__name__)

@app.route('/')
def index():
	return 'hello, world'



if __name__ == "__main__":
    	app.run(debug=True)
#import africastalking
'''

app = Flask(__name__)
username= "sandbox"
api_key = "ffc056d72be88de34e0b7c765e792ab37af5a6f9684dbe720a5e9727e3db56be"
africastalking.initialize(username, api_key)
#sms= africastalking.sms

@app.route('/', methods = ['POST','GET'])


#Session ID - this is a unique identifier for your USSD session
#Service Code - This is the USSD code that is making the request
#Phone Number - This is the phone number currently accessing
#Text - This is the text input provided by the user

def ussd():
    global response
    session_id = request.values.get("sessionId",None)
    servicecode =  request.values.get("serviceCode",None)
    phone_number = request.values.get("phoneNumber",None)
    text = request.values.get("text","default")
    sms_phone_number.append(phone_number)

    #ussd logic

    if text == "":
        response = "CON Track your health status?\n"
        response += "1. Cough(1pt)\n"
        response += "2. Next\n"
        response += "3. My phone number\n"
        response += "4. Send a message"
    elif text == "1":
        response = "CON Add up your points:\n"
        response += "1. colds(1pt)\n"
        response += "2. Next\n"
    elif text == "2":
        response = "CON Track your health:\n"
        response += "1. diarrhea(1pt)\n"
        response += "2. Next\n"
    elif text == "3":
        #sub menu 1
        response = "END Your phone number is {}".format(phone_number)
    elif text == "4":
        try:
            #sending the sms
            sms_response = sms.send("Thank you for going through this tutorial", sms_phone_number)
            print(sms_response)
        except Exception as e:
            #show us what went wrong
            print("Houston, we have a problem: {e}")
    elif text == "1*1":
        response = "CON Add up your points:\n"
        response += "1. sorethroat(1pt)\n"
        response += "2. Next\n"
    elif text == "1*2":
        response = "CON Add up your points:\n"
        response += "1. bodyache(1pt)\n"
        response += "2. Next\n"
    elif text == "2*1":
        response = "CON Add up your points:\n"
        response += "1. headache(1pt)\n"
        response += "2. Next\n"
    elif text == "2*2":
        response = "CON Add up your points:\n"
        response += "1. hightemp(1pt)\n"
        response += "2. Next\n"
    elif text == "1*1*1":
        response = "CON Add up your points:\n"
        response += "1. fever(1pt)\n"
        response += "2. Next\n"
    elif text == "1*1*2":
        response = "CON Add up your points:\n"
        response += "1. breathstress(2pt)\n"
        response += "2. Next\n"
    elif text == "1*2*2":
        response = "CON Add up your points:\n"
        response += "1. tiredness(2pt)\n"
        response += "2. Next\n"
    elif text == "2*1*1":
        response = "CON Add up your points:\n"
        response += "1. travelled(3pt)\n"
        response += "2. Next\n"
    elif text == "2*1*2":
        response = "CON Add up your points:\n"
        response += "1. corolocation(3pt)\n"
        response += "2. Next\n"
    elif text == "2*2*2":
        response = "CON Add up your points:\n"
        response += "1. coropatient(3pt)\n"
        response += "2. Next\n"
    elif text == "1*1*1*1*1*1*1*1*1*1*1*1*1":
        #ussd menus are split using *
        account_number = "21pt"
        response = "END Please go for check or call {}".format(account_number)
    elif text == "1*2":
        account_balance = "100,000"
        response = "END Your account balance is USD {}".format(account_balance)
    else:
        response = "END Invalid input. Try again."

    return response


    if __name__ == "__main__":
    	app.run(host="0.0.0.0", port=os.environ.get("PORT"))

    