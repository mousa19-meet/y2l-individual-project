import requests ,json
from correction import correction


def correcter(txt):
	txt = txt.split()
	string =""
	for i in range(len(txt)):
		response = requests.get('https://api.datamuse.com/words?sp='+correction(txt[i]))
		parsed_content = json.loads(response.content)
		if len(parsed_content) != 0:
			words = parsed_content[0]
			dictionary = list(words.values())
			the_wanted = dictionary[1]
			string += str(the_wanted) + " "
	return string

