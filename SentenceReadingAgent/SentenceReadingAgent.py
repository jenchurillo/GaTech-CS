class SentenceReadingAgent:
    def __init__(self):
        #If you want to do any initial processing, add it here.
        pass

    def solve(self, sentence, question):
        #Add your code here! Your solve method should receive
		#two strings as input: sentence and question. It should
		#return a string representing the answer to the question.

        
        answer = ""

        partsOfSpeech = [['Serena','name'], ['Andrew','name'], ['Bobbie','name'], ['Cason','name'], ['David','name'], ['Farzana','name'], ['Frank','name'], ['Hannah','name'], ['Ida','name'], ['Irene','name'], ['Jim','name'], ['Jose','name'], ['Keith','name'], ['Laura','name'], ['Lucy','name'], ['Meredith','name'], ['Nick','name'], ['Ada','name'], ['Yeeling','name'], ['Yan','name'], ['the','article'], ['of','preposition'], ['to','preposition'], ['and','conjunction'], ['a','article'], ['in','preposition'], ['is','verb'], ['it','pronoun'], ['you','pronoun'], ['that','preposition'], ['he','pronoun'], ['was','verb'], ['for','preposition'], ['on','preposition'], ['are','verb'], ['with','preposition'], ['as','preposition'], ['I','pronoun'], ['his','pronoun'], ['they','pronoun'], ['be','verb'], ['at','preposition'], ['one','adjective'], ['have','verb'], ['this','determiner'], ['from','preposition'], ['or','conjunction'], ['had','verb'], ['by','preposition'], ['hot','adjective'], ['but','conjunction'], ['some','verb'], ['what','question'], ['there','adverb'], ['we','pronoun'], ['can','verb'], ['out','adverb'], ['other','adjective'], ['were','verb'], ['all','adjective'], ['your','pronoun'], ['when','question'], ['up','preposition'], ['use','verb'], ['word','noun'], ['how','question'], ['said','verb'], ['an','article'], ['each','adjective'], ['she','pronoun'], ['which','question'], ['do','verb'], ['their','determiner'], ['time','noun'], ['if','conjunction'], ['will','verb'], ['way','noun'], ['about','preposition'], ['many','adjective'], ['then','adverb'], ['them','pronoun'], ['would','verb'], ['write','verb'], ['like','adjective'], ['so','adverb'], ['these','pronoun'], ['her','determiner'], ['long','adjective'], ['make','verb'], ['thing','noun'], ['see','verb'], ['him','pronoun'], ['two','adjective'], ['has','verb'], ['look','verb'], ['more','adjective'], ['day','noun'], ['could','verb'], ['go','verb'], ['come','verb'], ['did','verb'], ['my','pronoun'], ['sound','noun'], ['no','adverb'], ['most','adjective'], ['number','noun'], ['who','question'], ['over','preposition'], ['know','verb'], ['water','noun'], ['than','conjunction'], ['call','noun'], ['first','adjective'], ['people','noun'], ['may','adjective'], ['down','adverb'], ['side','noun'], ['been','verb'], ['now','adverb'], ['find','verb'], ['any','adjective'], ['new','adjective'], ['work','verb'], ['part','verb'], ['take','verb'], ['get','verb'], ['place','noun'], ['made','verb'], ['live','verb'], ['where','question'], ['after','preposition'], ['back','noun'], ['little','adjective'], ['only','adverb'], ['round','adjective'], ['man','noun'], ['year','time'], ['came','verb'], ['show','verb'], ['every','adjective'], ['good','adjective'], ['me','pronoun'], ['give','verb'], ['our','pronoun'], ['under','preposition'], ['name','noun'], ['very','adverb'], ['through','preposition'], ['just','adjective'], ['form','noun'], ['much','adjective'], ['great','adjective'], ['think','verb'], ['say','verb'], ['help','verb'], ['low','adjective'], ['line','noun'], ['before','preposition'], ['turn','verb'], ['cause','noun'], ['same','adjective'], ['mean','adjective'], ['differ','verb'], ['move','verb'], ['right','adjective'], ['boy','noun'], ['old','adjective'], ['too','adverb'], ['does','verb'], ['tell','verb'], ['sentence','noun'], ['set','verb'], ['three','adjective'], ['want','verb'],
        ['air','noun'], ['well','adverb'], ['also','adverb'], ['play','noun'], ['small','adjective'], ['end','noun'], ['put','verb'], ['home','noun'], ['read','verb'], ['hand','noun'], ['port','noun'], ['large','adjective'], ['spell','verb'], ['add','verb'], ['even','adjective'], ['land','noun'], ['here','adverb'], ['must','verb'], ['big','adjective'], ['high','adjective'], ['such','adjective'], ['follow','verb'], ['act','verb'], ['why','question'], ['ask','verb'], ['men','noun'], ['change','verb'], ['went','verb'], ['light','adjective'], ['kind','adjective'], ['off','adverb'], ['need','verb'], ['house','noun'], ['picture','noun'], ['try','verb'], ['us','pronoun'], ['again','adverb'], ['animal','noun'], ['point','verb'], ['mother','noun'], ['world','noun'], ['near','preposition'], ['build','verb'], ['self','noun'], ['earth','noun'], ['father','noun'], ['head','noun'], ['stand','verb'], ['own','adjective'], ['page','noun'], ['should','verb'], ['country','noun'], ['found','verb'], ['answer','verb'], ['school','noun'], ['grow','verb'], ['study','verb'], ['still','adjective'], ['learn','verb'], ['plant','noun'], ['cover','verb'], ['food','noun'], ['sun','noun'], ['four','adjective'], ['thought','noun'], ['let','verb'], ['keep','verb'], ['eye','noun'], ['never','adverb'], ['last','adjective'], ['door','noun'], ['between','preposition'], ['city','noun'], ['tree','noun'], ['cross','verb'], ['since','adverb'], ['hard','adjective'], ['start','verb'], ['might','verb'], ['story','noun'], ['saw','verb'], ['far','adverb'], ['sea','noun'], ['draw','verb'], ['left','adjective'], ['late','adjective'], ['run','verb'], ['donít',''], ['while','noun'], ['press','verb'], ['close','verb'], ['night','time'], ['real','adjective'], ['life','noun'], ['few','adjective'], ['stop','verb'], ['open','verb'], ['seem','verb'], ['together','adverb'], ['next','adjective'], ['white','adjective'], ['children','noun'], ['begin','verb'], ['got','verb'], ['walk','verb'], ['example','noun'], ['ease','noun'], ['paper','noun'], ['often','adverb'], ['always','adverb'], ['music','noun'], ['those','pronoun'], ['both','adjective'], ['mark','noun'], ['book','noun'], ['letter','noun'], ['until','conjunction'], ['mile','noun'], ['river','noun'], ['car','noun'], ['feet','noun'], ['care','verb'], ['second','adjective'], ['group','noun'], ['carry','verb'], ['took','verb'], ['rain','noun'], ['eat','verb'], ['room','noun'], ['friend','noun'], ['began','verb'], ['idea','noun'], ['fish','noun'], ['mountain','noun'], ['north','noun'], ['once','adverb'], ['base','noun'], ['hear','verb'], ['horse','noun'], ['cut','verb'], ['sure','adjective'], ['watch','verb'], ['color','noun'], ['face','noun'], ['wood','noun'], ['main','adjective'], ['enough','adjective'], ['plain','adjective'], ['girl','noun'], ['usual','adjective'], ['young','adjective'], ['ready','adjective'], ['above','preposition'], ['ever','adverb'], ['red','adjective'], ['list','noun'], ['though','conjunction'], ['feel','verb'], ['talk','verb'], ['bird','noun'], ['soon','time'], ['body','noun'], ['dog','noun'], ['family','noun'], ['direct','verb'], ['pose','verb'], ['leave','verb'], ['song','noun'], ['measure','verb'], ['state','noun'], ['product','noun'], ['black','adjective'], ['short','adjective'], ['numeral','noun'], ['class','noun'], ['wind','noun'], ['question','noun'], ['happen','verb'], 
        ['complete','adjective'], ['ship','noun'], ['area','noun'], ['half','adjective'], ['rock','noun'], ['order','verb'], ['fire','noun'], ['south','adjective'], ['problem','noun'], ['piece','noun'], ['told','verb'], ['knew','verb'], ['pass','verb'], ['farm','noun'], ['top','noun'], ['whole','adjective'], ['king','noun'], ['size','noun'], ['heard','verb'], ['best','adjective'], ['hour','noun'], ['better','adjective'], ['TRUE','adjective'], ['during','preposition'], ['hundred','adjective'], ['am','verb'], ['remember','verb'], ['step','verb'], ['early','adverb'], ['hold','verb'], ['west','adjective'], ['ground','noun'], ['interest','noun'], ['reach','verb'], ['fast','adverb'], ['five','adjective'], ['sing','verb'], ['listen','verb'], ['six','adjective'], ['table','noun'], ['travel','verb'], ['less','adverb'], ['morning','time'], ['ten','adjective'], ['simple','adjective'], ['several','adjective'], ['vowel','noun'], ['toward','preposition'], ['war','noun'], ['lay','verb'], ['against','preposition'], ['pattern','noun'], ['slow','adverb'], ['center','noun'], ['love','verb'], ['person','noun'], ['money','noun'], ['serve','verb'], ['appear','verb'], ['road','noun'], ['map','noun'], ['science','noun'], ['rule','verb'], ['govern','verb'], ['pull','verb'], ['cold','adjective'], ['notice','verb'], ['voice','noun'], ['fall','verb'], ['power','noun'], ['town','noun'], ['fine','adjective'], ['certain','adjective'], ['fly','noun'], ['unit','noun'], ['lead','verb'], ['cry','verb'], ['dark','adjective'], ['machine','noun'], ['note','noun'], ['wait','verb'], ['plan','noun'], ['figure','noun'], ['star','noun'], ['box','noun'], ['noun','noun'], ['field','noun'], ['rest','verb'], ['correct','verb'], ['able','adjective'], ['pound','verb'], ['done','verb'], ['beauty','noun'], ['drive','verb'], ['stood','verb'], ['contain','verb'], ['front','noun'], ['teach','verb'], ['week','noun'], ['final','adjective'], ['gave','verb'], ['green','adjective'], ['oh','verb'], ['quick','adverb'], ['develop','verb'], ['sleep','verb'], ['warm','adjective'], ['free','adjective'], ['minute','noun'], ['strong','adjective'], ['special','adjective'], ['mind','noun'], ['behind','preposition'], ['clear','adjective'], ['tail','noun'], ['produce','verb'], ['fact','noun'], ['street','noun'], ['inch','noun'], ['lot','noun'], ['nothing','noun'], ['course','noun'], ['stay','verb'], ['wheel','noun'], ['full','adjective'], ['force','verb'], ['blue','adjective'], ['object','noun'], ['decide','verb'], ['surface','noun'], ['deep','adjective'], ['moon','noun'], ['island','noun'], ['foot','noun'], ['yet','adverb'], ['busy','adjective'], ['test','noun'], ['record','verb'], ['boat','noun'], ['common','adjective'], ['gold','adjective'], ['possible','adjective'], ['plane','noun'], ['age','noun'], ['dry','adjective'], ['wonder','verb'], ['laugh','verb'], ['thousand','adjective'], ['ago','adjective'], ['ran','verb'], ['check','verb'], ['game','noun'], ['shape','noun'], ['yes','adverb'], ['cool','adjective'], ['miss','verb'], ['brought','verb'], ['heat','noun'], ['snow','noun'], ['bed','noun'], ['bring','verb'], ['sit','verb'], ['perhaps','adverb'], ['fill','verb'], ['east','adjective'], ['weight','noun'], ['language','noun'], ['among','preposition']]
  
        words = []
        wordsPartsOfSpeech = []
        singleWord = ""
        sentenceVerb = []
        sentenceSubject = []
        sentenceObject = []
        sentenceObjectDescription = []
        sentenceSubjectDescription = []
        sentenceLocation = []
        sentenceTime = []
        sentenceRecipient = []
        

        
        questionWords = []
        questionWordsPartsOfSpeech = []
        questionSingleWord = ""
        questionKeyWord = []
        questionVerb = []
        questionSubject = []
        questionObject = []
        questionLocation = []

        

        
        strSentence = sentence
        strQuestion = question

        #print(strSentence)
        #print(strQuestion)
                    


        #####################
        #BUILD SENTENCE FRAME
        #####################

        lengthOfSentence = 0
        for i in range(len(strSentence)):
            if(strSentence[i] == " "):
                words.append(singleWord)
                singleWord = ""
                lengthOfSentence += 1
            elif i == len(strSentence)-1:
                    words.append(singleWord)
                    singleWord = ""
            else:
                singleWord =  singleWord + strSentence[i]
        lengthOfSentence += 1


        
        for j in range(len(words)):
            currentWordFound = False
            for k in range(len(partsOfSpeech)):
                if(words[j].lower() == partsOfSpeech[k][0].lower()):
                    wordsPartsOfSpeech.append(partsOfSpeech[k][1].lower())
                    currentWordFound = True
            if(not currentWordFound):
                wordsPartsOfSpeech.append('noun')
                    
                    
        #Find Sentence Subject and Verb
        verbIndex=-1
        subjectIndex=-1
        for n in range(len(wordsPartsOfSpeech)):
            if(wordsPartsOfSpeech[n] == 'verb'):
                sentenceVerb.append(words[n])
                verbIndex = n
                if(len(words)>n+1):
                    if(wordsPartsOfSpeech[n+1] == 'verb'):
                        sentenceVerb.append(words[n+1])
                        verbIndex = n + 1
                
                break
            elif((wordsPartsOfSpeech[n] == 'name' or wordsPartsOfSpeech[n] == 'noun' or wordsPartsOfSpeech[n] == 'pronoun') and len(sentenceSubject) == 0):
                sentenceSubject.append(words[n])
                subjectIndex=n
                #if(len(wordsPartsOfSpeech)>n+2 and words[n+1] == 'and'):
                 #   sentenceSubject.append(words[n+2])
                 
        #If no subject was found before verb, look after verb
        if(len(sentenceSubject) == 0):
            x = verbIndex + 1
            while x < len(words):
                if(wordsPartsOfSpeech[x] == 'name' or wordsPartsOfSpeech[x] == 'noun' or wordsPartsOfSpeech[x] == 'pronoun'):
                    sentenceSubject.append(words[x])
                    subjectIndex=x
                    break
                x += 1

        #Find Subject description
        if(wordsPartsOfSpeech[subjectIndex-1] == 'adjective'):
            sentenceSubjectDescription.append(words[subjectIndex-1])
        elif(wordsPartsOfSpeech[subjectIndex-2] == 'adjective'):
            sentenceSubjectDescription.append(words[subjectIndex-2])
        elif(wordsPartsOfSpeech[subjectIndex-3] == 'adjective'):
            sentenceSubjectDescription.append(words[subjectIndex-3])
                    

        #Find Sentence Object
        m = verbIndex+1
        objectIndex=-1
        while m < len(words):
            if(wordsPartsOfSpeech[m] == 'noun'):
                if(wordsPartsOfSpeech[m-1] == 'determiner'):
                    pass
                elif(words[m].lower() == sentenceSubject[0].lower()):
                    pass
                else:
                    sentenceObject.append(words[m])
                    objectIndex=m
                    break
            m += 1
            
        if(len(sentenceObject)==0 and words[subjectIndex+1].lower()=='of'):
            sentenceObject.append(words[subjectIndex+2])

        #Find Object Description

        if(wordsPartsOfSpeech[objectIndex-1] == 'adjective'):
            sentenceObjectDescription.append(words[objectIndex-1])
        elif(wordsPartsOfSpeech[objectIndex-2] == 'adjective'):
            sentenceObjectDescription.append(words[objectIndex-2])
        elif(wordsPartsOfSpeech[objectIndex-3] == 'adjective'):
            sentenceObjectDescription.append(words[objectIndex-3])

        #Find Object recipient
        p = objectIndex+1
        while p < len(words):
            if(len(words) > p + 1):
                if(words[p].lower() == 'to'):
                    if(wordsPartsOfSpeech[p+1] == 'name'):
                        sentenceRecipient.append(words[p+1])
            p += 1

        #Find Sentence Location
        q = objectIndex + 1
        while q < len(words):
            if(len(words)> q+1):
                if(words[q].lower() == 'to' or words[q].lower() == 'at' or words[q].lower() == 'in'):
                    if(wordsPartsOfSpeech[q+1] == 'noun'):
                        sentenceLocation.append(words[q+1])
            q += 1

        #Find Sentence Time
        timeString = ""
        for i in range(len(strSentence)):
            if(strSentence[i] == ":"):
                timeString=strSentence[i-2:i+3]
                if(len(strSentence)>i+4):
                    if((strSentence[i+3] == 'A' and strSentence[i+4] == 'M') or (strSentence[i+3] == 'P' and strSentence[i+4] == 'M')):
                        timeString = timeString + (strSentence[i+3])
                        timeString = timeString + (strSentence[i+4])
        if(len(timeString)>0):
            sentenceTime.append(timeString.strip())
        if(len(sentenceTime)==0):
            for q in range(len(wordsPartsOfSpeech)):
                if(wordsPartsOfSpeech[q].lower() == 'time'):
                    sentenceTime.append(words[q])
                        
                    
                


        #####################
        #BUILD QUESTION FRAME
        #####################

        for i in range(len(strQuestion)):
            if(strQuestion[i] == " "):
                questionWords.append(questionSingleWord)
                questionSingleWord = ""
            elif i == len(strQuestion)-1:
                questionWords.append(questionSingleWord)
                questionSingleWord = ""
            else:
                questionSingleWord = questionSingleWord + strQuestion[i]

                
        
        for j in range(len(questionWords)):
            wordFound = False
            for k in range(len(partsOfSpeech)):
                if(questionWords[j].lower() == partsOfSpeech[k][0].lower()):
                    questionWordsPartsOfSpeech.append(partsOfSpeech[k][1].lower())
                    wordFound = True
            if(not wordFound):
                questionWordsPartsOfSpeech.append('noun')
                
                

        
        #Find Question Key word
        for j in range(len(questionWordsPartsOfSpeech)):
            if(questionWordsPartsOfSpeech[j] == 'question'):
                questionKeyWord.append(questionWords[j])
        if(len(questionKeyWord)==0):
            questionKeyWord.append(questionWords[0])


        #Find Question Subject
        questionSubjectIndex=-1
        for n in range(len(questionWordsPartsOfSpeech)):
            if(questionWordsPartsOfSpeech[n] == 'name'):
                questionSubject.append(questionWords[n])
                questionSubjectIndex=n
                if(len(questionWordsPartsOfSpeech) > n+1 and questionWords[n+1] == 'and'):
                    questionSubject.append(questionWords[n+2])
                    questionSubjectIndex=n+2
                
                break
            

        #Find Question Verb
        questionVerbIndex = -1
        for n in range(len(questionWords)):
            if(questionWordsPartsOfSpeech[n] == 'verb'):
                questionVerb.append(questionWords[n])
                questionVerbIndex = n
                    
            

        #Find Question Object
        y = questionVerbIndex+1
        while y<len(questionWords):
            if(questionWords[y] == "the" or questionWords[y] == "a" or questionWords[y] == "an"):
                questionObject.append(questionWords[y+1])
                break
            y+=1
            
        if(len(questionObject) == 0 and questionWordsPartsOfSpeech[-1].lower() !=  'verb'):
            z = questionVerbIndex+1
            while z < len(questionWords):
                if(questionWordsPartsOfSpeech[z] == "noun" or questionWordsPartsOfSpeech[z] == "name"):
                   questionObject.append(questionWords[z])
                   break
                z+=1

        if(len(questionObject) == 0 and questionWordsPartsOfSpeech[-1].lower() !=  'verb'):
            for a in range(len(questionWords)):
                if(questionWordsPartsOfSpeech[a].lower() == 'name' or questionWordsPartsOfSpeech[a].lower() == 'noun'):
                    questionObject.append(questionWords[a])
                    break

        #Find Question Location
        for q in range(len(questionWords)):
            if(len(questionWords)> q+1):
                if(questionWords[q].lower() == 'to' or questionWords[q].lower() == 'at' or questionWords[q].lower() == 'in'):
                    if(questionWordsPartsOfSpeech[q+1] == 'noun'):
                        questionLocation.append(questionWords[q+1])
            q += 1
         
        

        
        """
        print("SENTENCE")
        print(sentenceVerb)
        print(sentenceSubject)
        print(sentenceObject)
        print(sentenceObjectDescription)
        print(sentenceSubjectDescription)
        print(sentenceRecipient)
        print(sentenceLocation)
        print(sentenceTime)

        print("QUESTION")
        print(questionKeyWord)
        print(questionSubject)
        print(questionVerb)
        print(questionObject)
        print(questionLocation)
        """


        if(questionKeyWord[0].lower() == 'where'):
            if(len(sentenceLocation)>0):
                answer = sentenceLocation[0]
            else:
                for u in range(len(words)):
                    if(words[u].lower() == 'in' or words[u].lower() == 'at' or words[u].lower() == 'to' or words[u].lower() == 'from'):
                        while u < len(words):
                            if(wordsPartsOfSpeech[u].lower() == 'noun'):
                                answer = words[u]
                            u +=1
                    elif(words[u].lower() == 'of'):
                        if(wordsPartsOfSpeech[u-1].lower() == 'adjective'):
                            answer = words[u-1]
                        u += 1
        elif('time' in questionWords):
            answer = sentenceTime[0]
        elif(questionKeyWord[0].lower() == 'when'):
            if(len(sentenceTime)>0):
                if(len(sentenceTime)>0):
                    answer = sentenceTime[0]
            else:
                if(len(sentenceObject)>0):
                    answer = sentenceObject[0]
                
        elif(questionKeyWord[0].lower() == 'who'):
            if(len(sentenceSubject) == 1):
                if(sentenceSubject[0] in questionWords):
                    answer = sentenceRecipient[0]
                else:
                    answer = sentenceSubject[0]
            elif(len(sentenceSubject)>1):
                if(sentenceSubject[0] in questionWords):
                    answer = sentenceSubject[1]
                else:
                    answer = sentenceSubject[0]
        elif(questionKeyWord[0].lower() == 'what'):
            if(questionWordsPartsOfSpeech[1] == 'noun'):
                if(questionWords[-1].lower() == sentenceSubject[0].lower()):
                    answer = sentenceSubjectDescription[0]
                elif(questionWords[-1].lower() == sentenceObject[0].lower()):
                    answer = sentenceObjectDescription[0]
                
            else:
                if(len(sentenceObject)>0):
                    if(len(sentenceSubject)>0):
                        if(sentenceObject[0] in questionWords):
                            answer = sentenceSubject[0]
                        else:
                            answer = sentenceObject[0]
                     
                    else:
                        answer = sentenceObject[0]
                elif(len(sentenceSubject)>0):
                    if(len(sentenceObject)>0):
                        if(sentenceSubject[0] in questionWords):
                            answer = sentenceObject[0]
                        else:
                            answer = sentenceSubject[0]
                    else:
                        answer = sentenceSubject[0]
        elif(questionKeyWord[0].lower() == 'how'):
            if(len(questionObject)>0 and len(sentenceObject)>0 and len(sentenceObjectDescription)>0):
                if(len(sentenceObjectDescription[0])>0 and questionObject[0].lower() == sentenceObject[0].lower()): 
                    answer = sentenceObjectDescription[0]
                elif(questionLocation[0].lower() == sentenceLocation[0].lower() and len(sentenceVerb)>0):
                    answer = sentenceVerb[0]
            elif(questionVerb[-1].lower() == sentenceVerb[0].lower() and len(sentenceObject)>0):
                answer = sentenceObject[0]
            elif(questionLocation[0].lower() == sentenceLocation[0].lower() and len(sentenceVerb)>0):
                answer = sentenceVerb[0]

                    

        



        #print(strQuestion)
        #print(answer)
        return answer
