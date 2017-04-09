#!/usr/bin/python


import hashlib,base64
import sys

string=str(sys.argv[1])

#base64.b64decode("")
	
print "MD5 = "+hashlib.md5(string).hexdigest()+" // Size: "+str(hashlib.md5(string).digest_size)
print "MD5_base64 = "+base64.b64encode(hashlib.md5(string).hexdigest())

print "SHA1 = "+hashlib.sha1(string).hexdigest()+" // Size: "+str(hashlib.sha1(string).digest_size)
print "SHA1_base64 = "+base64.b64encode(hashlib.sha1(string).hexdigest())

print "SHA224 = "+hashlib.sha224(string).hexdigest()+" // Size: "+str(hashlib.sha224(string).digest_size)
print "SHA224_base64 = "+base64.b64encode(hashlib.sha224(string).hexdigest())

print "SHA256 = "+hashlib.sha256(string).hexdigest()+" // Size: "+str(hashlib.sha256(string).digest_size)
print "SHA256_base64 = "+base64.b64encode(hashlib.sha256(string).hexdigest())

print "SHA384 = "+hashlib.sha384(string).hexdigest()+" // Size: "+str(hashlib.sha384(string).digest_size)
print "SHA384_base64 = "+base64.b64encode(hashlib.sha384(string).hexdigest())

print "SHA512 = "+hashlib.sha512(string).hexdigest()+" // Size: "+str(hashlib.sha512(string).digest_size)
print "SHA512_base64 = "+base64.b64encode(hashlib.sha512(string).hexdigest())

