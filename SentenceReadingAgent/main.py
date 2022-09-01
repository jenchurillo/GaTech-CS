from SentenceReadingAgent import SentenceReadingAgent

def test():
    #This will test your SentenceReadingAgent
	#with nine initial test cases.

    test_agent = SentenceReadingAgent()

    sentence_1 = "Ada brought a short note to Irene."
    question_1 = "Who brought the note?"
    question_2 = "What did Ada bring?"
    question_3 = "Who did Ada bring the note to?"
    question_4 = "How long was the note?"

    sentence_2 = "David and Lucy walk one mile to go to school every day at 8:00AM when there is no snow."
    question_5 = "Who does Lucy go to school with?"
    question_6 = "Where do David and Lucy go?"
    question_7 = "How far do David and Lucy walk?"
    question_8 = "How do David and Lucy get to school?"
    question_9 = "At what time do David and Lucy walk to school?"

    sentence_3 = "Their children are in school."
    question_10 = "Who is in school?"

    sentence_4 = "The blue bird will sing in the morning."
    question_11 = "When will the blue bird sing?"

    sentence_5 = "Give us all your money."
    question_12 = "How much of your money should you give us?"

    sentence_6 = "Serena ran a mile this morning."
    question_13 = "When did Serena run?"

    sentence_7 = "The sound of rain is cool."
    question_14 = "What has a cool sound?"
    question_30 = "What is cool?"

    sentence_8 = "This year David will watch a play."
    question_15 = "Who will watch a play?"
    question_16 = "What will David watch?"

    sentence_9 = "She told her friend a story."
    question_17 = "What did she tell?"

    sentence_10 = "The red fish is in the river."
    question_18 = "What color is the fish?"

    sentence_11 = "There is snow at the top of the mountain."
    question_19 = "Where is the snow?"

    sentence_12 = "The island is east of the city."
    question_20 = "What is east of the city?"
    question_29 = "Where is the island?"

    sentence_13 = "There are a thousand children in this town."
    question_21 = "Where are the children?"

    sentence_14 = "The red fish is in the river."
    question_22 = "Where is the fish?"

    sentence_15 = "There are a thousand children in this town."
    question_23 = "Who is in this town?"

    sentence_16 = "The house is made of paper."
    question_24 = "What is made of paper?"

    sentence_17 = "A tree is made of wood."
    question_25 = "What is made of wood?"

    sentence_18 = "There are three men in the car."
    question_26 = "How many men are in the car?"

    sentence_19 = "Their children are in school."
    question_27 = "Where are their children?"

    sentence_20 = "Bring the dog to the other room."
    question_28 = "Where should the dog go?"

    sentence_21 = "My dog Red is very large."
    question_32 = "What is my dog's name?"

    sentence_22 = "The white dog and the blue horse play together."
    question_33 = "What animal is white?"
    question_34 = "What do the dog and horse do?"

    
    #print(test_agent.solve(sentence_1, question_1))  # "Ada"
    #print(test_agent.solve(sentence_1, question_2))  # "note" or "a note"
    #print(test_agent.solve(sentence_1, question_3))  # "Irene"
    #print(test_agent.solve(sentence_1, question_4))  # "short"

    #print(test_agent.solve(sentence_2, question_5))  # "David"
    #print(test_agent.solve(sentence_2, question_6))  # "school"
    #print(test_agent.solve(sentence_2, question_7))  # "mile" or "a mile"
    #print(test_agent.solve(sentence_2, question_8))  # "walk"
    #print(test_agent.solve(sentence_2, question_9))  # "8:00AM"

    """
    print(test_agent.solve(sentence_3, question_10)) #children

    print(test_agent.solve(sentence_4, question_11)) #morning

    print(test_agent.solve(sentence_5, question_12)) #all

    print(test_agent.solve(sentence_6, question_13)) #morning

    print(test_agent.solve(sentence_7, question_14)) #rain
    
    
    print(test_agent.solve(sentence_8, question_15)) #David
    print(test_agent.solve(sentence_8, question_16)) #Play
    
    print(test_agent.solve(sentence_9, question_17)) #story
    
    print(test_agent.solve(sentence_10, question_18)) #red

    print(test_agent.solve(sentence_11, question_19)) #mountain
    print(test_agent.solve(sentence_13, question_21)) #town
    print(test_agent.solve(sentence_14, question_22)) #river
    
    
    print(test_agent.solve(sentence_12, question_20)) #island
    print(test_agent.solve(sentence_15, question_23)) #island
    
    print(test_agent.solve(sentence_16, question_24)) #island
    print(test_agent.solve(sentence_17, question_25)) #island
    

    print(test_agent.solve(sentence_18, question_26)) 

    print(test_agent.solve(sentence_19, question_27))
    print(test_agent.solve(sentence_20, question_28))
    
    print(test_agent.solve(sentence_12, question_29))
    """
    print(test_agent.solve(sentence_22, question_33))
    
if __name__ == "__main__":
    test()
