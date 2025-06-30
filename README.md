# 🚀 Flutter App Automation with Appium + Pytest (Python)

Automated UI testing of Flutter apps using [Appium Flutter Driver](https://github.com/truongsinh/appium-flutter-driver) and Python's `pytest`.

---

## 📦 Prerequisites

Before you begin, ensure the following are installed:

- [Node.js](https://nodejs.org/) (v16+ recommended)
- [Python 3.8+](https://www.python.org/)
- [Appium 2.x](https://appium.io/)
- [Flutter SDK](https://flutter.dev/docs/get-started/install) (for building `.apk`)
- Android SDK / Emulator or real device

---

## 🔧 Step-by-Step Setup

### 1. Install Appium CLI

```bash
npm install -g appium

appium driver install --source=git https://github.com/truongsinh/appium-flutter-driver.git

appium driver list

pip install Appium-Python-Client pytest

```

## Running Tests

### 1. Start Appium Server

```bash

appium

```

### 2. Build and Install Flutter Monekin App (optional)

```bash

flutter build apk --debug
adb install -r build/app/outputs/flutter-apk/app-debug.apk

```

### 3. Run Tests with Pytest

```bash

pytest -v

```
