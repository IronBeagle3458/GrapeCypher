# You do need to install Pillow :pip install Pillow
from PIL import Image
 
# Convert encoding data into 8-bit binary
# form using ASCII value of characters
def genData(data):
 
        # list of binary codes
        # of given data
        newd = []
 
        for i in data:
            newd.append(format(ord(i), '08b'))
        return newd
 
# Pixels are modified according to the
# 8-bit binary data and finally returned
def modPix(pix, data):
 
    datalist = genData(data)
    lendata = len(datalist)
    imdata = iter(pix)
 
    for i in range(lendata):
 
        # Extracting 3 pixels at a time
        pix = [value for value in imdata.__next__()[:3] +
                                imdata.__next__()[:3] +
                                imdata.__next__()[:3]]
 
        # Pixel value should be made
        # odd for 1 and even for 0
        for j in range(0, 8):
            if (datalist[i][j] == '0' and pix[j]% 2 != 0):
                pix[j] -= 1
 
            elif (datalist[i][j] == '1' and pix[j] % 2 == 0):
                if(pix[j] != 0):
                    pix[j] -= 1
                else:
                    pix[j] += 1
                # pix[j] -= 1
 
        # Eighth pixel of every set tells
        # whether to stop ot read further.
        # 0 means keep reading; 1 means thec
        # message is over.
        if (i == lendata - 1):
            if (pix[-1] % 2 == 0):
                if(pix[-1] != 0):
                    pix[-1] -= 1
                else:
                    pix[-1] += 1
 
        else:
            if (pix[-1] % 2 != 0):
                pix[-1] -= 1
 
        pix = tuple(pix)
        yield pix[0:3]
        yield pix[3:6]
        yield pix[6:9]
 
def encode_enc(newimg, data):
    w = newimg.size[0]
    (x, y) = (0, 0)
 
    for pixel in modPix(newimg.getdata(), data):
 
        # Putting modified pixels in the new image
        newimg.putpixel((x, y), pixel)
        if (x == w - 1):
            x = 0
            y += 1
        else:
            x += 1
 
# Encode data into image
def encode(data):
    img = 'New_Vineyard\Grape.png'
    image = Image.open(img, 'r')

    if (len(data) == 0):
        raise ValueError('Data is empty')
 
    newimg = image.copy()
    encode_enc(newimg, data)
 
    new_img_name = 'New_Vineyard\Out\grape_vine.png'
    newimg.save(new_img_name, str(new_img_name.split(".")[1].upper()))
 
# Decode the data in the image
def decode():
    img = 'New_Vineyard\In\grape_vine.png'
    image = Image.open(img, 'r')
 
    data = ''
    imgdata = iter(image.getdata())
 
    while (True):
        pixels = [value for value in imgdata.__next__()[:3] +
                                imgdata.__next__()[:3] +
                                imgdata.__next__()[:3]]
 
        # string of binary data
        binstr = ''
 
        for i in pixels[:8]:
            if (i % 2 == 0):
                binstr += '0'
            else:
                binstr += '1'
 
        data += chr(int(binstr, 2))
        if (pixels[-1] % 2 != 0):
            return data

#         1    2    3    4    5    6    7    8    9   10   11   12   13   14   15   16   17   18   19   20   21   22   23   24   25   26   27   28   29   30   31   32   33   34   35   36   37   38   39   40   41   42   43   44   45   46   47   48   49   50   51   52   53   54   55   56   57   58   59   60   61   62   63   64   65   66   67   68   69   70   71   72   73   74   75   76   77   78   79   80   81   82   83   84   85   86   87   88   89   90   91   92   93   94
alpha = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', '[', ']', ';', "'", ',', '.', '/', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '{', '}', '|', ':', '"', '<', '>', '?']

def progress(name, num_current, num_total, prev):
    percent = num_current / num_total
    percent *= 100
    percent = round(percent)

    if percent > prev:
        print(name + ' : ' + str(percent) + '%')
        return percent
    else:
        return prev

def alph_to_num(alph):
    for index in range(len(alpha)):
        if (alph == alpha[index]):
            return index + 1
    
    return -1

def num_to_alph(num):
    return alpha[num - 1]

def string_reverse(string):
    new_string = ''
    prev = 0
    for index in range(len(string)):
        prev = progress('Reversing' ,index, len(string), prev)
        new_string = string[index] + new_string

    return new_string

def letter_stretcher(string):
    new_string = ''
    prev = 0
    for index in range(len(string)):
        prev = progress('Stretching', index, len(string), prev)
        mult = alph_to_num(string[index])
        stretched_char = string[index] * mult
        new_string += stretched_char

    return new_string

def za_hando(string):
    new_string = ''
    index = 0
    prev = 0
    while index in range(len(string)):
        prev = progress('Za Hando', index, len(string), prev)
        mult = alph_to_num(string[index])
        new_string += string[index]
        index += mult

    return new_string

def isEven(num):
    if num % 2 == 0:
        return True
    else:
        return False

def encrypt(string, key):
    cypher_stage_1 = letter_stretcher(string)

    cypher_stage_2 = ''
    key_index = 0
    prev = 0
    for index in range(len(cypher_stage_1)):
        prev = progress('Encrypting', index, len(cypher_stage_1), prev)
        new_pos = 0
        if isEven(index):
            new_pos = alph_to_num(cypher_stage_1[index]) + key[key_index]
        else :
            new_pos = alph_to_num(cypher_stage_1[index]) - key[key_index]
        
        if new_pos >= len(alpha):
            new_pos -= len(alpha)
        elif new_pos < 0:
            new_pos += len(alpha)

        key_index += 1
        if key_index >= len(key):
            key_index -= len(key)

        cypher_stage_2 += num_to_alph(new_pos)

    return string_reverse(cypher_stage_2)

def decrypt(string, key):
    cypher_stage_1 = string_reverse(string)

    cypher_stage_2 = ''
    key_index = 0
    prev = 0
    for index in range(len(cypher_stage_1)):
        prev = progress('Decrypting', index, len(cypher_stage_1), prev)
        new_pos = 0
        if isEven(index):
            new_pos = alph_to_num(cypher_stage_1[index]) - key[key_index]
        else :
            new_pos = alph_to_num(cypher_stage_1[index]) + key[key_index]
        
        if new_pos >= len(alpha):
            new_pos -= len(alpha)
        elif new_pos < 0:
            new_pos += len(alpha)

        key_index += 1
        if key_index >= len(key):
            key_index -= len(key)

        cypher_stage_2 += num_to_alph(new_pos)
    
    return za_hando(cypher_stage_2)

def key_proccess(key):
    new_key = []
    prev = 0
    for index in range(len(key)):
        prev = progress('Proccessing Key', index, len(key), prev)
        new_key.append(alph_to_num(key[index]))

    return new_key

def file_in():
    outtext = ''

    with open('New_Vineyard\In\grape_vine.txt', 'r') as reader:
        line = reader.readline()
        while line != '':
            outtext += line
            outtext += '|'
            line = reader.readline()

        reader.close()

        return outtext

def file_out(text):
    out = open('New_Vineyard\Out\grape_vine.txt', 'w+')
    prev = 0

    for index in range(len(text)):
        prev = progress('Outputing', index, len(text), prev)
        out.write(text[index] + '\n')

    out.close

def text_cleanup(text):
    outtext = []
    index = 0
    size_text = text
    prev = 0

    while size_text.find('|') > -1:
        prev = progress('Cleaning', index, len(text), prev)
        outtext.append(size_text[0:size_text.find('|')])
        index = size_text.find('|') + 1
        size_text = size_text[index:]
    prev = 0

    for pos in range(len(outtext)):
        prev = progress('Clearing', index, len(text), prev)
        outtext[pos].replace('|', ' ')

    return outtext


def main():
    print('')
    print('')
    print('')
    print('Grape Cypher')
    print('Encrypting of Decrypting (e or d)')
    select = input(" : ")
    print('Key')
    key = key_proccess(input(' : '))

    if select == 'e' or select == 'E':
        in_text = file_in()
        cypher_text = []
        encode(encrypt(in_text, key))
        file_out(cypher_text)
    elif select == 'd' or select == 'D':
        in_text = decode()
        cypher_text = text_cleanup(decrypt(in_text, key))
        file_out(cypher_text)

    print('Done')

def debug():
    print(file_in())
    print(encrypt(file_in(), [2, 3, 4, 5]))
    print('done')

if __name__ == "__main__":
    debug()