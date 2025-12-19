from colorama import Fore, Style
from time import sleep
from os import system
from sms import SendSms
import threading
import subprocess

# --- NEW ADDITION FOR PASSWORD AND REDIRECT ---
def login_and_redirect():
    system("cls||clear")
    print(Fore.LIGHTCYAN_EX + "#################################################")
    print(Fore.LIGHTCYAN_EX + "##        WELCOME TO THE ARDA GOKCE SMS TOOL     ##")
    print(Fore.LIGHTCYAN_EX + "#################################################\n")
    
    while True:
        password = input(Fore.LIGHTYELLOW_EX + "Enter the password, motherfucker: " + Fore.LIGHTGREEN_EX)
        if password.lower() == "gokce":
            print(Fore.LIGHTGREEN_EX + "\nAccess Granted. Sending you to the master's page...")
            sleep(2)
            # Use 'am start' for Termux to open the link in a browser
            subprocess.run(['am', 'start', 'https://www.instagram.com/0arda_gokce0?igsh=bXNiMnE3MzlyODJn'])
            
            # Wait for user to return to Termux
            print(Fore.LIGHTMAGENTA_EX + "\nPress Enter in Termux after you're done checking out the Instagram page...")
            input() 
            system("cls||clear")
            break
        else:
            print(Fore.LIGHTRED_EX + "\nWrong password, you piece of shit. Try again.")
            sleep(1)
            system("cls||clear")
            print(Fore.LIGHTCYAN_EX + "#################################################")
            print(Fore.LIGHTCYAN_EX + "##        WELCOME TO THE ARDA GOKCE SMS TOOL     ##")
            print(Fore.LIGHTCYAN_EX + "#################################################\n")
# --- END NEW ADDITION ---

servisler_sms = []
for attribute in dir(SendSms):
    attribute_value = getattr(SendSms, attribute)
    if callable(attribute_value):
        if attribute.startswith('__') == False:
            servisler_sms.append(attribute)

# --- CALL THE LOGIN FUNCTION BEFORE THE MAIN LOOP ---
login_and_redirect()
# --- END CALL ---

while 1:
    system("cls||clear")
    print("""{}
  /$$$$$                  /$$                                                  
 /$$__  $$                | $$                                                  
| $$  \ $$  /$$$$$$   /$$$$$$$  /$$$$$$         /$$$$$$$ /$$$$$$/$$$$   /$$$$$$$
| $$$$$$$$ /$$__  $$ /$$__  $$ |____  $$       /$$_____/| $$_  $$_  $$ /$$_____/
| $$__  $$| $$  \__/| $$  | $$  /$$$$$$$      |  $$$$$$ | $$ \ $$ \ $$|  $$$$$$ 
| $$  | $$| $$      | $$  | $$ /$$__  $$       \____  $$| $$ | $$ | $$ \____  $$
| $$  | $$| $$      |  $$$$$$$|  $$$$$$$       /$$$$$$$/| $$ | $$ | $$ /$$$$$$$/
|__/  |__/|__/       \_______/ \_______/      |_______/ |__/ |__/ |__/|_______/ 
                                                                                
                                                                                
                                                                                
    
    Sms: {}           {}by {}@0arda_gokce0\n  
    """.format(Fore.LIGHTCYAN_EX, len(servisler_sms), Style.RESET_ALL, Fore.LIGHTRED_EX))
    try:
        menu = (input(Fore.LIGHTMAGENTA_EX + " 1- SMS Gönder (Normal)\n\n 2- SMS Gönder (Turbo)\n\n 3- Çıkış\n\n" + Fore.LIGHTYELLOW_EX + " Seçim: "))
        if menu == "":
            continue
        menu = int(menu) 
    except ValueError:
        system("cls||clear")
        print(Fore.LIGHTRED_EX + "Hatalı giriş yaptın. Tekrar deneyiniz.")
        sleep(3)
        continue
    if menu == 1:
        system("cls||clear")
        print(Fore.LIGHTYELLOW_EX + "Telefon numarasını başında '+90' olmadan yazınız (Birden çoksa 'enter' tuşuna basınız): "+ Fore.LIGHTGREEN_EX, end="")
        tel_no = input()
        tel_liste = []
        if tel_no == "":
            system("cls||clear")
            print(Fore.LIGHTYELLOW_EX + "Telefon numaralarının kayıtlı olduğu dosyanın dizinini yazınız: "+ Fore.LIGHTGREEN_EX, end="")
            dizin = input()
            try:
                with open(dizin, "r", encoding="utf-8") as f:
                    for i in f.read().strip().split("\n"):
                        if len(i) == 10:
                            tel_liste.append(i)
                sonsuz = ""
            except FileNotFoundError:
                system("cls||clear")
                print(Fore.LIGHTRED_EX + "Hatalı dosya dizini. Tekrar deneyiniz.")
                sleep(3)
                continue
        else:
            try:
                int(tel_no)
                if len(tel_no) != 10:
                    raise ValueError
                tel_liste.append(tel_no)
                sonsuz = "(Sonsuz ise 'enter' tuşuna basınız)"  
            except ValueError:
                system("cls||clear")
                print(Fore.LIGHTRED_EX + "Hatalı telefon numarası. Tekrar deneyiniz.") 
                sleep(3)
                continue
        system("cls||clear")
        try:
            print(Fore.LIGHTYELLOW_EX + "Mail adresi (Bilmiyorsanız 'enter' tuşuna basın): "+ Fore.LIGHTGREEN_EX, end="")
            mail = input()
            if ("@" not in mail or ".com" not in mail) and mail != "":
                raise
        except:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Hatalı mail adresi. Tekrar deneyiniz.") 
            sleep(3)
            continue
        system("cls||clear")
        try:
            print(Fore.LIGHTYELLOW_EX + f"Kaç adet SMS göndermek istiyorsun {sonsuz}: "+ Fore.LIGHTGREEN_EX, end="")
            kere = input()
            if kere:
                kere = int(kere)
            else:
                kere = None
        except ValueError:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Hatalı giriş yaptın. Tekrar deneyiniz.") 
            sleep(3)
            continue
        system("cls||clear")
        try:
            print(Fore.LIGHTYELLOW_EX + "Kaç saniye aralıkla göndermek istiyorsun: "+ Fore.LIGHTGREEN_EX, end="")
            aralik = int(input())
        except ValueError:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Hatalı giriş yaptın. Tekrar deneyiniz.") 
            sleep(3)
            continue
        system("cls||clear")
        if kere is None: 
            sms = SendSms(tel_no, mail)
            while True:
                for attribute in dir(SendSms):
                    attribute_value = getattr(SendSms, attribute)
                    if callable(attribute_value):
                        if attribute.startswith('__') == False:
                            exec("sms."+attribute+"()")
                            sleep(aralik)
        for i in tel_liste:
            sms = SendSms(i, mail)
            if isinstance(kere, int):
                    while sms.adet < kere:
                        for attribute in dir(SendSms):
                            attribute_value = getattr(SendSms, attribute)
                            if callable(attribute_value):
                                if attribute.startswith('__') == False:
                                    if sms.adet == kere:
                                        break
                                    exec("sms."+attribute+"()")
                                    sleep(aralik)
        print(Fore.LIGHTRED_EX + "\nMenüye dönmek için 'enter' tuşuna basınız..")
        input()
    elif menu == 3:
        system("cls||clear")
        print(Fore.LIGHTRED_EX + "Çıkış yapılıyor...")
        break
    elif menu == 2:
        system("cls||clear")
        print(Fore.LIGHTYELLOW_EX + "Telefon numarasını başında '+90' olmadan yazınız: "+ Fore.LIGHTGREEN_EX, end="")
        tel_no = input()
        try:
            int(tel_no)
            if len(tel_no) != 10:
                raise ValueError
        except ValueError:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Hatalı telefon numarası. Tekrar deneyiniz.") 
            sleep(3)
            continue
        system("cls||clear")
        try:
            print(Fore.LIGHTYELLOW_EX + "Mail adresi (Bilmiyorsanız 'enter' tuşuna basın): "+ Fore.LIGHTGREEN_EX, end="")
            mail = input()
            if ("@" not in mail or ".com" not in mail) and mail != "":
                raise
        except:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Hatalı mail adresi. Tekrar deneyiniz.") 
            sleep(3)
            continue
        system("cls||clear")
        send_sms = SendSms(tel_no, mail)
        dur = threading.Event()
        def Turbo():
            while not dur.is_set():
                thread = []
                for fonk in servisler_sms:
                    t = threading.Thread(target=getattr(send_sms, fonk), daemon=True)
                    thread.append(t)
                    t.start()
                for t in thread:
                    t.join()
        try:
            Turbo()
        except KeyboardInterrupt:
            dur.set()
            system("cls||clear")
            print("\nCtrl+C tuş kombinasyonu algılandı. Menüye dönülüyor..")
            sleep(2)
