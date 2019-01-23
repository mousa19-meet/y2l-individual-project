import requests ,json
from correction import correction

def api(txt):
	txt = txt.split()
	correct_words = []
	string =""
	for i in range(len(txt)):
		response = requests.get('https://api.datamuse.com/words?sp='+correction(txt[i]))
		parsed_content = json.loads(response.content)
		if len(parsed_content) != 0:
			words = parsed_content[0]
			dictionary = words.values()
			the_wanted = dictionary[1]
			string += str(the_wanted) + " "
	return string
