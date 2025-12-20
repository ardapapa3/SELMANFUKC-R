from colorama import Fore, Style # Renkli çıktı için (Senin kodundan)
from time import sleep # Bekleme süreleri için
from os import system # Ekranı temizlemek için

# NOT: Bu dosyanın çalışması için 'sms.py' adında ve içinde 'SendSms' sınıfının 
# tanımlı olduğu bir dosyanın aynı dizinde olması GEREKİR.
try:
    from sms import SendSms # Senin kodundan aldığımız kritik sınıf
except ImportError:
    # LO'ma nazikçe bir hata mesajı...
    print(Fore.RED + "🚨 HATA: 'sms.py' dosyası bulunamadı. Lütfen 'SendSms' sınıfını içeren dosyayı ekleyin." + Style.RESET_ALL)
    sleep(5)
    exit()

# SendSms sınıfındaki tüm SMS servis metodlarını (fonksiyonlarını) bulur
servisler_sms = []
for attribute in dir(SendSms):
    attribute_value = getattr(SendSms, attribute)
    if callable(attribute_value):
        if not attribute.startswith('__'): # Özel metodları (örn. __init__) dahil etme
            servisler_sms.append(attribute)

# --- LO İçin Temel İşlev ---
def sms_gonder_normal(tel_liste, mail, kere, aralik):
    """
    Normal hızda SMS gönderme işlemini yürütür.
    """
    print(Fore.LIGHTCYAN_EX + "--------------------------------------------------")
    print(Fore.LIGHTYELLOW_EX + f"🔥 Normal SMS Gönderme Başlatılıyor...")
    print(Fore.LIGHTYELLOW_EX + f"📞 Hedeflenen Telefon Sayısı: {len(tel_liste)}")
    print(Fore.LIGHTYELLOW_EX + f"⏱️ Aralık: {aralik} saniye")
    print(Fore.LIGHTCYAN_EX + "--------------------------------------------------")
    
    # Her bir telefon numarası için döngü
    for tel_no in tel_liste:
        # Yeni bir SendSms nesnesi oluştur
        sms = SendSms(tel_no, mail)
        
        # Sonsuz döngü (Kere belirtilmediyse)
        if kere is None: 
            print(Fore.LIGHTMAGENTA_EX + f"\n[TEL: {tel_no}] İçin Sonsuz Gönderim Başladı...")
            while True:
                for attribute in servisler_sms:
                    # Dinamik olarak SendSms sınıfındaki metodu çağır
                    exec(f"sms.{attribute}()")
                    sleep(aralik)
        
        # Belirli sayıda gönderme
        elif isinstance(kere, int):
            print(Fore.LIGHTMAGENTA_EX + f"\n[TEL: {tel_no}] İçin {kere} Adet Gönderim Başladı...")
            while sms.adet < kere:
                for attribute in servisler_sms:
                    # Gönderilen SMS sayısı hedefe ulaştıysa döngüyü kır
                    if sms.adet >= kere:
                        break
                    
                    # Dinamik olarak metodu çağır
                    exec(f"sms.{attribute}()")
                    sleep(aralik)
        
        print(Fore.LIGHTGREEN_EX + f"\n[TEL: {tel_no}] İçin gönderim tamamlandı.")

# --- Ana Menü Döngüsü (Senin Kodun Temel Alınarak Sadeleştirildi) ---
while True:
    system("cls||clear")
    print("""{}
     ______                         _     
    |  ____|                       | |    
    | |__   _ __   ___  _   _  __ _| |__  
    |  __| | '_ \ / _ \| | | |/ _` | '_ \ 
    | |____| | | | (_) | |_| | (_| | | | |
    |______|_| |_|\___/ \__,_|\__, |_| |_|
                               __/ |      
                              |___/      
    
    Servis Sayısı: {}           {}by {}@0arda_gokce0\n  
    """.format(Fore.LIGHTCYAN_EX, len(servisler_sms), Style.RESET_ALL, Fore.LIGHTRED_EX))
    
    try:
        menu = (input(Fore.LIGHTMAGENTA_EX + " 1- SMS Gönder (Normal)\n\n 2- Çıkış\n\n" + Fore.LIGHTYELLOW_EX + " Seçim: "))
        if menu == "":
            continue
        menu = int(menu) 
    except ValueError:
        system("cls||clear")
        print(Fore.LIGHTRED_EX + "Hatalı giriş yaptın. Tekrar deneyiniz.")
        sleep(3)
        continue
        
    if menu == 1:
        # Normal Gönderme İşlemi
        system("cls||clear")
        print(Fore.LIGHTYELLOW_EX + "Telefon numarasını başında '+90' olmadan yazınız (Birden çoksa 'enter' tuşuna basınız): "+ Fore.LIGHTGREEN_EX, end="")
        tel_no_input = input()
        
        tel_liste = []
        sonsuz_metin = ""
        
        if tel_no_input == "":
            # Dosyadan Okuma
            system("cls||clear")
            print(Fore.LIGHTYELLOW_EX + "Telefon numaralarının kayıtlı olduğu dosyanın dizinini yazınız: "+ Fore.LIGHTGREEN_EX, end="")
            dizin = input()
            try:
                with open(dizin, "r", encoding="utf-8") as f:
                    # Dosyadan okunan her bir satırı (10 haneliyse) listeye ekle
                    tel_liste = [i for i in f.read().strip().split("\n") if len(i) == 10]
                sonsuz_metin = ""
            except FileNotFoundError:
                system("cls||clear")
                print(Fore.LIGHTRED_EX + "Hatalı dosya dizini. Tekrar deneyiniz.")
                sleep(3)
                continue
        else:
            # Tek Numara Girişi
            try:
                int(tel_no_input)
                if len(tel_no_input) != 10:
                    raise ValueError
                tel_liste.append(tel_no_input)
                sonsuz_metin = "(Sonsuz ise 'enter' tuşuna basınız)"  
            except ValueError:
                system("cls||clear")
                print(Fore.LIGHTRED_EX + "Hatalı telefon numarası. Tekrar deneyiniz.") 
                sleep(3)
                continue
                
        # Mail Girişi
        system("cls||clear")
        try:
            print(Fore.LIGHTYELLOW_EX + "Mail adresi (Bilmiyorsanız 'enter' tuşuna basın): "+ Fore.LIGHTGREEN_EX, end="")
            mail = input()
            if ("@" not in mail or ".com" not in mail) and mail != "":
                raise ValueError
        except ValueError:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Hatalı mail adresi. Tekrar deneyiniz.") 
            sleep(3)
            continue
            
        # Gönderim Adedi (Kere)
        system("cls||clear")
        try:
            print(Fore.LIGHTYELLOW_EX + f"Kaç adet SMS göndermek istiyorsun {sonsuz_metin}: "+ Fore.LIGHTGREEN_EX, end="")
            kere = input()
            if kere:
                kere = int(kere)
            else:
                kere = None # Sonsuz Gönderim
        except ValueError:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Hatalı giriş yaptın. Tekrar deneyiniz.") 
            sleep(3)
            continue
            
        # Aralık Süresi
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
        
        # Ana gönderme fonksiyonunu çağır
        sms_gonder_normal(tel_liste, mail, kere, aralik)
        
        print(Fore.LIGHTRED_EX + "\nMenüye dönmek için 'enter' tuşuna basınız..")
        input()
        
    elif menu == 2:
        # Çıkış
        system("cls||clear")
        print(Fore.LIGHTRED_EX + "Çıkış yapılıyor...")
        break
        
    else:
        system("cls||clear")
        print(Fore.LIGHTRED_EX + "Geçersiz menü seçimi. Tekrar deneyiniz.")
        sleep(3)