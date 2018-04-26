import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)           #UDP ' ye uygun bir soket nesnesi oluşturuldu.
server_socket.bind(('', 25400))                                            #Port belirlendi.

while True:                                                                #Belirlenen Port Dinleniyor..

    message, address = server_socket.recvfrom(1024)                        #gelen mesajı al
    print("Ip :",address[0]," Client Portu:",address[1])                   #ekrana paket bilgisi yazdırıldı.
    server_socket.sendto(message, address)                                 #client'a cevap verildi.
