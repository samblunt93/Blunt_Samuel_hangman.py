#!/usr/bin/env python
# coding: utf-8

# In[1]:


#pick a random word from a list
def word_pick():
    import random
    with open('word_file.txt') as myfile:
        wordlist = myfile.readlines()
    
    useablelist = []
    for i in wordlist:
        useablelist.append(i.strip())


    word = random.choice(useablelist)
    return word


# In[2]:


#replace each letter with underscores
def hide_word(word):
    
    lettercount = 0
    
    for letters in word:
        lettercount += 1
    hiddenword = ' _ '*lettercount    
        
       
    return hiddenword
        


# In[3]:


#accept a valid guess
def player_choice():
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    guess = 'wrong'
    while guess not in alphabet:
        guess = input('Please enter your next guess: ')
        if guess not in alphabet:
            print('Sorry, invalid guess, please guess agiain')
        else:
            alphabet.remove(guess)
            return guess
        


# In[4]:


#compare guess against word, reveal letter or loose a life
def guess_check(word,guess,hiddenword):
    newhiddenword = hiddenword
    lettercount = 0
    
    for letter in word:
        if guess == letter:
            newhiddenword = hiddenword[:lettercount]+' '+guess+' '+hiddenword[lettercount+3:]
            lettercount += 3
            hiddenword = newhiddenword
        else:
            lettercount += 3
           
   
    return newhiddenword
        


# In[5]:


#compare hiddenword and newhiddenword, if same loose life

def loose_life(lives,hiddenword,newhiddenword):
    if hiddenword == newhiddenword:
        lives -= 1
        return lives
    else:
        return lives
    


# In[6]:


#check if won/out of lives, if not guess again
def win_check(newhiddenword,lives):
    playagain = False
    if ' _ ' not in newhiddenword:
        playagain = True
        print('Congratualations you win')
        return playagain
    elif lives == 0:
        playagain = True
        print ('You loose')
        return playagain
    else:
        pass
    
        
        


# In[7]:


#display hangman
def hangman(lives):
    
    head = '\n O '
    body = '\n O \n |'
    arms = '\n_O_\n |'
    legs = '\n_O_\n |\n''/ \ '
    crossbar = '  ___\n_O_\n |\n''/ \ '
    post = '  ___\n_O_  |\n |   |\n''/ \  |'
    baseplate = '  ___\n_O_  |\n |   |\n''/ \ _|_'

    hangman = ''
    
    if lives == 6:
        print(head)
    elif lives == 5:
        print(body)
    elif lives == 4:
        print(arms)
    elif lives == 3:
        print(legs)
    elif lives == 2:
        print(crossbar)
    elif lives == 1:
        print(post)
    elif lives == 0:
        print(baseplate)


# In[8]:


#ask player to replay
def replay(play):
    
    
    
    result = 'wrong'
    while result not in ['Y','N']: 
        result = input('would you like to play again, Y or N: ')
        if result == 'Y':
            play = True
            return play
        elif result == 'N':
            play = False
            return play
        else:
            print('\n'*100)
            print('Invalid choice, please pick again')


# In[9]:


#ask player if they are ready to play
def ready(play):

    
    
    result = 'wrong'
    while result not in ['Y','N']: 
        result = input('Welcome to hangman!!! \n\n\nA word will be selected at random. \nYou will then guess a letter. \nIf the guess is correct, the letter shall appear in the correct place. \nIf the guess is incorrect, you will loose a life. \nYou will begin the game with 7 lives. \nAre you ready to play? Y or N: ')
        if result == 'Y':
            play = True
            return play
        elif result == 'N':
            play = False
            return play
        else:
            print('\n'*100)
            print('Invalid choice, please pick again')


# In[ ]:


#The full program

play = False

#Set up the game- are they ready to play, while loop to run game in
play = ready(play)

while play == True:
   
    
    
    word = 'wrong'
    hiddenword = 'wrong'
    guess = 'wrong'
    lives = 7
    newhiddenword = 'wrong'
    playagain = False
    
    print('\n'*100)



    #randomly pick a word and display as hidden word
    
    word = word_pick()

    hiddenword = hide_word(word)
    
    #loop to keep playing while lives are over 0
    while lives >= 0:
        
        #display dahsed out word 
        print(hiddenword)
        
        
        #accept player guess
    
        guess = player_choice()
        
        #check if guess was correct and return the new dashed out word
        
        newhiddenword = guess_check(word,guess,hiddenword)
        print('\n'*100)
        print(newhiddenword)
        
        #if guess was incorrect take a life
        
        lives = loose_life(lives,hiddenword,newhiddenword)
        print(lives)
        print('\n'*100)
        
        #display hangman
        hangman(lives)
        
        
        #win/ loose check
        
        playagain = win_check(newhiddenword,lives)
        
        #check if game still on back to start of loop if it is
        
        
        
        if playagain == True:
            break
        else:
            hiddenword = newhiddenword
            
    #ask to play again if game off    
    play = replay(play)
    if play == True:
        print('\n'*100)

    else:
        break
            
                
        
        
        
        
        
        


    


# In[ ]:





# In[ ]:




