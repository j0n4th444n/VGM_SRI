import math

def precision(RR, REC):
    return RR/REC

def recobrado(RR, REL):
    return RR/REL

def f_medida(RR, REL, REC):
    P = precision(RR, REC)
    R = recobrado(RR, REL)
    return (2*P*R)/(P+R)

def e_medida(RR, REL, REC, Beta):
    P = precision(RR, REC)
    R = recobrado(RR, REL)
    return ((1+ Beta**2)*P*R) / (Beta**2*P + R)

def r_presicion(RR,REC,REL):
    P = precision(RR, REC)
    R = recobrado(RR, REL)
    return P / R
