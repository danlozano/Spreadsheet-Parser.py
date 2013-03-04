"""
Daniel Lozano Valdes
11/1/2012 
"""

# Import XML parsing library.
import xml.etree.ElementTree as ET

# Import module for renaming files.
from os import rename

# Global Variable: "Address Book" List
addressBook = [] 

# Class for representing an entry in the address book.
class Entry(object):

	# Constructor method.
 	def __init__(self, firstName, lastName, email, phone, zipCode):
 		self.firstName = firstName
 		self.lastName = lastName
 		self.email = email
 		self.phone = phone
 		self.zipCode = zipCode

 	# Entry objects have a 'Less Than' method so that the Sort method knows how to sort them.
 	def __lt__(self, other):
 		return self.lastName < other.lastName 			# They will be sorted by last name.

 	# The string method is here so that each entry can be written to file in the correct .csv format.
 	def __str__(self):
 		return (self.lastName + '|' + self.firstName + '|' + self.email + '|' + self.phone + '|' + self.zipCode).rstrip('\n')

# Function for parsing the XML file using the ElementTree XML parsing module.
def parseXml():

	tree = ET.parse('names.xml')		# Build a tree out of the XML file.
	root = tree.getroot()		# Get the root of the XML tree.
	for record in root:			# Go through every record(child) in the XML tree.
		for attribute in record:
			if attribute.tag == 'First_Name':
				firstName = attribute.text
			elif attribute.tag == 'Last_Name':
				lastName = attribute.text
			elif attribute.tag == 'email':
				email = attribute.text
			elif attribute.tag == 'phone':
				phone = attribute.text
			elif attribute.tag == 'zip_code':
				zipCode = attribute.text
		entry = Entry(firstName, lastName, email, phone, zipCode)		# Create an entry object.
		addressBook.append(entry)		# Add it to the address book.

# Function for parsing the CSV file.
def parseCsv():

	f = open('names.csv','r')		# Open the CSV file.
	f.readline()		# Discard first line.
	for record in f:		# Go through each line.
		attributes = record.split('|')		# Split each line using the | as delimeter.
		if len(attributes) != 5: continue		# In case there is an empty or incorrect line, skip it.
		entry = Entry(attributes[0],attributes[1],attributes[2],attributes[3],attributes[4])		# Create an entry object.
		addressBook.append(entry)		# Add it to the address book.
	f.close()

# Function for parsing the txt file.
def parseTxt():

	f = open('names.txt','r')
	f.readline()
	for record in f:
		attributes = record.split()			# Function is same as previous function, except we split each line with any whitespace.
		if len(attributes) != 5: continue
		entry = Entry(attributes[0],attributes[1],attributes[2],attributes[3],attributes[4])
		addressBook.append(entry)
	f.close()
	

# Function for creating the output file in a .csv file format.
def output():

	f = open('output.csv','w')
	f.write('Last Name|First Name|E-Mail|Phone|Zip Code')
	f.write('\n')
	for entry in addressBook:		# Add each entry in the address book to the file.
		f.write(str(entry))
		f.write('\n')
	f.close()


# Function for renaming the files into an appropiate name with correct extension.
def renameFiles():
	rename('names_in_csv.txt','names.csv')
	rename('names_in_xml.txt','names.xml')
	rename('names_in_text.txt','names.txt')


# Main Method
if __name__ == '__main__':

	renameFiles()

	parseXml()
	parseCsv()
	parseTxt()

	addressBook.sort()		# Sorts the address book.

	output()

