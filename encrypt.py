from PIL import Image, ImageShow

IMAGE_PATH = "source_images/nature.png"
PADDING_START = ""
PADDING_END = ""
INTENSITY_MIN = 200 #minimum intensity of RGB pixel to be selected for LSB encoding
INTENSITY_MAX = 230 #maximum intensity of RGB pixel to be selected for LSB encoding



def main():
    #attempt opening image file
    try:
        imageFile = Image.open(IMAGE_PATH)
        #get image format here
        imageFormat = imageFile.format

        #note : PNG file format uses RGBA, which adds extra complexity 
        #we want to stick to using strictly RGB
        if imageFormat == "PNG":
            imageFile = imageFile.convert("RGB")
            print("\nOnly RGB channels will be used for PNG file format.")
        
        #opens up Preview and displays the image
        #imageFile.show()

        imageWidth = imageFile.width
        imageHeight = imageFile.height

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

        #convert the list above into a string
        userMessageEncodedString = ""
        for i in range(0, len(userMessageEncoded)):
            userMessageEncodedString += userMessageEncoded[i]

        userMessageLength = len(userMessageEncodedString)

        #load RGB image in binary
        pixelBytes = bytearray(imageFile.tobytes())

        count = 0

        for index in range(0, len(pixelBytes)):

            if count == userMessageLength:
                    break

            elif count < userMessageLength:

                if pixelBytes[index] <= INTENSITY_MAX and pixelBytes[index] >= INTENSITY_MIN:

                    currentPixelByte = pixelBytes[index]
                    inBinary = format(currentPixelByte, '08b')

                    old = inBinary

                    #change the LSB of pixel data with that of message
                    inBinary = inBinary[:-1] + str(userMessageEncodedString[count])

                    #place modified pixel byte back into image
                    pixelBytes[index] = int(inBinary, 2)

                    count += 1

                if index == len(pixelBytes) - 1 and count < userMessageLength:
                    print(f'Not enough pixels in the specified intensity thresholds for encoding!')
                    break



        #LSB encoding is done, create new PIL image
        finalImage = Image.frombytes("RGB", (imageWidth, imageHeight), bytes(pixelBytes))
        finalImage.save("encoded_image.png")
        
        print(f'Final image saved as encoded_image.png!')



        
    except Exception as e:
        print(f'Error : {e}')

if __name__ == "__main__":
    main()