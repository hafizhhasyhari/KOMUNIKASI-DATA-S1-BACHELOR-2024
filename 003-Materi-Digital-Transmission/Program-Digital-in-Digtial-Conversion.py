import matplotlib.pyplot as plt
import numpy as np

# Data biner untuk dikonversi
data = [1, 0, 1, 1, 0, 0, 1]

# Fungsi untuk NRZ-L Encoding
def nrz_l(data):
    return [-1 if bit == 0 else 1 for bit in data]

# Fungsi untuk NRZ-I Encoding
def nrz_i(data):
    signal = []
    current = 1
    for bit in data:
        if bit == 1:
            current *= -1
        signal.append(current)
    return signal

# Fungsi untuk Manchester Encoding
def manchester(data):
    signal = []
    for bit in data:
        if bit == 1:
            signal += [1, -1]
        else:
            signal += [-1, 1]
    return signal

# Fungsi untuk Differential Manchester Encoding
def diff_manchester(data):
    signal = []
    current = -1
    for bit in data:
        if bit == 0:
            signal += [current, -current]
        else:
            current *= -1
            signal += [current, -current]
    return signal

# Visualisasi
def plot_signals(data, signals, titles):
    plt.figure(figsize=(12, 8))
    for i, (signal, title) in enumerate(zip(signals, titles)):
        plt.subplot(len(signals), 1, i + 1)
        plt.step(range(len(signal)), signal, where='post')
        plt.ylim([-2, 2])
        plt.title(title)
        plt.grid()
    plt.tight_layout()
    plt.show()

# Generate signals
nrz_l_signal = nrz_l(data)
nrz_i_signal = nrz_i(data)
manchester_signal = manchester(data)
diff_manchester_signal = diff_manchester(data)

# Plot
plot_signals(data, [nrz_l_signal, nrz_i_signal, manchester_signal, diff_manchester_signal],
             ["NRZ-L", "NRZ-I", "Manchester", "Differential Manchester"])
