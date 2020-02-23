from PIL import Image
import glob
import os
charSets = ["$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "," .:-=+*#%@","█▓▒░ "]
def main():
    imageDetails = imageSelect()
    textFileName = imageDetails[1]+".txt"
    img = Image.open(imageDetails[0])
    img = img.convert(mode="L")
    img = adjustImageSize(img)
    file = open(textFileName, "w")
    charSet = setCharSet()
    ascciImage(img,file,charSet)
    file.close()
def setCharSet(retry = False):
    if(retry): print("Error Please Enter valid input for character set eg (1-"+str(len(charSets))+")")
    else:
        for index,charSet in enumerate(charSets):
            print(str(index+1)+") "+charSet)
    charIndex = input("select Input:\t")
    if(not(charIndex.isnumeric())):return setCharSet(True)
    if(int(charIndex)==0):return setCharSet(True)
    if(int(charIndex)>len(charSets)):return setCharSet(True)
    return charSets[int(charIndex)-1]
def imageSelect():
    images = glob.glob('*.png')
    for index,image in enumerate(images):
        print(str(index+1)+") "+image)
    imageIndex=int(input("Select image:\t"))-1
    out = [images[imageIndex],images[imageIndex][:-4]]
    return out
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
    "Select outPut Width Size"+
    "\n1) Console Width\t"+str(consoleSize)+
    "\n2) Image Width\t"+str(imageSize)+
    "\n3) Custome Width\nOption:\t"))
    if op == str(1):return consoleSize
    if op == str(2):return imageSize
    if op == str(3):
        out = input("Size:\t")
        while(not(out.isnumeric())):
            out = input("please enter a valid Integer\nSize:\t")
        return int(out)
    return setSize(img)
def ascciImage(img, file, charList):
    charSet = charList
    line = ""
    out=""
    printToConsole=input("Print to Console (y/n)")
    for y in range(0,img.size[1],2):
        for x in range(0,img.size[0]-1):
            line+= charSet [int(img.getpixel((x,y))/(256/len(charSet))-1)]
        if(printToConsole=="y"): print(line)
        out+="\n"+line
        line=""
    file.write(out)
main()
