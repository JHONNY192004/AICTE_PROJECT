import cv2
import os

def load_image(image_path):
    """Load an image from the specified path."""
    try:
        img = cv2.imread(image_path)
        if img is None:
            raise ValueError("Image not found or unable to load.")
        return img
    except Exception as e:
        print(f"Error loading image: {e}")
        return None

def encode_message(img, msg, password, output_path="encryptedImage.png"):
    """Encode a secret message into the image."""
    d = {chr(i): i for i in range(255)}
    
    m, n, z = 0, 0, 0
    msg += chr(0)  # Append a null character as the end marker
    for char in msg:
        img[n, m, z] = d[char]
        m += 1
        if m >= img.shape[1]:  # Move to the next row if we reach the end of the current row
            m = 0
            n += 1
            if n >= img.shape[0]:  # Stop if we exceed the image dimensions
                raise ValueError("Message is too large for the image.")
        z = (z + 1) % 3  # Cycle through RGB channels

    cv2.imwrite(output_path, img)
    print(f"Message encrypted successfully in {output_path}")
    os.system(f"start {output_path}")  # Open the encrypted image (for Windows)

def main():
    image_path = input("Enter the image path: ")
    img = load_image(image_path)
    if img is not None:
        msg = input("Enter the secret message: ")
        password = input("Enter a passcode: ")
        encode_message(img, msg, password)

if __name__ == "__main__":
    main()
