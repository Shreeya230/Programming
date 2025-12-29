#question1
word=input('Enter the word:')
vowel=set()
for i in word:
   if i in 'aeiou':
        vowel.add(i)
print(vowel)

#question2
operation=int(input('Enter how many operation you want to perform:'))
dictionary={}
for i in range(1,operation+1):
    choice=int(input('Press 1.add 2.display 3.remove 4.exit:'))
    if choice==1:
       word=input('Enter a word:')
       if word in dictionary:
                print(f'{word} already exist.')
       else:
                meaning=input('Enter a meaning of that given word:')
                dictionary[word]=meaning
    elif choice==2:
       for i,j in sorted(dictionary.items()):
           print(f'{i} {j}')
    elif choice==3:
        word=input('Enter a word you want to remove:')
        if word not in dictionary:
            print(f'{word} doesnt exists')
        else:
            dictionary.pop(word)
    elif choice==4:
        break 

#question3
quiz_questions={
    '1':{
       'question':'Which of the following character comments in Python','options':{'a':'#', 'b':'//', 'c':'/', 'd':'!'}, 'correct_answer':'a'
    },
    '2':{
        'question':'Which of the following statements is used to create an empty set in python?','options':{'a':'()', 'b':'[]', 'c':'{ }', 'd':'set()'},
        'correct_answer':'d'
    },
    '3':{
        'question':'Which method is used to add an element to a list?','options':{'a':'add()', 'b':'addList()', 'c':'update()', 'd':'append()'},
        'correct_answer':'d'
    }
}
score=0
for i,j in quiz_questions.items():
    print(i,' ',j['question'])
    for key,value in j['options'].items():
       print(key,' ',value)
    choice=input('Choose the correct option:')
    if choice==j['correct_answer']:
       score+=1
    print(score)

#question4
items=int(input('Enter the total number of items you purchased:'))
prices=[]
for i in range(1,items+1):
    item=float(input(f'Enter the price of item {i}:'))
    prices.append(item)
total_cost=sum(prices)
print("Total cost of all items is:", total_cost)

#question5
sentence=input('Enter a full sentence:')
words=sentence.split()
total_word=len(words)
sets=set()
for word in words:
   sets.add(word.lower())
total_count=len(sets)
print(f'Total number of words {total_word}')
print(f'The number of unique words found is {total_count} ')

#question6 
sentence=input('Enter the sentence:')
words=sentence.split()
dictionary={}
for word in words:
    word=word.lower()
    dictionary[word]=dictionary.get(word, 0)+1
for word in sorted(dictionary):
    print(word,':',dictionary[word])
