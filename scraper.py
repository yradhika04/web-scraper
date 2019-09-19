import requests
import re
from bs4 import BeautifulSoup
import socket
import sys

char="y"
var1="www."
var2="http://www."
var3="https://www."
flag=1

def functionAll(url):
    functionIP(url)
    res = functionTitle(url,var2)
    if(functionLogin(res)):
        functionLoginLink(res)
    if(functionRegister(res)):
        functionRegisterLink(res)
    functionContact(res)
    functionPassword(res)
    functionCaptcha(res)
    if(functionApp(res)):
        functionPlatform(res)
    functionUserDataIndustry(res)
    functionCopyright(res)
    functionPrivacy(res)
    functionCookie(res)
    functionAllLinks(res)

def functionHTTP(url):                 #CHECK HTTP CONNECTION
    str1=var2+url
    try:
        page=requests.get(str1)
        print("The status code of entered url is: ",page.status_code)
        if(page.status_code==200):
            print("Yes, HTTP connected")
            return True
        else: 
            print("Not HTTP connected")
            return False
        #functionHTTPS(url,count)
    except:
        print("Error: ", sys.exc_info()[0], "Occured")
        return False


def functionHTTPS(url):           #CHECK HTTPS CONNECTION
    str1=var3+url
    try:
        page=requests.get(str1)
        #print(page.status_code)
        if(page.status_code==200):
            print("Yes, HTTPS is enforced")
            return True
        elif(page.status_code==300): 
            print("HTTPS connected but not enforced")
            return True
        else:
            print("Not HTTPS connected")
            return False
    except:
        print("Error: ", sys.exc_info()[0], "Occured")
        return False        

def functionIP(url):                #FIND IP ADDRESS
    ip=socket.gethostbyname(url)
    print("The IP addr:",ip)
    #functionTitle(url,str1)

def functionTitle(url, schema):             #FIND TITLE OF WEBPAGE
    str1=schema+url
    page=requests.get(str1)
    soup=BeautifulSoup(page.content,'html.parser')
    title=str(soup.find_all('title'))
    print(title)
    return soup
    #functionLogin(page,url,soup)
    
def functionLogin(soup):         #FIND LOGIN PRESENCE
    logins=re.findall(r'Login|Sign in|Signin|Enter|Get in|Start',str(soup))
    if(logins):
        print("Login available")
        return True
    else: 
        print("Login unavailable")
        return False
    #functionRegister(page,url,soup)  

def functionLoginLink(soup):
    flag2=0
    for i in range(1,len(soup.find_all('a'))):
        link1=soup.find_all('a')[i]
        loginlink=re.findall(r'login|account',str(link1))
        if(loginlink):
            link2=link1['href']
            page2=requests.get(link2)
            if(page2.status_code==200):
                print("Login link is working and status code is: ",page2.status_code)
                soup2=BeautifulSoup(page2.content,'html.parser')
                data=re.findall(r'Username|User name|Password|key|Email|E-mail|Email address|Code|OTP|Mail|MFA|2FA|Multi-Factor Authentication|Name|First|Last|Firstname|Lastname|Gender|Title|Male|Female|Password|Passport|SSN|Social Security Number|Postal|Zip|Address|Phone|Cellular|Email|E-mail',
                str(soup2))
                print("The keywords found in the login link are: ", data)
                flag2=1
                break 
    if(flag2==0):
        print("Login link is not working")

def functionRegister(soup):       #FIND REGISTRATION PRESENCE
    register=re.findall(r'Registration|Register|New User|New Username|Signup|Sign Up|First time user|Join|Sign In',str(soup))
    if(register):
        print("Registeration available") 
        return True
    else: 
        print("Registeration unavailable")
        return False
    #functionContact(soup)

def functionRegisterLink(soup):
    flag3=0
    for i in range(1,len(soup.find_all('a'))):
        link1=soup.find_all('a')[i]
        reglink=re.findall(r'register|signup|new',str(link1))
        if(reglink):
            link2=link1['href']
            page2=requests.get(link2)
            if(page2.status_code==200):
                print("Registration link is working and status code is: ",page2.status_code)
                soup2=BeautifulSoup(page2.content,'html.parser')
                data=re.findall(r'Username|User name|Password|key|Email|E-mail|Email address|Code|OTP|Mail|MFA|2FA|Multi-Factor Authentication|Name|First|Last|Firstname|Lastname|Gender|Title|Male|Female|Password|Passport|SSN|Social Security Number|Postal|Zip|Address|Phone|Cellular|Email|E-mail',
                str(soup2))
                print("The keywords found in the registration link are: ", data)
                flag3=1
                break 
    if(flag3==0):
        print("Registration link is not working")


def functionContact(soup):        #FIND CONTACT INFORMATION
    contact=re.findall(r'Contact|Contact us|About|About us|Phone|Call|Address',str(soup))
    if(contact):
        print("Contact information available")
    else: 
        print("Contact information unavailable")

def functionPassword(soup):
    password=re.findall(r'Forgot Password|Forget Password|Recover Password|Update Password|Forget|Forgot|Recover|Update',str(soup))
    if(password):
        print("Forgot password option available")
    else: 
        print("Forgot password option unavailable")

def functionCaptcha(soup):
    captcha=re.findall(r'CAPTCHA',str(soup))
    if(captcha):
        print("CAPTCHA present")
    else: 
        print("CAPTCHA not present")

def functionApp(soup):
    app=re.findall(r'App store|Store|Download|App',str(soup))
    if(app):
        print("App download available")
        return True
    else: 
        print("App download not available")
        return False

def functionPlatform(soup):
    platform1=re.findall(r'iOS|Appstore|App store',str(soup))
    platform2=re.findall(r'Android|Playstore|Play store',str(soup))
    if(platform1):
        print("iOS app platform")
    if(platform2): 
        print("Android app platform")
    else:
        print("Unknown app platform")

def functionHeaders(link):
    page=requests.get(link)
    #print(page.headers)
    dict1=page.headers

    r1=0
    r1=re.findall(r'X-XSS-Protection',str(dict1))
    if(r1):
        a=dict1["X-XSS-Protection"]
        print("The X-XSS-Protection header response is ", a)
    else:
        print("X-XSS-Protection header not detected")

    r1=0
    r1=re.findall(r'X-Frame-Options',str(dict1))
    if(r1):
        a=dict1["X-Frame-Options"]
        print("The X-Frame-Options header response is ", a)
    else:
        print("X-Frame-Options header not detected")

    r1=0
    r1=re.findall(r'Server',str(dict1))
    if(r1):
        a=dict1["Server"]
        print("The Server header response is", a)
    else:
        print("Server header not detected")

    r1=0
    r1=re.findall(r'Strict-Transport-Security',str(dict1))
    if(r1):
        a=dict1["Strict-Transport-Security"]
        print("The Strict-Transport-Security header response is", a)
    else:
        print("Strict-Transport-Security header not detected")

def functionUserDataIndustry(soup):
    userdata=re.findall(r'Animal|Human|Cat|Dog',str(soup))
    print("User data industry: ",userdata)

def functionCopyright(soup):
    cr=re.findall(r'Copyright|©',str(soup))
    if(cr):
        print("Copyright issued")
    else:
        print("No copyright")

def functionPrivacy(soup):
    privacy=re.findall(r'Privacy|Privacy Policy|Disclaimer',str(soup))
    if(privacy):
        print("Privacy policy exists")
    else:
        print("Privacy policy doesn't exist")

def functionCookie(soup):
    cookie=re.findall(r'Cookie|Cookies|Consent',str(soup))
    if(cookie):
        print("Cookie consent asked")
    else:
        print("No cookie consent")

def functionAllLinks(soup):
    print("List of all links:")
    for i in range(1,len(soup.find_all('a'))):
        print(soup.find_all('a')[i])
        '''link2=link1['href']
        print(link2)
        page2=requests.get(link2)
        if(page2.status_code==200):
            print(link2)'''

#MAIN FUNCTION, START OF PRG
while char=="y":
    print("Enter url: ")
    url=input()
    if(functionHTTP(url)):
        flag=1
        functionAll(url)
        link1=var2+url
        functionHeaders(link1)

    if(flag==1):
        functionHTTPS(url)
    
    else: 
        functionHTTPS(url)
        functionAll(url)
        link2=var3+url
        functionHeaders(link2)

    print("Press y to continue")
    char=input()
    if(char!="y"):
        print("Exiting...")
