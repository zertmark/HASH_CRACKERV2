#!/bin/python3
from hashlib import *
#from enum import Enum
#TO-DO Add enum
banner="""                  ▄▄  ▄▄▄▄▄▄▄▄                                ▄▄        ▄▄
       ██        ██   ▀▀▀▀▀███                        ██       █▄        █▄
      ██        ██        ██▀    ▄████▄    ██▄████  ███████     █▄        █▄
     ██        ██       ▄██▀    ██▄▄▄▄██   ██▀        ██         █▄        █▄
    ▄█▀       ▄█▀      ▄██      ██▀▀▀▀▀▀   ██         ██          █▄        █
   ▄█▀       ▄█▀      ███▄▄▄▄▄  ▀██▄▄▄▄█   ██         ██▄▄▄        █▄        █▄
  ▄█▀       ▄█▀       ▀▀▀▀▀▀▀▀    ▀▀▀▀▀    ▀▀          ▀▀▀▀         █▄        █▄
                                Hash Cracker
"""
class CrackEncryption():

  def __init__(self, encryption_type, hash, wordlist):
      import time
      self.type=encryption_type
      self.hash=hash.strip()
      self.wordlist=wordlist.strip()
      self.lines=self.get_lines()
      self.list={
      "md5":self.get_md5,
      "sha512":self.get_sha512,
      "sha384":self.get_sha384,
      "sha256":self.get_sha256,
      "sha224":self.get_sha224,
      "sha1":self.get_sha1
      }
      self.start_time=time.time()
      
  def get_md5(self, passwd: str) -> str:
    return md5(passwd.strip().encode()).hexdigest()

  def get_sha512(self, passwd: str) -> str:
    return sha512(passwd.strip().encode()).hexdigest()

  def get_sha256(self, passwd: str) -> str:
    return sha256(passwd.strip().encode()).hexdigest()

  def get_sha384(self, passwd: str) -> str:
    return sha384(passwd.strip().encode()).hexdigest()

  def get_sha224(self, passwd: str) -> str:
    return sha224(passwd.strip().encode()).hexdigest()

  def get_sha1(self, passwd: str) -> str:
    return sha1(passwd.strip().encode()).hexdigest()

  def crack_password(self):
    print("Cracking, please wait...")
    import os
    with open(self.wordlist,'r',errors='ignore') as file:
      for password in file.readlines():
        if self.list[self.type](password) == self.hash:
          print("\nPassword:{}\nTime:{}".format(password.strip(),self.get_time()))
          exit()
        else:
          pass
      print ("\nPassword wasn't found!\nTime:{}".format(self.get_time()))
      exit()

  def get_time(self) -> str:
   import time
   result=time.time()
   output=result-self.start_time
   return str(output)

  def get_lines(self, chunk_size=1<<13) -> int:
    with open(self.wordlist, errors='ignore') as file:
        return sum(chunk.count('\n')
                   for chunk in iter(lambda: file.read(chunk_size), ''))

class Parser():
  def __init__(self):
     import argparse
     print(banner)
     self.parser = argparse.ArgumentParser(description="Hash Cracker")
     self.parser.add_argument("hash", help="Type of hash:md5,sha256,sha1,sha224,sha384,sha512")
     self.parser.add_argument("--file",'-f', help="File with hash")
     self.parser.add_argument("--wordlist",'-w', help="Wordlist file")
     self.args = self.parser.parse_args()
     self.hash_type=self.args.hash
     self.path_to_hash=self.args.file
     self.wordlist=self.args.wordlist

  def read_hash(self):
    import os 
    with open(self.path_to_hash,'r') as file:
      self.hash=file.read()
    if self.hash !="":
      print("Found hash:{}".format(self.hash))
    else:
      print("Error(hash isn't found in {} file). Check file {}(there should be only hash)".format(self.path_to_hash))
      exit()
      
if __name__=="__main__":
 parser=Parser()
 parser.read_hash()
 cracker=CrackEncryption (parser.hash_type, parser.hash, parser.wordlist)
 cracker.crack_password()

