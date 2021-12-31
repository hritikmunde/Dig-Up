import os
import sys
from time import sleep
from modules.logo import *
from modules.system import *

yellow="\033[1;33m"
blue="\033[1;34m"
nc="\033[00m"

class tool:
  @classmethod
  def install(self):
    while True:
      system=sys()
      os.system("clear")
      logo.ins_tnc()
      inp=input(f"{yellow}Do you want to install Dig-Up [Y/n]> {nc}")
      if inp=="y" or inp=="Y":
        os.system("clear")
        logo.installing()
        if system.sudo is not None:
          #require root permission
          if os.path.exists(system.conf_dir+"/Dig-Up"):
            pass
          else:
            os.system(system.sudo+" mkdir "+system.conf_dir+"/Dig-Up")
          os.system(system.sudo+" cp -r modules core Dig-Up.py "+system.conf_dir+"/Dig-Up")
          os.system(system.sudo+" cp -r core/Dig-Up "+system.bin)
          os.system(system.sudo+" cp -r core/digup "+system.bin)
          os.system(system.sudo+" chmod +x "+system.bin+"/Dig-Up")
          os.system(system.sudo+" chmod +x "+system.bin+"/digup")
          os.system("cd .. && "+system.sudo+" rm -rf Dig-Up")
          if os.path.exists(system.bin+"/Dig-Up") and os.path.exists(system.conf_dir+"/Dig-Up"):
            os.system("clear")
            logo.ins_sc()
            tmp=input(f"{blue}Dig-Up{nc}@{blue}space {yellow}$ {nc}")
            break
          else:
            os.system("clear")
            logo.not_ins()
            tmp=input(f"{blue}Dig-Up{nc}@{blue}space {yellow}$ {nc}")
            break
        else:
          if os.path.exists(system.conf_dir+"/Dig-Up"):
            pass
          else:
            os.system("mkdir "+system.conf_dir+"/Dig-Up")
          os.system("cp -r modules core Dig-Up.py "+system.conf_dir+"/Dig-Up")
          os.system("cp -r core/Dig-Up "+system.bin)
          os.system("cp -r core/digup "+system.bin)
          os.system("chmod +x "+system.bin+"/Dig-Up")
          os.system("chmod +x "+system.bin+"/digup")
          os.system("cd .. && rm -rf Dig-Up")
          if os.path.exists(system.bin+"/Dig-Up") and os.path.exists(system.conf_dir+"/Dig-Up"):
            os.system("clear")
            logo.ins_sc()
            tmp=input(f"{blue}Dig-Up{nc}@{blue}space {yellow}$ {nc}")
            break
          else:
            os.system("clear")
            logo.not_ins()
            tmp=input(f"{blue}Dig-Up{nc}@{blue}space {yellow}$ {nc}")
            break
      else:
        break

if __name__=="__main__":
  try:
    tool.install()
  except KeyboardInterrupt:
    os.system("clear")
    logo.exit()
