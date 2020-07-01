#!/usr/bin/python
# -*- coding: utf-8 -*-
 
########################################################################
################### Sample format for reference ########################
########################################################################
#File Description = Python program App
#File Version = 1.1.1.1000
#Product Name = Python program App
#Product Version = 1,1,1,1000
#Legal Copyright = Copyright © reserved Joel Dcosta Ltd
#Company Name = Fuddy Duddies, Inc. 8 Flossie Dr. Arlington, VA 00001
#Internal Name = Python
#Legal Trademarks = Python is a Trademark of Python program App
#Original Filename = PythonApp.exe
########################################################################

################ Edit this only ########################################
file_description = "Python program TK App"
file_version = "1.1.1.1000"
product_name = "Python program TK App"
product_version = "1,1,1,1000"
copyright_ = "Copyright © reserved Joel Dcosta Ltd"
company_name = "Fuddy Duddies, Inc. 8 Flossie Dr. Arlington, VA 00001"
internal_name = "Python"
legal_trademarks = "Python is a Trademark of Python program App"
original_filename = "PythonApp.exe"
########################################################################
f_version = file_version.replace(".",",")


body = """VSVersionInfo(
   ffi=FixedFileInfo(
	# filevers and prodvers should be always a tuple with four items: (1, 2, 3, 4)
	# Set not needed items to zero 0.
	filevers=(%(f_version)s), 
	prodvers=(%(product_version)s), 
	# Contains a bitmask that specifies the valid bits 'flags' 
	mask=0x3f, 
	# Contains a bitmask that specifies the Boolean attributes of the file. 
	flags=0x0, 
	# The operating system for which this file was designed. 
	# 0x4 - NT and there is no need to change it. 
	OS=0x4, 
	# The general type of file. 
	# 0x1 - the file is an application. 
	fileType=0x1, 
	# The function of the file. 
	# 0x0 - the function is not defined for this fileType 
	subtype=0x0, 
	# Creation date and time stamp. 
	date=(0, 0)
	), 
   kids=[ 
	StringFileInfo( 
		[ 
		StringTable( 
		u'040904b0', 
		[
                StringStruct(u'FileDescription', u'%(file_description)s'),
                StringStruct(u'FileVersion', u'%(f_version)s'),
		StringStruct(u'ProductName', u'%(product_name)s'),
		StringStruct(u'ProductVersion', u'%(product_version)s'),
                StringStruct(u'LegalCopyright', u'%(copyright_)s'),
		StringStruct(u'CompanyName', u'%(company_name)s'), 
		StringStruct(u'InternalName', u'%(internal_name)s'),
		StringStruct(u'LegalTrademarks', u'%(legal_trademarks)s'),
                StringStruct(u'OriginalFilename', u'%(original_filename)s'),
		]) 
	    ]), 
	VarFileInfo([VarStruct(u'Translation', [1033, 1200])]) 
  ]
)
"""

f_version = file_version.replace(".",",")

print(body % {'file_description':file_description,
              'f_version':f_version,
              'product_name':product_name,
              'product_version':product_version,
              'copyright_':copyright_,
              'company_name':company_name,
              'internal_name':internal_name,
              'legal_trademarks':legal_trademarks,
              'original_filename':original_filename})

with open("t_version.txt","w",encoding='utf8') as f:
    f.writelines(body % {'file_description':file_description,
              'f_version':f_version,
              'product_name':product_name,
              'product_version':product_version,
              'copyright_':copyright_,
              'company_name':company_name,
              'internal_name':internal_name,
              'legal_trademarks':legal_trademarks,
              'original_filename':original_filename})

test = """
def writeFile():
    file = open('sh3rly.txt','w')
    file.write(metinF.get() + '\n')
    file.close()

gui = Tk()

metinF = Entry(gui)
metinF.grid(row=9, column=1)

butonWrite = Button(gui)
butonWrite.config(text = 'Write To File', command = writeFile)
butonWrite.grid(row=8, column=1)

gui.mainloop()
"""
