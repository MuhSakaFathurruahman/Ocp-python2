from karakter import Karakter
from pengendara import Pengendara
from show import Shower

showing = Karakter("Udin", 100)
user = Pengendara()
tampil = Shower()

tampil.show_nama(showing, user)
tampil.show_power(showing, user)