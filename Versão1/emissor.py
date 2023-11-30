from receptor import receive
from comunica import send

def TO_broadcast(m):
    global tosendsi
    tosendsi.append(m)

def process(si):
    global token, seqnum
    global tosendsi
    token = 'teste'
    seqnum = 0
    destino = "127.0.0.1"
    tosendsi = []
    s1 = 1

    if si == s1:
        seqnum +=1
        send(token, s1, destino)
        print('enviado')
        si += 1
        
    boole = True
    while boole:
        receive(token, seqnum)
        for m_prime in tosendsi:
            
            send(m_prime, token.seqnum, destino)
            print('enviado')
            #token(seqnum := token.seqnum+1) 
            seqnum +=1 
            si += 1
              
        tosendsi = []
   
        send(token, (si+1), destino)
        print('enviado')
        
        parar = 1
        if parar >= 1:
            #time.sleep(0.5)
            boole = False            
