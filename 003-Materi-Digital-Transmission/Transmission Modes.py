# Transmission Modes
# Simulasi untuk menunjukkan simplex, half-duplex, dan full-duplex mode.
# Oleh : hafizhhasyhari

import time
from threading import Thread

# Simplex Transmission
def simplex(sender, receiver):
    print(f"Sender: {sender} -> Receiver: {receiver}")

# Half-Duplex Transmission
def half_duplex(sender, receiver):
    print(f"Sender: {sender} sends data")
    time.sleep(1)
    print(f"Receiver: {receiver} acknowledges data")

# Full-Duplex Transmission
def full_duplex(sender, receiver):
    def send():
        print(f"Sender: {sender} sends data")
    
    def receive():
        print(f"Receiver: {receiver} sends response")
    
    Thread(target=send).start()
    Thread(target=receive).start()

# Simulations
print("\nSimplex Transmission:")
simplex("Device A", "Device B")

print("\nHalf-Duplex Transmission:")
half_duplex("Device A", "Device B")

print("\nFull-Duplex Transmission:")
full_duplex("Device A", "Device B")
