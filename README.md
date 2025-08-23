
## 📲 Connect
Check out my LinkedIn post about this project where you can see the LEDs dance to music 👉  
[View on LinkedIn](www.linkedin.com/in/anuragsahooiiitg)



## Why I Built It 🎶💡

I’ve always been fascinated by how **music can be seen as well as heard**. Watching lights respond to beats brings sound to life in a completely different way.  

During my summer holidays, I wanted to learn **Python**—since it’s such a widely used language in software development, automation, and creative projects. At the same time, I was a member of our college Music Club *Tarang* under the band *Fusion*.  

🎤 Singing has always been a dear hobby to me, but I couldn’t contribute much to the band as I was heavily involved in the Robotics Club *Technocrats*.  

So, I thought of building a project that would **bridge this gap between my love for music and my interest in technology**. The **LED Music Visualizer** became that project. I absolutely enjoyed the process—every run gave me a chance to see my voice come alive through lights and improve it further.  

✨ And when it finally worked, I found myself singing for hours, mesmerized by how the lights danced with my voice.  

![Demo_Visualiser](DemoVisualizer.gif)

## ⚙️ How It Works  

This project is a **two-part system**:  

### 1. Python Script (PC/Laptop)  
- 🎤 Captures live audio from the microphone.  
- 📊 Uses **Fast Fourier Transform (FFT)** to split audio into three frequency bands: **bass, mids, and highs**.  
- 🎨 Maps each band’s strength to an **RGB color value**.  
- 🔗 Sends RGB values over **Serial** to the ESP32.  

### 2. ESP32 Microcontroller  
- 📥 Receives the RGB values from Python.  
- 💡 Updates the **WS2812B LED strip** in real time.  
- ✨ LEDs glow and change dynamically with the music.  

---

## 🚀 Features  
- 🎵 **Real-time Audio Analysis** – processes live sound from any microphone.  
- 🎚️ **Frequency Band Separation** – bass, mids, and highs mapped to RGB colors.  
- 🔗 **Seamless Serial Communication** – Python sends RGB values directly to ESP32.  
- 💡 **WS2812B NeoPixel Control** – syncs addressable LEDs with music.  

![Demo_Visualiser2](DemoVisualizer2compressor.gif)
---

## 🛠️ Hardware Requirements  
- 🔲 **ESP32 Microcontroller**  
- 🌈 **WS2812B NeoPixel LED Strip**  
- 🔌 **USB Cable** (for flashing & serial communication)  
- 🎤 **Microphone** connected to your computer


## 5) Software & Dependencies

### Python
Install the required libraries:
1. Pyserial  
2. Sounddevice  
3. Numpy  
4. Soundfile  

### Arduino
The ESP32 sketch requires the **Adafruit NeoPixel** library.  
Install it via Arduino IDE → **Library Manager** → Search *Adafruit NeoPixel* → Install.  

---

## 6) Setup & Installation

### Step 1: Flash the ESP32
1. Open `Code_Serial_music_dance.ino` in Arduino IDE.  
2. Set `NUM_LEDS` to match your LED strip (default: 300).  
3. Ensure `LED_PIN` is the GPIO pin used (default: 5).  
4. Connect ESP32 via USB → Select correct **Board** & **Port**.  
5. Upload the code.  

### Step 2: Configure the Python Script
1. Open `microphone_server_frequency.py`.  
2. Change `SERIAL_PORT` to your ESP32 port:  
   - Windows → `COM3`  
   - Linux/macOS → `/dev/ttyUSB0`  

### Step 3: Run the Visualizer

Run the python code in your bash or any other IDE -> microphone_server_frequency.py

The script will start listening to your microphone and stream RGB values to your ESP32. LEDs will respond in real time!


 ## Contributing
Contributions are welcome!  
- Add new lighting patterns 🎨  
- Optimize audio processing ⚡  
- Improve synchronization 🕹️  

---

## License
This project is licensed under the **MIT License**.  
See [LICENSE.md](LICENSE) for details.  

