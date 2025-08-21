## Why I Built It 🎶💡

I’ve always been fascinated by how **music can be seen as well as heard**. Watching lights respond to beats brings sound to life in a completely different way.  

During my summer holidays, I wanted to learn **Python**—since it’s such a widely used language in software development, automation, and creative projects. At the same time, I was a member of our college Music Club *Tarang* under the band *Fusion*.  

🎤 Singing has always been a dear hobby to me, but I couldn’t contribute much to the band as I was heavily involved in the Robotics Club *Technocrats*.  

So, I thought of building a project that would **bridge this gap between my love for music and my interest in technology**. The **LED Music Visualizer** became that project. I absolutely enjoyed the process—every run gave me a chance to see my voice come alive through lights and improve it further.  

✨ And when it finally worked, I found myself singing for hours, mesmerized by how the lights danced with my voice.  

![Demo_Visualiser](DemoVisualiser.gif)

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
 
