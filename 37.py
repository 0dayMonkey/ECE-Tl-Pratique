class AdresseIP:

    def __init__(self, adresse):
        self.adresse = adresse
   
    def liste_octet(self):
        return [int(i) for i in self.adresse.split('.')]
        
    def est_reservee(self):
        return self.adresse in ('192.168.0.0', '192.168.0.255')
             
    def adresse_suivante(self):
        octet_nouveau = self.liste_octet()[3] + 1
        if octet_nouveau <= 254:
            return AdresseIP('192.168.0.' + str(octet_nouveau))
        else:
            return False
