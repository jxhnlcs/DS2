from socket_europeu import SocketEuropeu
from chaleira_eletrica import ChaleiraEletrica
from socket_brasileiro import SocketBrasileiro

sochet_europeu = SocketEuropeu()
socket_brasileiro = SocketBrasileiro(SocketEuropeu)
chaleira_eletrica = ChaleiraEletrica(SocketEuropeu)
chaleira_eletrica.ferver()