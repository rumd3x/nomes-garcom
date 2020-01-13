import cv2
import pytesseract
import numpy as np
import os
import re

# CONFIG
pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'


def rotate_bound(image, angle):
    # grab the dimensions of the image and then determine the
    # center
    (h, w) = image.shape[:2]
    (cX, cY) = (w // 2, h // 2)

    # grab the rotation matrix (applying the negative of the
    # angle to rotate clockwise), then grab the sine and cosine
    # (i.e., the rotation components of the matrix)
    M = cv2.getRotationMatrix2D((cX, cY), -angle, 1.0)
    cos = np.abs(M[0, 0])
    sin = np.abs(M[0, 1])

    # compute the new bounding dimensions of the image
    nW = int((h * sin) + (w * cos))
    nH = int((h * cos) + (w * sin))

    # adjust the rotation matrix to take into account translation
    M[0, 2] += (nW / 2) - cX
    M[1, 2] += (nH / 2) - cY

    # perform the actual rotation and return the image
    return cv2.warpAffine(image, M, (nW, nH))


def extract_text(image):
    # LOAD IMG
    img = cv2.imread(image, cv2.IMREAD_GRAYSCALE)
    cv2.dilate(img, (50, 50), img)

    # APPLY CONSTRAST
    alpha = 1.2  # CONTRAST 1.0 to 3.0
    beta = -100    # BRIGHTNESS 0 to 100

    img = cv2.convertScaleAbs(img, alpha=alpha, beta=beta)

    # ROTATE
    img = rotate_bound(img, 10)
    (h, w) = img.shape[:2]

    # CROP
    img = img[235:310, 0:w]

    # DISPLAY
    # cv2.imshow('Teste', img)
    # cv2.waitKey(0)

    # GATHER TEXT
    text = pytesseract.image_to_string(img, config='--psm 8')

    return re.sub(r'[^A-Z]', '', text)


with open('nomes.txt', "w+") as f:

    images = os.listdir('images/')
    total = len(images)
    current = 0
    for img in images:
        current += 1
        try:
            nome = extract_text("images/{}".format(img))
            if nome.strip() != '':
                print("{} de {}: {}".format(current, total, nome))
                f.write("{}\n".format(nome))
        except:
            print("{} falhou".format(current))
