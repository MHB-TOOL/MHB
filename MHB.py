import os, platform, time, sys
os.system('xdg-open https://chat.whatsapp.com/HdppaiQyFtZ1AwiOzc5iEe')
try:
 import requests
except:os.system("pip uninstall requests -y;pip install requests")

print('[*] Loeading Chacking Update.')
os.system('git pull --quiet 2>/dev/null')
bit = platform.architecture()[0]
if bit == '64bit':
 print('[✓] Found 64 Bit Device')
 import MHB64
elif bit == '32bit':
 print('\033[1;97m[✓] Found 32 Bit Device')
 import MHB32
