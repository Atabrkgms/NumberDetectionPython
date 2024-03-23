import cv2
import pytesseract

# Görüntüyü yükle
image = cv2.imread("/home/ubuntu/Desktop/test.png")

# Gri tonlamaya dönüştür
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# OCR işlemi
custom_config = r'--oem 3 --psm 6'  # Tesseract OCR için özel yapılandırma
text = pytesseract.image_to_string(gray_image, config=custom_config)

# Metni yazdır
print("Sayılar:", text)
