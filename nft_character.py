# code from https://betterprogramming.pub/create-your-own-nft-collection-with-python-82af40abf99f
from PIL import Image
import random
import json
import os

face = ["White", "Black"]
face_weights = [60, 40]

ears = ["No Earring", "Left Earring", "Right Earring", "Two Earrings"]
ears_weights = [25, 30, 44, 1]

eyes = ["Regular", "Small", "Rayban", "Hipster", "Focused"]
eyes_weights = [70, 10, 5 , 1 , 14]

hair = ['ach1', 'ach2', 'ach3', 'ach4', 'ach5', 'ach6', 'ach7',
 'ach8',
 'ach9',
 'ach10',
 'ach11',
 'ach12']

mouth = ['Black Lipstick', 'Red Lipstick', 'Big Smile', 'Smile', 'Teeth Smile', 'Purple Lipstick']
mouth_weights = [10, 10,50, 10,15, 5]

nose = ['Nose', 'Nose Ring']
nose_weights = [90, 10]

face_files = {
    "White": "face1",
    "Black": "face2"
}

ears_files = {
    "No Earring": "ears1",
    "Left Earring": "ears2",
    "Right Earring": "ears3",
    "Two Earrings": "ears4"
}

eyes_files = {
    "Regular": "eyes1",
    "Small": "eyes2",
    "Rayban": "eyes3",
    "Hipster": "eyes4",
    "Focused": "eyes5"
}

hair_files = {
    "ach1": "hair1",
    "ach2": "hair2",
    "ach3": "hair3",
    "ach4": "hair4",
    "ach5": "hair5",
    "ach6": "hair6",
    "ach7": "hair7",
    "ach8": "hair8",
    "ach9": "hair9",
    "ach10": "hair10",
    "ach11": "hair11",
    "ach12": "hair12"
}


mouth_files = {
    "Black Lipstick": "m1",
    "Red Lipstick": "m2",
    "Big Smile": "m3",
    "Smile": "m4",
    "Teeth Smile": "m5",
    "Purple Lipstick": "m6"
}

nose_files = {
    "Nose": "n1",
    "Nose Ring": "n2"
}

TOTAL_IMAGES = 1# Number of random unique images we want to generate


# A recursive function to generate unique image combinations
def create_new_image(ach: str):
    im1 = Image.open(f'face_parts/face/{face_files[random.choices(face, face_weights)[0]]}').convert('RGBA')
    im2 = Image.open(f'face_parts/eyes/{eyes_files[random.choices(eyes, eyes_weights)[0]]}.png').convert('RGBA')
    im3 = Image.open(f'face_parts/ears/{ears_files[random.choices(ears, ears_weights)[0]]}.png').convert('RGBA')
    im4 = Image.open(f'face_parts/hair/{hair_files[ach]}.png').convert('RGBA')
    im5 = Image.open(f'face_parts/mouth/{mouth_files[random.choices(mouth, mouth_weights)[0]]}.png').convert('RGBA')
    im6 = Image.open(f'face_parts/nose/{nose_files[random.choices(nose, nose_weights)[0]]}.png').convert('RGBA')

    #Create each composite
    com1 = Image.alpha_composite(im1, im2)
    com2 = Image.alpha_composite(com1, im3)
    com3 = Image.alpha_composite(com2, im4)
    com4 = Image.alpha_composite(com3, im5)
    com5 = Image.alpha_composite(com4, im6)

    #Convert to RGB
    rgb_im = com5.convert('RGB')
    # file_name = str(item["tokenId"]) + ".png"
    # rgb_im.save("./images/" + file_name)
    return rgb_im