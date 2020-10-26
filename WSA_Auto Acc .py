import pyautogui
pyautogui.FAILSAFE = True
pyautogui.PAUSE = 5.0


pyautogui.size()
n=0
x=5

#Gathering Information for pkms and accountn ninfo
Username= pyautogui.prompt('Username for PKMS')
Password= pyautogui.password('Password for PKMS')
acc_nums= pyautogui.prompt ('How many accounts do you want to create')
Temp=pyautogui.prompt('Cal1 temp or cal 2')
#Opening pkms
pyautogui.press('home')
pyautogui.write('wsa')
pyautogui.write (Username)
pyautogui.press('tab')
pyautogui.write (Password)
pyautogui.write ('23')

#Looping to create accounts and add in excel
while acc_nums <= 0:
    Acc_Full_Name= pyautogui.prompt('Enter the full name of the account being create')
    Acc_User_Name=pyautogui.prompt('Enter the UserID')
    Acc_Password_Name=pyautogui.prompt('Enter the Password')
    pyautogui.hotkey('alt', 'tab', interval=0.1)
    #Write in Excel
    pyautogui.write(Acc_Full_Name)
    pyautogui.press('tab')
    pyautogui.write(Acc_User_Name)
    pyautogui.press('tab')
    pyautogui.write(Acc_Password_Name)
    pyautogui.press('enter')
    pyautogui.hotkey('alt', 'tab', interval=0.1)
    #Excel Done, Inputting in pkms
    pyautogui.write('1')
    pyautogui.write('Temp1')
    pyautogui.press('enter')
    pyautogui.press('down')
    pyautogui.write('3')
    pyautogui.press('enter')
    pyautogui.write(Acc_User_Name)
    pyautogui.press('tab')
    pyautogui.write(Acc_Password_Name)
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.write(Temp + ' ' + Acc_Full_Name)
    pyautogui.press('enter')
    pyautogui.press('f12')
    pyautogui.press('f12')
    #PKMS step 1 complete moving to step too
    pyautogui.write('2')
    pyautogui.press('enter')
    pyautogui.write('temp1')
    pyautogui.press('enter')
    pyautogui.write('3')
    pyautogui.press('enter')
    pyautogui.write(Acc_Full_Name)
    pyautogui.press('enter')
    pyautogui.write(Acc_Full_Name)
    pyautogui.press('tab')
    pyautogui.write(Acc_Password_Name)
    pyautogui.press('f16')
    pyautogui.press('f12')
    pyautogui.press('f12')
    acc_nums -=1
    #Complete
    




