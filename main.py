from PIL import Image, ImageShow

IMAGE_PATH = "source_images/nature.png"


def main():
    #attempt opening image file
    try:
        imageFile = Image.open(IMAGE_PATH)
        
        #opens up Preview and displays the image
        #imageFile.show()

        imageWidth = imageFile.width
        imageHeight = imageFile.height
        imageFormat = imageFile.format

        print(f'\nImage data \nwidth : {imageWidth} pixels \nheight : {imageHeight} pixels \n')
        print(f'File format : {imageFormat}')
        print(f'\nBytes to work with : {int(imageWidth) * int(imageHeight) * 3} bytes.')

        userMessageRaw = input("Enter a message to encode: ")

        #padding to mark beginning of message : $)!
        #padding to mark ending of message : &?+
        userMessageEncoded = []
        paddingStart = "$)!"
        userMessageEncoded = [f"{ord(char):08b}" for char in paddingStart]
        
        #convert the user's message into binary
        for character in userMessageRaw:
            asciiValue = ord(character)
            binaryValue = f"{asciiValue:08b}"
            userMessageEncoded.append(binaryValue)

        paddingEnd = "&?+"
        userMessageEncoded += [f"{ord(char):08b}" for char in paddingEnd]

        print(userMessageEncoded)

        
        

    except Exception as e:
        print(f'Error : {e}')

if __name__ == "__main__":
    main()