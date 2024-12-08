# Sampling Sinusoidal Signal
def analog_to_digital(frequency, sampling_rate, duration, quantization_levels):
    t = np.linspace(0, duration, int(sampling_rate * duration))
    signal = np.sin(2 * np.pi * frequency * t)
    
    # Quantization
    quantized_signal = np.round(signal * quantization_levels) / quantization_levels
    
    # Plotting
    plt.figure(figsize=(10, 6))
    plt.plot(t, signal, label="Original Signal", color='blue')
    plt.stem(t, quantized_signal, linefmt='r-', markerfmt='ro', basefmt='k', label="Quantized Signal")
    plt.title("Analog to Digital Conversion")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.legend()
    plt.grid()
    plt.show()
    
    return quantized_signal

# Parameters
frequency = 5  # Hz
sampling_rate = 50  # Samples per second
duration = 1  # Second
quantization_levels = 16  # Number of levels

# Call function
analog_to_digital(frequency, sampling_rate, duration, quantization_levels)
