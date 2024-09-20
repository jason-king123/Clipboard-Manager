# Clipboard Manager

**Read this in other languages: [中文](readme_zh.md).**

## Overview

The Clipboard Manager is a lightweight clipboard management tool 📋 designed to help you keep track of and manage your clipboard history. With its user-friendly graphical user interface, you can easily view and paste from your clipboard history. All your clipboard items are persistently stored, ensuring that your history is intact even after restarting the application. 🗂️

## Features

- **Clipboard History**: Automatically records text from your clipboard.
- **Real-time Updates**: Monitors clipboard changes and updates the list in real-time.
- **Persistent Storage**: Saves clipboard history to a local JSON file.
- **Quick Access**: Double-click on an item in the list to copy it back to the clipboard.
- **Clear History**: One-click to clear all clipboard history.
- **User-friendly Interface**: A clean and easy-to-use graphical interface.

## Usage

1. Run `ClipboardManager.py` to start the application.
2. Copy any text to your clipboard, and the application will automatically record it.
3. View and manage your clipboard history in the application window.
4. Double-click on an item in the list to copy it to the clipboard.
5. Click the "Clear" button to clear the history.

## Packaging into EXE

To package this script into an executable file, you can use `pyinstaller`. Here are the steps:

1. First, ensure you have `pyinstaller` installed. If not, you can install it by running:

   ```bash
   pip install pyinstaller
   ```

2. Open a command line or terminal in the project directory.

3. Run the following command to package the script:

   ```bash
   pyinstaller --onefile --add-data "clipboard_data.json;." --add-data "sad.ico;." ClipboardManager.py
   ```

   This command creates a single executable file and includes the `clipboard_data.json` and `sad.ico` files.

4. The executable will be located in the `dist` directory, which you can distribute to other users.

## Notes

- Currently, this script only handles text content and does not support images or other non-text clipboard content. 🖼️
- Ensure you have the necessary permissions to access the clipboard and file system when running the program.

## Future Improvements

- Add support for images and other media types in clipboard content.
- Enhance the user interface to provide more features and a better user experience.

---

Hope this clipboard management tool boosts your productivity! 🚀 If you have any questions or suggestions, feel free to reach out.
