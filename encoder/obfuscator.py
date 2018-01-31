#!/usr/bin/python

import urllib
import os
import binascii

#Encoder
#Read Coders from file
f=open('encoding_raw.txt','r')
tags={}
excluded=['bz2\n','ibm1026\n','EBCDIC-CP-HE\n','zip\n','zlib\n','IBM037\n','ibm1140\n','IBM424\n','EBCDIC-CP-CH\n','IBM500\n','IBM039\n','EBCDIC-CP-BE\n','UTF-32LE\n','hkscs\n','UTF-16BE\n','uu\n']
s=raw_input("Enter a string: ")

#Encoding Types

for x in f:
	try:
		if not tags.has_key('quote_plus'):
			tags.update({'quote_plus': urllib.quote_plus(s)})

		if not tags.has_key('quote'):
			tags.update({'quote':urllib.quote(s)})

		if not tags.has_key('url'):
			
			hex=binascii.hexlify(s)
			url="%".join(hex[i:i+2] for i in range(-2, len(hex), 2))
			tags.update({'url': url})

		if not tags.has_key('url_hex'):

                        hex=binascii.hexlify(s)
                        url="\\x".join(hex[i:i+2] for i in range(-2, len(hex), 2))
                        tags.update({'url_hex': url})
	 	
		#Use to bypass Javascript filters
		if not tags.has_key('unicode_int'):
			int_table=[]
			#Convert Char to Unicode Int: For A->65
			for o in s:
				int_table.append(ord(o))
			tags.update({'unicode_int': tuple(int_table)})

		#HTML dec A -> &#65;
                if not tags.has_key('unicode_dec'):
                        dec_table=[]
                        #Convert Char to HTML hex : For A-> &#65;
                        for o in s:
                                dec_table.append(ord(o))
                        tags.update({'unicode_dec': tuple(dec_table)})

		#HTML hex A-> &#x41; 
		if not tags.has_key('unicode_hex'):
                        split_StringTable=[]
                        hex_table=[]
                        #Convert Char to HTML hex : For A-> &#x41;
                        for o in s:
                                hex_table.append(binascii.hexlify(o))
                        tags.update({'unicode_hex': tuple(hex_table)})


		if x not in excluded:
			if not tags.has_key(x):
				if x == "hex\n":
					tags.update({x:"0x"+s.encode(encoding=str(x),errors='strict')})
				else:
					tags.update({x:s.encode(encoding=str(x),errors='strict')})
			
		
	except Exception as e: 
			e=1
		
unique_dict={}
#Create New Dictionary with unique keys
#Excluded values from loop
excluded_enc=['unicode_dec']
for item in tags.items():
	x,y=item
	if not unique_dict.has_key(y):
		unique_dict.update({y:x})

#stdout unique values
counter=0
for item2 in unique_dict.items():
	m,n=item2
	if hasattr(n,'strip') and hasattr(m,'strip'):
		print str(counter)+") %s -> %s" % (n.strip('\n'),m.strip('\n'))
	elif n == "unicode_int":
		print str(counter)+") %s -> String.fromCharCode%s  //Bypass Javascript filters" % (n,str(m))
	elif n == "unicode_hex":
		#Add dec values with &#x; to oneline_html_hex
		#Add dec values with &#; to oneline_html_dec
		oneline_html_hex=[]
		oneline_html_dec=[]
		for x in m:
			oneline_html_hex.append("&#x"+str(x)+";")
			oneline_html_dec.append("&#"+str(ord(binascii.unhexlify(x)))+";")
		print str(counter)+") %s -> %s  //Bypass HTML filters" % (n,''.join(oneline_html_hex))
		#Convert hex to dec
		print str(counter)+") unicode_dec -> %s  //Bypass HTML filters" % (''.join(oneline_html_dec))
	counter=counter+1
		


f.close()
