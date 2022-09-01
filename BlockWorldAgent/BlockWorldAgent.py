class BlockWorldAgent:
    def __init__(self):
        #If you want to do any initial processing, add it here.
        pass

    """
    def popNode(self):
        
        topPriorityNode = 0
        
        for i in range(len(self.queue)):
            if(self.queue[topPriorityNode][1] > self.queue[i][1]):
                topPriorityNode = i
                i += 1
            elif(self.queue[topPriorityNode][1] == self.queue[i][1]):
                #Keep the origional topPriorityNode
                i += 1
        returnNode = self.queue[topPriorityNode]
        del self.queue[topPriorityNode]
        return returnNode
    """


    def solve(self, initial_arrangement, goal_arrangement):
        initial_state = initial_arrangement
        goal_state = goal_arrangement
        goal_state = sorted(goal_state)
        blocks = []
        possible_relationships = []
        possible_move_deltas = []
        possible_moves = []
        reached = []
        goal_block_relationships = []
        solved = False
        sequence_of_moves = []
        final_sequence = []
        final_path_options = []

        
        queue = []
        queue.append((initial_state,0))
        paths=[[initial_state]]
        pathMoves = [[]]
        pathOptions = []
        pathOptionMoves = []
        current_state = queue.pop()[0]
        
        

        for i in range(len(initial_state)):
            for j in range(len(initial_state[i])):
                blocks.append(initial_state[i][j])

        for i in range(len(goal_state)):
            for j in range(len(goal_state[i])):
                if(j == 0):
                    goal_block_relationships.append(goal_state[i][j]+" on "+"table")
                else:
                    goal_block_relationships.append(goal_state[i][j]+" on "+goal_state[i][j-1])

        numOfBlocks = len(blocks)


        a = 0
        #while a < 75:
        while(not solved):
            reached.append(sorted(current_state))

            #print("CURRENT STATE")
            #print(current_state)

            #print("Goal Statet")
            #print(goal_state)

            #print(goal_block_relationships)
            

            #DETERMINE IF SUBGOALS HAVE BEEN REACHED
            currentStateSubGoals = []
            for i in range(len(current_state)):
                subGoalReached = True
                q = 0
                while q < len(current_state[i]):
                    if(q == 0):
                        #print(current_state[i][q]+" on table")
                        if(current_state[i][q]+" on table" in goal_block_relationships):
                            pass
                        else:
                            subGoalReached = False
                            break

                    else:
                        #print(current_state[i][q]+" on "+current_state[i][q-1])
                        if(current_state[i][q]+ " on " + current_state[i][q-1] in goal_block_relationships):
                            pass
                        else:
                            subGoalReached = False
                            break
                    q += 1
                currentStateSubGoals.append(subGoalReached)

            #print(currentStateSubGoals)
            #print(current_state)
                        
            


            #DETERMINE NEW POSSIBLE STATES
            for i in range(len(current_state)):
                blockToMove = current_state[i][-1]
                #print(blockToMove)

                if(len(current_state[i]) == 1 and blockToMove+" on table" in goal_block_relationships):
                    pass
                
                else:
                    if(currentStateSubGoals[i]):
                        pass
                    
                    else:
                        
                        for k in range(len(current_state)):
                            #print(currentStateSubGoals[k])
                            #print("HERE")
                            #print(current_state[k][-1])
                            if(currentStateSubGoals[k] and blockToMove + " on " + current_state[k][-1] not in goal_block_relationships):
                                pass
                            elif(not currentStateSubGoals[k] and blockToMove + " on " + current_state[k][-1] in goal_block_relationships):
                                pass
                            elif(blockToMove + " on " + current_state[k][-1] not in goal_block_relationships):
                                pass
                    
                            else:
                               
                                new_state = []
                                for j in range(len(current_state)):
                                    if(blockToMove in current_state[j]):
                                        move = current_state[j].copy()
                                        move.remove(blockToMove)
                                        if(move == []):
                                            pass
                                        else:
                                            new_state.append(move)
                                    else:
                                        if(j == k):
                                            move = current_state[j].copy()
                                            move.append(blockToMove)
                                            new_state.append(move)
                                            sequence_of_moves.append([blockToMove,move[-2]])
                                        else:
                                            move = current_state[j].copy()
                                            new_state.append(move)

                                newBlocks = 0
                                for i in range(len(new_state)):
                                    for j in range(len(new_state[i])):
                                        newBlocks += 1

                                if(newBlocks == numOfBlocks):
                                    possible_moves.append(sorted(new_state))

                        tableMove = []
                        for m in range(len(current_state)):
                            if(blockToMove in current_state[m]):
                                if(currentStateSubGoals[m]):
                                    pass
                                else:
                                    move = current_state[m].copy()
                                    move.remove(blockToMove)
                                    if(move == []):
                                        pass
                                    else:
                                        tableMove.append(move)
                                    tableMove.append([blockToMove])
                            else:
                                move = current_state[m].copy()
                                tableMove.append(move)
                                #print(tableMove)
                                
                        sequence_of_moves.append([blockToMove,'Table'])
                        possible_moves.append(sorted(tableMove))

            #print("Possible Moves Before")
            
            #for x in range(len(possible_moves)):
               # print(possible_moves[x])

            #print("reached")
            #print(reached)
            
            u = 0
            while(u < len(possible_moves)):
                if(possible_moves[u] in reached):
                    #print("DELETE")
                    #print(possible_moves[u])
                    del possible_moves[u]
                    del sequence_of_moves[u]
                else:
                    u += 1
            

            """        
            u = 0
            while(u < len(possible_moves)):
                alreadyInQueue = False
                for i in range(len(queue)):
                    if(queue[i][0] == possible_moves[u]):
                        alreadyInQueue = True
                if(alreadyInQueue):
                    del possible_moves[u]
                    del sequence_of_moves[u]
                else:
                    u += 1
            """
                    
                        
                
      
            #print("MOVES")
            for x in range(len(possible_moves)):
                #print(possible_moves[x])
                possible_move_block_relationships = []
                for y in range(len(possible_moves[x])):
                    for z in range(len(possible_moves[x][y])):
                        if(z == 0):
                            possible_move_block_relationships.append(possible_moves[x][y][z]+" on "+"table")
                        else:
                            possible_move_block_relationships.append(possible_moves[x][y][z]+" on "+possible_moves[x][y][z-1])
                possible_relationships.append(possible_move_block_relationships)


            for x in range(len(possible_relationships)):
                delta = 0

                for y in range(len(goal_block_relationships)):
                    if(goal_block_relationships[y] in possible_relationships[x]):
                        pass
                    else:
                        delta += 1
                possible_move_deltas.append(delta)

            
          


            #print("Paths")
            #for x in range(len(paths)):
            #    print(paths[x])

                
            exists = False
            inQueue = False
            for j in range(len(possible_moves)):
                if(possible_moves[j] in reached):
                    pass
                else:
                    for k in range(len(paths)):
                        if(paths[k][-1] == current_state):
                            expandPath = paths[k].copy()
                            expandPathMoves = pathMoves[k].copy()
                            if(expandPath in pathOptions):
                                pathOptions.remove(expandPath)
                            if(expandPathMoves in pathOptionMoves):
                                pathOptionMoves.remove(expandPathMoves)
                            expandPath.append(possible_moves[j])
                            pathLength = len(expandPath)
                            expandPathMoves.append(sequence_of_moves[j])
                            for z in range(len(pathOptions)):
                                if((pathOptions[z] == expandPath) or (len(pathOptions[z]) <= len(expandPath) and pathOptions[z][-1] == expandPath[-1])):
                                    exists = True
                            if(not exists):
                                pathOptions.append(expandPath)
                                pathOptionMoves.append(expandPathMoves)
                                expandPath = []
                                expandPathMoves = []
                            #exists = False
                            queue.append((possible_moves[j], possible_move_deltas[j]+pathLength))



                            
                            """
                            if(len(queue) == 0):
                                queue.append((possible_moves[j], possible_move_deltas[j]+pathLength))
                            else:
                                for i in range(len(queue)):
                                    if(queue[i][0] == possible_moves[j]):
                                        if(queue[i][1] <= possible_move_deltas[j]+pathLength):
                                            inQueue = True
                                if(not inQueue):
                                    queue.append((possible_moves[j], possible_move_deltas[j]+pathLength))
                            inQueue = False
                            """
                            
            #print("Possible Moves")
            
            #for x in range(len(possible_moves)):
            #    print(possible_moves[x])
            #print(queue)
              
                            
                                
                                
            #print("Path Options")
            #for x in range(len(pathOptions)):
            #    print(pathOptions[x])


            
            #if(len(queue)<5):
            #    print("Path Options")
            #    for x in range(len(pathOptions)):
            #        print(pathOptions[x])
            #    print("QUEUE")
            #    print(queue)


            for n in range(len(pathOptions)):
                if(sorted(pathOptions[n][-1]) == sorted(goal_state)):
                    #print(pathOptions[n][-1])
                    #print("SOLVED")
                    solved = True
                    i = 0
                    final_path_options.append(pathOptionMoves[n])

                
            if(len(final_path_options)>0):
                bestPathIndex = 0
                bestPath = final_path_options[bestPathIndex]

                
                
                for i in range(len(final_path_options)):
                    if(len(final_path_options[i]) < len(final_path_options[bestPathIndex])):
                        bestPathIndex = i
                        bestPath = final_path_options[i]

                j = 0
                while j < len(bestPath):
                    finalPath = (bestPath[j][0],bestPath[j][1])
                    final_sequence.append(finalPath)
                    j += 1

                #print(final_sequence)
                
                   
                   #while i < len(pathOptionMoves[n]):
                   #     finalPath = (pathOptionMoves[n][i][0],pathOptionMoves[n][i][1])
                   #     final_sequence.append(finalPath)
                   #     i += 1

            min_delta_index = 0
            min_delta = queue[min_delta_index][1]
            for w in range(len(queue)):
                if(queue[w][1]<min_delta):
                    min_delta = queue[w][1]
                    min_delta_index = w
            
            current_state = queue[min_delta_index][0]
            
            del queue[min_delta_index]
            paths = pathOptions.copy()
            pathMoves = pathOptionMoves.copy()

            possible_relationships = []
            possible_move_deltas = []
            possible_moves = []
            sequence_of_moves = []
            a += 1


        return final_sequence
        
        


