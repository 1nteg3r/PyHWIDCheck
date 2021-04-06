import requests
import subprocess
def HWID():
    cmd = 'wmic csproduct get uuid'
    uuid = str(subprocess.check_output(cmd))
    pos1 = uuid.find("\\n")+2
    uuid = uuid[pos1:-15]
    return uuid
print(f"Your HWID is {HWID()} ")
hwid_auth = requests.get("RAW PASTEBIN LINK WITH THE HWIDS ADDED")
if HWID() in hwid_auth.text:
    print("Welcome")
else:
    print("Your HWID was not found in our database!")
