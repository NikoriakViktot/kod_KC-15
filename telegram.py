

class Telegram():
    # Обовязковий розділ (Розділ 0 в коді КС-15) для передачі.
    def __init__(self,  BB = None, iii= None, YY = None, GG=None, n = None):
        # self.MiMi = MiMiMjMj
        self.BB = BB
        self.iii = iii
        self.YY = YY
        self.GG = GG
        # if  n == 1:
        #     self.n = n
        # if n == 2:
        #     self.n = n
        # if n == 3:
        #     self.n = n
        # if n == 7:
        self.n = n


    def index_posta(self):
        numbers_baseyny = str(self.BB)
        numbers_posta = str(self.iii)
        index_posta = numbers_baseyny+numbers_posta
        return index_posta


    def date_time_n(self):
        date = str(self.YY)
        time = str(self.GG)
        n_rozdil = str(self.n)
        date_time_n = date + time + n_rozdil
        return  date_time_n


class Rozdil_1(Telegram):
    def __init__(self, data):
        self.data = data













i = Telegram(42,130,30,'08',1)
g =Telegram(42,130,30,'08',7)

# i(42,130,30,8,1)
print(i.index_posta())
print(i.date_time_n())
print(g.__dict__)

g1 = Telegram(42, 148, "04", '08', 2)
print(g1.date_time_n())



