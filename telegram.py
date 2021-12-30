

class Telegram():
    # Обовязковий розділ (Розділ 0 в коді КС-15) для передачі.
    def __init__(self,  BB, iii, YY, GG, n):
        # self.MiMi = MiMiMjMj
        self.BB = BB
        self.iii = iii
        self.YY = YY
        self.GG = GG
        self.n = n

    def index_posta(self):
        self.numbers_baseyny = str(self.BB)
        self.numbers_posta = str(self.iii)
        index_posta = self.numbers_baseyny+self.numbers_posta
        return index_posta


    def date_time_n(self):
        self.date = str(self.YY)
        self.time = str(self.GG)
        self.n_rozdil = str(self.n)
        date_time_n = self.date + self.time + self.n_rozdil
        return  date_time_n


class Rozdil_1(Telegram):
    def __init__(self, grupa ,HHHH):
        self.











i = Telegram(42,130,30,'08',1)

# i(42,130,30,8,1)
print(i.index_posta())
print(i.date_time_n())





