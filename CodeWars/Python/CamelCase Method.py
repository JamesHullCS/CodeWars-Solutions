def camel_case(string):
    
	List = []
	for i in string.split():
		List.append(i.capitalize())
	return ("".join(List))

camel_case("hello world")

def camel_case(string):
    return string.title().replace(" ", "")