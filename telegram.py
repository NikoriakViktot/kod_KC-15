

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










i = Telegram(42,130,30,8,1)

# i(42,130,30,8,1)
print(i.index_posta())





