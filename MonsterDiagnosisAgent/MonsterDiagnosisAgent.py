class MonsterDiagnosisAgent:
    def __init__(self):
        # If you want to do any initial processing, add it here.
        pass

    def solve(self, diseases, patient):
        # Add your code here!
        #
        # The first parameter to this method is a list of diseases, represented as a
        # list of 2-tuples. The first item in each 2-tuple is the name of a disease. The
        # second item in each 2-tuple is a dictionary of symptoms of that disease, where
        # the keys are letters representing vitamin names ("A" through "Z") and the values
        # are "+" (for elevated), "-" (for reduced), or "0" (for normal).
        #
        # The second parameter to this method is a particular patient's symptoms, again
        # represented as a dictionary where the keys are letters and the values are
        # "+", "-", or "0".
        #
        # This method should return a list of names of diseases that together explain the
        # observed symptoms. If multiple lists of diseases can explain the symptoms, you
        # should return the smallest list. If multiple smallest lists are possible, you
        # may return any sufficiently explanatory list.
        #pass

        diseaseList = []
        symptoms = list(patient.values())
        possibleDiseases = list(diseases.keys())
        diseaseSymptoms = []
        solutionFound = False
        pathOptions = []

        for vitamin, vitaminValue in diseases.items():
            possibleDiseaseSymptoms = []
            for key in vitaminValue:
                possibleDiseaseSymptoms.append(vitaminValue[key])
            diseaseSymptoms.append(possibleDiseaseSymptoms)


        #print(symptoms)
        #print(possibleDiseases)
        #print(diseaseSymptoms[0])
        #print(diseaseSymptoms[1])


        #Check if one of the diseases matches the symptoms exactly
        for i in range(len(diseaseSymptoms)):
            if(diseaseSymptoms[i]==symptoms):
                diseaseList.append(possibleDiseases[i])
                solutionFound = True

        if(not solutionFound):
            possiblePaths = []
            for i in range(len(possibleDiseases)):
                possiblePaths.append([possibleDiseases[i]])

            #print(possiblePaths)
            #x = 0
            #while(x<1):
            while(not solutionFound):
                for j in range(len(possiblePaths)):
                    currentState = possiblePaths[j][-1]
                    #Build out list of possible neighbors
                    neighbors = []
                    for k in range(len(possibleDiseases)):
                        if(possibleDiseases[k] in possiblePaths[j]):
                            pass
                        else:
                            neighbors.append(possibleDiseases[k])


                    for n in range(len(neighbors)):
                        expandPath = possiblePaths[j].copy()
                        if(expandPath in pathOptions):
                            pathOptions.remove(expandPath)
                        expandPath.append(neighbors[n])
                        expandPath.sort()
                        if(expandPath in pathOptions):
                            pass
                        else:
                            pathOptions.append(expandPath)
                        expandPath = []

                possiblePaths = pathOptions.copy()
                possiblePathSymptoms = []
                #print(possiblePaths)
                for i in range(len(possiblePaths)):
                    pathSymptoms = []
                    for k in range(len(possiblePaths[i])):
                        diseaseIndex = -1
                        for j in range(len(possibleDiseases)):
                            if(possiblePaths[i][k] == possibleDiseases[j]):
                                diseaseIndex = j
                        #print("DISEASE")
                        #print(diseaseSymptoms[diseaseIndex])
                        #print(possibleDiseases[diseaseIndex])
                        pathSymptoms.append(diseaseSymptoms[diseaseIndex])
                    possiblePathSymptoms.append(pathSymptoms)


                totalPathSymptoms = []
                for i in range(len(possiblePaths)):
                    totalPathSymptoms.append([])
                    
                n = 0
                while n < 26:
                    for i in range(len(possiblePathSymptoms)):
                        plusCount = 0
                        minusCount = 0
                        zeroCount = 0
                        symptomCount = 0
                        for j in range(len(possiblePathSymptoms[i])):
                            
                            #print("PATHS")
                            #print(possiblePathSymptoms[i])
                            #print(possiblePathSymptoms[i][j])
 
                            if(possiblePathSymptoms[i][j][n] == "+"):
                                symptomCount += 1
                            if(possiblePathSymptoms[i][j][n] == "-"):
                                symptomCount -= 1
                            if(possiblePathSymptoms[i][j][n] == "0"):
                                symptomCount += 0
                        #print("COUNT")
                        #print(symptomCount)
                        #print(plusCount)
                        #print(minusCount)
                        #print(zeroCount)

                        if(symptomCount>0):
                            totalPathSymptoms[i].append('+')    
                        elif(symptomCount<0):
                            totalPathSymptoms[i].append('-')      
                        elif(symptomCount==0):
                            totalPathSymptoms[i].append('0')
                            
                        
                    n += 1

                #print(symptoms)
                
                for y in range(len(totalPathSymptoms)):
                    #print(totalPathSymptoms[y])
                    if(totalPathSymptoms[y]==symptoms):
                        #print("YES")
                        #print(pathOptions[y])
                        diseaseList = pathOptions[y]
                        solutionFound = True
                        
                #print(totalPathSymptoms)   
                #x += 1
                #print("PATH OPTIONS")
                #for i in range(len(pathOptions)):
                #    print(pathOptions[i])
                #    print(possiblePathSymptoms[i])
                #    print(totalPathSymptoms[i])

        
                            






        return diseaseList

