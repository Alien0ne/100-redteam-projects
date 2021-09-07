from argparse import ArgumentParser
import enchant

parser = ArgumentParser()
group = parser.add_mutually_exclusive_group()
parser.add_argument("mode", help ="mode", choices=["encode", "decode","brute"])
group.add_argument("-f", metavar="file" , help="filename")
group.add_argument("-t", metavar="text" , help="encode/decode from <")
parser.add_argument("-r", metavar="rotation", help="Roation Number",default=26)
parser.add_argument("-v", help="Word validation",action="store_true")
parser.add_argument("-k", metavar="key" , help ="Key or the Shift Value, Default = 3", default=3)
parser.add_argument("-o", metavar="file" , help="output file",default="output.txt")

args = parser.parse_args()
key = args.k

def encode(plain_text, alphabet):
    print("[+] Plain Text  : ",plain_text)
    cipher_text=""
    for i in plain_text:
        try:
            index=(alphabet.index(i.lower())+int(key))%26
            cipher_text=cipher_text+alphabet[index]
        except:
            cipher_text=cipher_text+i
    print("[+] Cipher Text : ",cipher_text)
    return(cipher_text)
def decode(cipher_text, alphabet):
    print("[+] Cipher Text - ",cipher_text)
    plain_text=""
    for i in cipher_text:
        try:
            index=(alphabet.index(i.lower())-int(key))%26
            plain_text=plain_text+alphabet[index]
        except:
            plain_text=plain_text+i
    print("[+] Plain Text  - ",plain_text)
    return(plain_text)

alphabet="abcdefghijklmnopqrstuvwxyz"
brute=[]

if args.f:
    text = open(args.f, "rt").read()
    if args.mode == "encode":
        output_text = encode(text,alphabet)
        open(args.o,"wt").write(output_text)
        
    elif args.mode == "decode":
        output_text = decode(text,alphabet)
        open(args.o,"wt").write(output_text)
    
else:
    text = args.t
    if args.mode == "encode":
        encode(text,alphabet)
    elif args.mode == "decode":
        decode(text,alphabet)
    elif args.mode == "brute":
        key=0
        for i in range(1,(int(args.r)+1)):
            key=i
            output=decode(text,alphabet)
            brute.append(output)
            output=""
        for i in brute:
            add=str(brute.index(i)+1)+" : "+i+"\n"
            open(args.o,"a").write(add)
        if args.v:
            valid_check = enchant.Dict("en_US")
            for i in brute:
                valid_true=valid_check.check(i)
                if valid_true == True:
                    print("Valid Word : " ,i)