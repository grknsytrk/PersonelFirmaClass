class Personel:
    def girdi(self, ad, departman, calisma_yili, maas):
        self.ad = ad
        self.departman = departman
        self.calisma_yili = calisma_yili
        self.maas = maas

class Firma:
    def girdi(self):
        self.personel_listesi = []

    def personel_ekle(self, personel):
        self.personel_listesi.append(personel)

    def personel_listele(self):
        for personel in self.personel_listesi:
            print(f"Ad: {personel.ad}, Departman: {personel.departman}, Çalışma Yılı: {personel.calisma_yili}, Maaş: {personel.maas}")

    def maas_zammi(self, personel, zam_orani):
        personel.maas *= (1 + zam_orani/100)

    def personel_cikart(self, personel):
        self.personel_listesi.remove(personel)
        
personel1 = Personel()
personel2 = Personel()
personel1.girdi("gurkan", "muhendis", 1, 15000)
personel2.girdi("ali", "güvenlik", 3, 5000)

firma = Firma()
firma.girdi()

firma.personel_ekle(personel1)
firma.personel_ekle(personel2)

firma.personel_listele()
print("\n")

firma.maas_zammi(personel1, 10)

firma.personel_listele()
print("\n")
firma.personel_cikart(personel2)

firma.personel_listele()
