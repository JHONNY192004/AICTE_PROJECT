# Steganography Project

## Introduction

This project demonstrates **image steganography** using Python and OpenCV. It allows users to **hide a secret message** inside an image and later extract it using the correct passcode.

## Features

- **Encryption:** Hide a message inside an image.
- **Decryption:** Extract the hidden message from the image.
- **Password Protection:** Ensures only authorized users can decode the message.

## Technologies Used

- Python
- OpenCV (cv2)
- VScode
- Windows
  
## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/steganography-project.git
   ```
2. Navigate to the project directory:
   ```bash
   cd steganography-project
   ```
3. Install dependencies:
   ```bash
   pip install opencv-python
   ```

## Usage

### Encryption

1. Run the encryption script:
   ```bash
   python encrypt.py
   ```
2. Enter the path of the image.
3. Input the secret message.
4. Enter a passcode for security.
5. The encrypted image will be saved as `encryptedImage.png`.

### Decryption

1. Run the decryption script:
   ```bash
   python decrypt.py
   ```
2. Enter the path of the encrypted image.
3. Provide the passcode to reveal the hidden message.

## Example

### Encrypting a Message

```
Enter the image path: secret.png
Enter the secret message: Hello, this is hidden!
Enter a passcode: 1234
Message encrypted successfully in encryptedImage.png
```

### Decrypting a Message

```
Enter the encrypted image path: encryptedImage.png
Enter passcode for Decryption: 1234
Decrypted message: Hello, this is hidden!
```

### Contributing

Feel free to fork this repository and submit pull requests for improvements.

