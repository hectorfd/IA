from orden import Orden
from computadora import Computadora
from monitor import Monitor
from dispositivos_entrada import Raton
from dispositivos_entrada import Teclado

# Crear una orden con computadoras y dispositivos
orden = Orden()
orden.add_computadora("Gamer PC")

# Añadir dispositivos a la primera computadora
pc = orden.list_computadoras[0]
pc.add_monitor("Samsung", 27.0)
pc.add_raton("Logitech", "USB")
pc.add_teclado("Razer", "Mecánico")

# Añadir otra computadora
orden.add_computadora("Desktop")

# Añadir dispositivos a la segunda computadora
pc2 = orden.list_computadoras[1]
pc2.add_monitor("Dell", 24.0)
pc2.add_raton("Microsoft", "Bluetooth")
pc2.add_teclado("Apple", "Mecánico")

print(orden)  # Muestra la orden con detalles