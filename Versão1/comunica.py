import socket

def send(message, seqnum, destination):
    # Cria um socket UDP
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        m = message.encode()

        # Envia a mensagem para o destino
        s.sendto(m, (destination, 5000))   

