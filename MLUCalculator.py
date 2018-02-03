#MLU Calculation Code
#Dylan Cassady
#University of Colorado Boulder
#Fall 2017

import re;

#Text to analyze goes here
T = "Bacon ipsum dolor amet alcatra doner bresaola sirloin ham kevin shankle tenderloin boudin jowl beef ribs jerky spare ribs short ribs. Meatball ham hock pork loin sirloin pancetta turducken. Strip steak pig capicola prosciutto pork chop jowl. Sausage pork buffalo turducken flank, shoulder rump kevin. Shankle ground round shank leberkas, spare ribs kielbasa filet mignon tri-tip alcatra sausage pork doner pork belly chicken. Tri-tip ribeye bresaola filet mignon buffalo turkey, beef ribs short loin ham hock beef cow cupim hamburger tongue. Meatball ham hock ribeye, turkey kielbasa kevin bacon pig pork t-bone beef spare ribs hamburger shankle."

def separate(txt): #break the paragraph into individual words, all lowercase
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
	#print (wordArray)
	#print ()
	print ("Word Count:")
	print (len(wordArray))
	return wordArray

def sentenceCount(txt,wordArray): #count the number of sentences using punctuation
	count = 0
	ii = 0
	for letter in txt:
		if letter == "." or letter == "?" or letter == "!":
			count = count + 1
		ii = ii + 1
	print ()
	print ("Utterance Count:")
	print (count)
	return count

def prefixMorpheme(txt):
	pref2 = re.search('^dis',txt)
	if pref2:
		#print (txt) #prints each word flagged as having a prefix
		return 1
	else:
		return 0

def suffixMorpheme(txt): #looks for words that end in s, ed, or ing
	suf1 = re.search("s$", txt)
	suf2 = re.search("ed$", txt)
	suf3 = re.search("ing$", txt)
	if suf1 or suf2 or suf3:
		if txt == "was" or txt == "is" or txt == "boing" or txt == "this" or txt == "being" or txt == "has" or txt == "oops" or txt == "thing":
			return 0
		else:
			#print (txt) #prints each word flagged as having a suffix
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
	print ()
	print ("MorphCount:")
	print (morphCount)
	print ()
	if sCount != 0:
		MLU = float(morphCount)/float(sCount)
	else:
		MLU = ("undefined")
		print ("Please end all uterances with appropriate puctuation.")
	return MLU

MLU = MLUCalculator(T)
print ("MLU:")
print (MLU)

def wordTypes(txt):
	txt=txt.lower
	txtArray = separate(txt)
