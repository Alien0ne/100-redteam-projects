

## What is Ceaser Cipher
A Caesar cipher, also known as Caesar's cipher, the shift cipher, Caesar's code or Caesar shift, is one of the simplest and most widely known encryption techniques. It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet. For example, with a left shift of 3, D would be replaced by A, E would become B, and so on. The method is named after Julius Caesar, who used it in his private correspondence.

<br>
<br>

## Why this tool ?
This tool gives you various options to encrypt, decrypt files or just words only, or brute force the ciphertext in Ceaser Cipher.

<br>
<br>

## Usage:

<br>

```shell
$ python3 script.py ceaser.py [mode] [-f] {input file} [-t] {input word} [-r] [-v] [-k] {key} [-o] {output file name}
```

- `mode` -> Possible Options={encode,decode,brute}
- `encode` -> Encodes a the given input into ceaser cipher based on rest of options.
- `decode` -> Decodes the input from ceaser cipher based on options passed
- `brute` -> Brute force the ciphertext


## Optinal Arguments

- `-f` `Filename` -> when the input is a file, pass this flag

- `-t` `Text` -> when it's just one string you are working on pass that as argument to this flag

##### Note : Text and file flags are complimentary, and either one of them should be passed.

- `-r` `Rotation` -> The input may not always using the standard rotation in cipher, those cases needs this flag, but the default is 26

- `-v` `Validate` -> Every output doesn't need to be a word which you can understand in plain dictonary word of English, use this flag to just give you valid English words

- `-k` `Key` -> The shifts by which the ceaser cipher is done, also madmen may change the shifts which was done in tradition, but the default one is 3

- `-o` `Output` -> When the output of the excution has to be stored in file, this flag comes handy

<br>
<br>

## Installation:


        sudo apt-get -y install python3-pip
        pip3 install argparse
        pip3 install pyenchant
        git clone https://github.com/Alien0ne/100-redteam-projects
        cd 100-redteam-projects/Ciphers/caeser

## Example Usage: 


        caeser.py encode -t <text> -k <Key/Shift value>
        caeser.py encode -f <input_file_name> -k <key/shift value> -o <output_file_name>

        caeser.py decode -t <text> -k <Key/Shift value>
        caeser.py decode -t <input_file_name> -k <key/shift value> -o <output_file_name>

        caeser.py brute -t <text>  
        caeser.py brute -t <text> -v -o <output_file_name>

