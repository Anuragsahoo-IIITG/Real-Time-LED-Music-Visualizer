import numpy as np
import soundfile as sf
import sounddevice as sd
import serial
import time

# Use coe_music_dance on ESP32

# --- Config ---
SERIAL_PORT = 'COM3'       # Change this to match your ESP32 port
CHUNK_SIZE = 1024          # Samples per chunk

# --- Serial Setup ---
ser = serial.Serial(SERIAL_PORT, 115200)
time.sleep(2)

samplerate = 44100  # microphone supports (44.1kHz is standard)

def callback(indata, frames, time_info, status):
    chunk = indata[:, 0]  # Use first channel

    # --- Frequency Analysis ---
    fft = np.fft.fft(chunk)
    magnitude = np.abs(fft[:len(fft)//2])

    # --- Frequency Band Splitting ---
    bass = np.sum(magnitude[0:50])        # ~0–500 Hz
    mids = np.sum(magnitude[50:100])      # ~500–2000 Hz
    highs = np.sum(magnitude[100:])       # ~2000+ Hz

    # --- Normalize Each Band to 0–255 ---
    r = int(np.interp(bass, [5, 2000], [0, 180]))
    g = int(np.interp(mids, [5, 2000], [0, 180]))
    b = int(np.interp(highs, [5, 2000], [0, 180]))

    r = max(0, min(r, 255))
    g = max(0, min(g, 255))
    b = max(0, min(b, 255))

    # --- Send RGB to ESP32 ---
    try:
        ser.write(bytes([r, g, b]))
    except:
        pass



with sd.InputStream(channels=1, callback=callback, samplerate=samplerate, blocksize=CHUNK_SIZE):
    print("Listening from microphone... Press Ctrl+C to stop.")
    while True:
        time.sleep(0.1)

