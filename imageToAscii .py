from PIL import Image
import glob
import os
charSets = ["$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "," .:-=+*#%@","█▓▒░ "]
def main():
    imageDetails = imageSelect()
    im = Image.open(imageDetails[0]).convert(mode="L")
    im = adjustImageSize(im)
    f = open(imageDetails[1]+".txt", "w")
    ascciImage(im,f,setCharSet())
def setCharSet():
    for index,charSet in enumerate(charSets):
        print(str(index+1)+") "+charSet)
    charIndex = int(input("select Input:\t"))+1
    return charIndex
def imageSelect():
    images = glob.glob('./*.png')
    for index,image in enumerate(images):
        print(str(index+1)+") "+image[2:])
    imageIndex=int(input("Select image:\t"))+1
    return [images[imageIndex],images[imageIndex][2:-4]]
def adjustImageSize(img):
    basewidth = setSize(img)
    wpercent = (basewidth/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    img = img.resize((basewidth,hsize))
    return img
def setSize(img):
    consoleSize = int(os.popen('stty size', 'r').read().split()[1])
    imageSize = img.size[1]
    op = str(input(
    "Select outPut Width Size\n
    1) Console Width\t"+str(consoleSize)+"\n
    2) Image Width\t"+str(imageSize)+"\n
    3) Custome Width\nOption:\t"))
    if op == str(1):return consoleSize
    if op == str(2):return imageSize
    if op == str(3):return input("Size:\t")
    return setSize(img)
def ascciImage(img, file, charList):
    charSet = charSets[charList]
    line = ""
    out=""
    printToConsole=input("Print to Console (y/n)")
    for y in range(0,img.size[1],2):
        for x in range(0,img.size[0]-1):
            line+= charSet [int(img.getpixel((x,y))/(256/len(charSet))-1)]
        if(printToConsole=="y")print(line)
        out+="\n"+line
        line=""
    file.write(out)
    file.close()
main()
