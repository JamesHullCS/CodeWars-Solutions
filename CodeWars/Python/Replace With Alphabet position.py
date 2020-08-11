from string import ascii_lowercase
def alphabet_position(text):
	List = []
	for i in text.lower():
		if i.isalpha():
			List.append(i)
		elif i == " ":
			i.replace(" ","")
		else:
			print("")

	formatedtext = "".join(List)
	print(formatedtext)
	


alphabet_position("Hello World!")