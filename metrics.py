
def precision(RR, REC):
    try:
        if REC==0:
            raise Exception()
        return RR/REC
    except (Exception):
        print("Cero Documentos recuperados. Division por cero")


def recobrado(RR, REL):
    try:
        if REL==0:
            raise Exception()
        return RR/REL

    except (Exception):
        print("Cero Documentos Relevantes. Division por cero")

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
