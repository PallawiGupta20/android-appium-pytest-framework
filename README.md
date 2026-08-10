# Android Appium Pytest Framework

A Page Object Model (POM) based mobile UI test automation framework built with **Appium**, **Python**, and **pytest**, tested against the Sauce Labs "My Demo App RN" Android application.

## Tech Stack
- Python 3
- Appium (UiAutomator2 driver)
- pytest
- Page Object Model design pattern
- Android emulator (Pixel 6, API 34)

## Project Structure
cat > .github/workflows/appium-ci.yml << 'EOF'
name: Appium Android Tests

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: macos-latest
    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Install Python dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Set up Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'

      - name: Install Appium
        run: |
          npm install -g appium
          appium driver install uiautomator2

      - name: Enable KVM (for Android emulator)
        run: |
          echo 'KERNEL=="kvm", GROUP="kvm", MODE="0666", OPTIONS+="static_node=kvm"' | sudo tee /etc/udev/rules.d/99-kvm4all.rules
          sudo udevadm control --reload-rules
          sudo udevadm trigger --name-match=kvm

      - name: Run tests on Android Emulator
        uses: reactivecircus/android-emulator-runner@v2
        with:
          api-level: 34
          target: google_apis
          arch: x86_64
          script: |
            appium &
            sleep 10
            pytest -v
