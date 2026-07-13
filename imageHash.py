#using hashlib to get the SHA-256 checksum of an image 
#this program compares the checksum of two images to see if they are identical

import hashlib

def getChecksum(filePath):

    try:
        with open(filePath, "rb") as f:
            fileBytes = f.read()
            hash = hashlib.sha256(fileBytes).hexdigest()
            return hash
        
    except Exception as e:
        print(f'Error : {e}.')


def compareImages(filePath1, filePath2):
    checkSum1 = getChecksum(filePath1)
    checkSum2 = getChecksum(filePath2)

    return checkSum1 == checkSum2

#control set-up nature.png and nature copy.png are the same images
print(compareImages("nature.png", "nature copy.png")) #returned True!

print(compareImages("nature.png", "encoded_image.png")) #returns False! 
