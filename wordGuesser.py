import random
word_list = [
    'rizz', 'sus', 'yeet', 'skibidi', 'fanum', 'gyatt', 'sigma',
    'goofy', 'slay', 'bussin', 'cap', 'noCap', 'drip', 'lit',
    'vibe', 'bet', 'mood', 'lowkey', 'highkey', 'oop', 'bruh',
    'yap', 'shook', 'flex', 'simp', 'based', 'mid', 'ratio',
    'delulu', 'griddy', 'aura', 'gyal', 'yolo', 'fam', 'snacc',
    'pookie', 'aight', 'chad', 'goat', 'nerf', 'buff', 'pog',
    'uwu', 'karen', 'slaps', 'salty', 'cringe', 'zesty', 'fire',
    'sheesh', 'periodt', 'okurrr', 'woke', 'npc', 'mainChar',
    'suspect', 'toxic', 'vibez', 'drippy', 'ratioed', 'sturdy'
]
word_chosen = random.choice(word_list)
guessWord = ['_'] * len(word_chosen)
attempts = 10  

while attempts>0:
    print('\nCurrent Word: ' + ' '.join(guessWord))

    guess = input('Guess a letter: ').strip().lower()

    if guess in word_chosen:
        for i in range(len(word_chosen)):
            if word_chosen[i] == guess:
                guessWord[i] = guess
        print('Great Guess!')
    else:
        attempts -=1
        print('Wrong Guess! Attempts left: ' + str(attempts))
    if '_' not in guessWord:
        print('\nCongratulations!! You guessed the word: ' + word_chosen)
        break
if '_' not in guessWord or attempts == 0:
    print('\nYou\'ve run out of attempts! The word was: ' + word_chosen)






    