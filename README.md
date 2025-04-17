# Face‑ESP32 Connector

A robust, Python‑powered face‑recognition bridge that links your webcam to an ESP32 (or any serial‑compatible microcontroller). On detecting a known face, it instantly triggers hardware actions—LEDs, buzzers, relays, or your own custom scripts—over a serial interface. Perfect for DIY security locks, attendance systems, personalised smart‑home greetings, and beyond.

---

## 🔍 Key Features

- **Real‑time face detection & recognition**: Utilises OpenCV for rapid frame capture and `face_recognition` (dlib‑powered) for high‑accuracy encoding & matching.
- **Serial‑based control**: Communicates via `pySerial` to your ESP32, Arduino, or any COM‑port device; send simple byte commands.
- **Configurable performance**: Skip N frames between recognition passes to balance CPU load and responsiveness.
- **Infinite scalability**: Add unlimited labeled face images—just drop new files in the `dataset/` folder.
- **Easy customisation**: Modify the serial command logic or extend to network notifications, database logging, cloud APIs, etc.

---

## 🛠️ Tech Stack

| Component              | Purpose                                          |
| ---------------------- | ------------------------------------------------ |
| **Python 3.8+**        | Core scripting, cross‑platform compatibility     |
| **OpenCV**             | Camera capture, image preprocessing, annotations |
| **face_recognition**   | High‑level API wrapping dlib’s face models       |
| **pySerial**           | USB‑serial communication                         |
| **ESP32 / Arduino**    | Microcontroller target for hardware actuation    |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or above
- pip (Python package manager)
- A USB‑serial compatible microcontroller (ESP32, Arduino)
- A working webcam or camera module

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/face-esp32-connector.git
   cd face-esp32-connector
   ```

2. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Prepare your `dataset/`**
   - Create a folder named `dataset/` in the project root.
   - Add labelled images: e.g., `alice.jpg`, `bob.png`, etc.

4. **Configure serial port**
   - Open `main.py` (or `app.py`) and set the correct port:
     ```python
     ser = serial.Serial('COM3', 115200, timeout=1)
     # or '/dev/ttyUSB0' on Linux/macOS
     ```

5. **Flash your ESP32**
   - Upload a simple sketch to toggle GPIO on receiving serial bytes `b'1'` and `b'0'`.


> Crafted with ❤️ for face‑driven automation. Feel free to drop issues, suggestions, or ⭐ the project if you find it useful!

