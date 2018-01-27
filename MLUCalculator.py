#MLU Calculation Code
#Dylan Cassady
#University of Colorado Boulder
#Spring 2018

import re;


T = "Text. Goes. Here."


def separate(txt):
	wStart = 0
	wEnd = 0
	wordArray = []
	for letter in txt:
		if letter == "," and txt[wStart:(wEnd)] != "":
			wordArray.append(txt[wStart:(wEnd)])
			wStart = wEnd + 2		
		elif letter == " " and txt[wStart:(wEnd)] != "":
			wordArray.append(txt[wStart:(wEnd)])
			wStart = wEnd + 1
		elif letter == "." and txt[wStart:(wEnd)] != "":
			wordArray.append(txt[wStart:(wEnd)])
			wStart = wEnd + 2
		wEnd = wEnd + 1
	if wStart != wEnd and txt[wStart:(wEnd)] != "":
		wordArray.append(txt[wStart:(wEnd)])
	print "Word Count:"
	print len(wordArray)
	return wordArray

def sentenceCount(txt,wordArray):
	count = 0
	ii = 0
	for letter in txt:
		if letter == ".":
			count = count + 1
		ii = ii + 1
	print ""
	print "Sentence Count:"
	print count
	return count

def prefixMorpheme(txt):
	match = re.search('^un', txt)
	if match:
		return 1
	else:
		return 0
	
def suffixMorpheme(txt):
	match1 = re.search("s$", txt)
	match2 = re.search("ed$", txt)
	match3 = re.search("ing$", txt)
	if match1:
		return 1
	elif match2:
		return 1
	elif match3:
		return 1
	else:
		return 0

def MLUCalculator(txt):
	txt = txt.lower()
	txtArray = separate(txt)
	sCount = sentenceCount(txt,txtArray)
	morphCount = len(txtArray);
	for word in txtArray:
		morphCount = morphCount + prefixMorpheme(word)
	for word2 in txtArray:
		morphCount = morphCount + suffixMorpheme(word2)
	print ""
	print "MorphCount:"
	print morphCount
	print ""
	MLU = float(morphCount)/float(sCount)
	return MLU

MLU = MLUCalculator(T)
print "MLU:"
print MLU


