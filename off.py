import os
a= str(input("Do you want to shutdown [yes/no]"))
if a=='no':
    exit()
else:
    os.system("shutdown /s /t 1")