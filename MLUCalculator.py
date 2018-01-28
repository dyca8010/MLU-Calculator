#MLU Calculation Code
#Dylan Cassady
#University of Colorado Boulder
#Fall 2017

import re;


T = "Bacon ipsum's dolor amet pork bresaola hamburger, ham hock biltong drumstick andouille kielbasa sausage beef ribs chicken tenderloin. Ball tip pork jowl prosciutto t-bone, bresaola andouille tenderloin beef shank tail leberkas. Shoulder porchetta picanha, turducken bacon spare ribs beef ribs leberkas frankfurter flank short loin salami. Ribeye kevin beef ribs corned beef shankle shoulder shank burgdoggen pork loin. Cow leberkas beef ribs tenderloin. Landjaeger shank kevin, doner prosciutto kielbasa pancetta."


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
		elif letter == "!" or letter == "?" and txt[wStart:(wEnd)] != "":
			wordArray.append(txt[wStart:(wEnd)])
			wStart = wEnd + 2	
			
		wEnd = wEnd + 1
	if wStart != wEnd and txt[wStart:(wEnd)] != "":
		wordArray.append(txt[wStart:(wEnd)])
	print wordArray
	print ""
	print "Word Count:"
	print len(wordArray)
	return wordArray

def sentenceCount(txt,wordArray):
	count = 0
	ii = 0
	for letter in txt:
		if letter == "." or letter == "?" or letter == "!":
			count = count + 1
		ii = ii + 1
	print ""
	print "Sentence Count:"
	print count
	return count

def prefixMorpheme(txt):
	pref1 = re.search('^un', txt)
	pref2 = re.search('^dis',txt)
	if pref1 or pref2:
		return 1
	else:
		return 0
	
def suffixMorpheme(txt):
	suf1 = re.search("s$", txt)
	suf2 = re.search("ed$", txt)
	suf3 = re.search("ing$", txt)
	if suf1 or suf2 or suf3:
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
	if sCount != 0:
		MLU = float(morphCount)/float(sCount)
	else:
		MLU = "undefined"
		print "Please end all uterances with appropriate puctuation."
	return MLU

MLU = MLUCalculator(T)
print "MLU:"
print MLU

