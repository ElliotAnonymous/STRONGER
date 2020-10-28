import string
import colorama
from colorama import (Fore, Back, Style)#this module help you for adding colours
import time
import hashlib #this module is a python inbuilt model this help you for creating hash generater program's
from random import *
  
#hello guys my name is prem 
#Guys i have only android and i am use Dcoder  for coding 
print(Fore.RED+'''
  
  █▀▀ ▀▀█▀▀ █▀▀█ █▀▀█ █▀▀▄ █▀▀▀ █▀▀ █▀▀█
  ▀▀█ ░░█░░ █▄▄▀ █░░█ █░░█ █░▀█ █▀▀ █▄▄▀
  ▀▀▀ ░░▀░░ ▀░▀▀ ▀▀▀▀ ▀░░▀ ▀▀▀▀ ▀▀▀ ▀░▀▀   ''')
 
print(Style.RESET_ALL)
print(Fore.YELLOW+"   ᴄʀᴇᴀᴛᴇᴅ ʙʏ 👑 ᴍʀ.ᴀɴᴏɴʏᴍᴏᴜs 👑 v1.0")
print(Style.RESET_ALL)

while(True):
  
 
  Choice =int(input(Fore.GREEN+'''
 
  [+] 1.𝙿𝚊𝚜𝚜𝚠𝚘𝚛𝚍_𝙶𝚎𝚗𝚎𝚛𝚊𝚝𝚘𝚛
  [+] 2.𝙷𝚊𝚜𝚑_𝙶𝚎𝚗𝚎𝚛𝚊𝚝𝚘𝚛
  [+] 3.𝙴𝚡𝚒𝚝\n  >>> ''' ))
  
  
 
  if Choice == 1 :
     
    
      choice1 = "1"
      Exit = "2"
      print("\n  𝑃𝑎𝑠𝑠𝑤𝑜𝑟𝑑 𝐺𝑒𝑛𝑒𝑟𝑎𝑡𝑖𝑛𝑔...........")
      time.sleep(3)
      #this combination all characters..
      gen = string.ascii_letters + string.punctuation + string.digits
    
      PassWord = "".join(choice(gen) for x in range(randint(10, 30)))
    
      print (Fore.YELLOW+"\n  𝑃𝑎𝑠𝑠𝑤𝑜𝑟𝑑  >>>", PassWord)
      print(Style.RESET_ALL)
    
  if Choice == 3 :
      print()
      print(Fore.YELLOW+" ʜᴀᴠᴇ ᴀ ɢᴏᴏᴅ ᴅᴀʏ !! ")
      break
      print(Style.RESET_ALL)
       
  if Choice == 2 :
    Hash = int(input(Fore.GREEN+''' 
    
  [+] 1.md5                                
  [+] 2.sha512
  [+] 3.sha1
  [+] 4.sha256
  [+] 5.sha384\n  >>> '''))
    
    if Hash == 1 :
      
       hash1 = input("\n  Enter Password >> ")
       print("\n  𝙿𝚕𝚎𝚊𝚜𝚎 𝚆𝚊𝚒𝚝............𝙷𝚊𝚜𝚑_𝙶𝚎𝚗𝚎𝚛𝚊𝚝𝚒𝚗𝚐 !!")
       hash2 = hashlib.md5(hash1.encode("utf-8")).hexdigest()
       time.sleep(3)
       print(f"\n  md5 generated ---> "+ hash2 )
   
    elif Hash == 2 :
  
       h3 = input("\n  Enter Password >> ")
       print("\n  𝙿𝚕𝚎𝚊𝚜𝚎 𝚆𝚊𝚒𝚝............𝙷𝚊𝚜𝚑_𝙶𝚎𝚗𝚎𝚛𝚊𝚝𝚒𝚗𝚐 !!")
       h4 = hashlib.sha512(h3.encode("utf-8")).hexdigest()
       time.sleep(3)
       print(f"\n  sha512 generated ---> " + h4 )
       
   
    elif Hash == 3 :
    
       HASH5 = input("\n  Enter Password >> ")
       print("\n  𝙿𝚕𝚎𝚊𝚜𝚎 𝚆𝚊𝚒𝚝............𝙷𝚊𝚜𝚑_𝙶𝚎𝚗𝚎𝚛𝚊𝚝𝚒𝚗𝚐 !!")
       HASH6 = hashlib.sha1(HASH5.encode("utf-8")).hexdigest()
       time.sleep(3)   
       print(f"\n  sha1 generated ---> " + HASH6 )
    
    elif Hash == 4 :
     
       h7 = input("\n  Enter Password >> ")
       print("\n  𝙿𝚕𝚎𝚊𝚜𝚎 𝚆𝚊𝚒𝚝............𝙷𝚊𝚜𝚑_𝙶𝚎𝚗𝚎𝚛𝚊𝚝𝚒𝚗𝚐 !!")
       h8 = hashlib.sha256(h7.encode("utf-8")).hexdigest()
       time.sleep(3)
       print(f"\n  sha256 generated ---> " + h8 )
       
    elif Hash == 5 :
     
       h9 = input("\n  Enter Password >> ")
       print("\n  𝙿𝚕𝚎𝚊𝚜𝚎 𝚆𝚊𝚒𝚝............𝙷𝚊𝚜𝚑_𝙶𝚎𝚗𝚎𝚛𝚊𝚝𝚒𝚗𝚐 !!")
       h10 = hashlib.sha384(h9.encode("utf-8")).hexdigest()
       time.sleep(3)
       print(f"\n  sha384 generated ---> " + h10 )
       print(Style.RESET_ALL)
       
"""
Hello Guys my name is prem and i am a python programmer
and i am creating this tool for Passwords Generating and Hash Pass generating.

Guys maybe you understand this code 😅 

Good By..Friends

"""
       

     
      
      
  
       
  
