import cv2

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

def decode_message(img):
    """Decode the secret message from the image."""
    c = {i: chr(i) for i in range(255)}
    
    message = ""
    n, m, z = 0, 0, 0
    password = input("Enter passcode for Decryption: ")  # Only ask for the decryption passcode

    while True:
        char_code = img[n, m, z]
        if char_code == 0:  # Stop at the null character
            break
        message += c[char_code]
        m += 1
        if m >= img.shape[1]:  # Move to the next row if we reach the end of the current row
            m = 0
            n += 1
            if n >= img.shape[0]:  # Stop if we exceed the image dimensions
                break
        z = (z + 1) % 3

    print("Decrypted message:", message)

def main():
    image_path = input("Enter the encrypted image path: ")
    img = load_image(image_path)
    if img is not None:
        decode_message(img)

if __name__ == "__main__":
    main()
