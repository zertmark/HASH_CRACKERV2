# HASH_CRACKERV2
Better version of HASH_CRACKER
# INSTALL:                 
git clone https://github.com/zertmark/HASH_CRACKERV2.git && cd HASH_CRACKERV2 && chmod +x install.sh && ./install.sh                        
# RUN:                      
usage: hash_cracker.py [-h] [--file FILE] [--wordlist WORDLIST] hash

Hash Cracker

positional arguments:
  hash                  Type of hash:md5,sha256,sha1,sha224,sha384,sha512

optional arguments:
  -h, --help            show this help message and exit                      
  --file FILE, -f FILE  File with hash                              
  --wordlist WORDLIST, -w WORDLIST                                          
                        Wordlist file
