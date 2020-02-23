class Kalkulator(object):

    def jumlah(self, a, b):
        return (a+b)

    def kurang(self, a, b):
        return (a-b)

if __name__ == "__main__":
    k = Kalkulator()
    print(k.jumlah(20,20))