#****** SENDER *****
import time
import socket

IP = input("ENTER IP : ")                                               #Hedef IP adresi alındı.
adress = (IP, 25400)                                                    #Port numarası ve IP ile adres oluşturuldu.

PacketCounter = 0                                                         #Toplam paket sayacına başlangıç değeri atandı.
PacketLossCounter = 0                                                     #Kayıp paket sayacına başlangıç değeri atandı.

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)        #UDP'ye uygun bir socket nesnesi oluşturuldu.
client_socket.settimeout(2.0)                                           #Timeout süresi 2 sn olarak belirlendi.

for pings in range(1, 7):                                                #6 paket için gerekli döngü
    message = str(pings)+". Ping Message"                               #Mesaj oluşturuldu.
    message = message.encode()                                          #Binary formata çevirildi.

    start = time.time()                                                 #Paketin göderilmeye başlandığı zaman tutuldu.
    client_socket.sendto(message, adress)                               #Paket gönderildi
    PacketCounter = PacketCounter+1                                       #Toplam paket sayacı 1 artırıldı.

    try:
        data, server = client_socket.recvfrom(1024)                     #gönderilen mesajdan cevap geldi.
        end = time.time()                                               #pakedin cevap gelme süresi tutuldu.
        elapsed = end - start                                           #Cevap gelmesi için gereken süre bulundu.

        print(f'+ Data :  {data} - Size : {len(data)}byte - Ping : {pings} - Time : {elapsed}sn State : OK')#Paket Bilgileri yazıdırıldı

    except socket.timeout:                                                #Timeout hatası yakalanır ise
        PacketLossCounter = PacketLossCounter+1                           #Kayıp paket sayacını artır.
        print("- Ping ", pings, ': REQUEST TIMED OUT - State : Failed')   #Ekrana hangi ping in Timeout Olduğu mesajını göster.

#Sonuç Çıktısı
print("\n\n\t\t\t\t\t\t\t\t\t\t|*** RESULT *** |\n")
print(f" IP : [{IP}] - Total Packet Count : [{PacketCounter}] - Arrived Packet Count: [{PacketCounter-PacketLossCounter}]"
      f" - Packet Loss Count : [{PacketLossCounter}]")
