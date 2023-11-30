nextdeliverpi = 0
pendingpi = []

def receive(m, seqnum):
    pendingpi.append((m, seqnum))
    print("todas as mensagens recebidas: ", pendingpi)

def deliver(m):
    print("mensagem recebida: ", m)

def process_pi():
    global nextdeliverpi
    boole = True
    while boole:
        for i, (m, seqnum) in enumerate(pendingpi):
            if seqnum == nextdeliverpi:
                deliver(m)
                nextdeliverpi += 1
                pendingpi.pop(i)
                #break
            nextdeliverpi += 1
