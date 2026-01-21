#q1
def extract_firstwords(filename):
    firstwords_list=[]
    with open('sample.txt','r') as file:
        for line in file:
            words=line.split()
            if words:
                firstwords_list.append(words[0])
    return firstwords_list
result=extract_firstwords('sample.txt')
print(result)

#q2
def backup(a,b):
 with open('aa.txt','r') as f:
  with open('bb.txt','w') as f1:
   for line in f:
      f1.write(line)
 return "File backup completed successfully."
print(backup('a.txt','b.txt')) 

#q3
def analyze_file(filename):
 with open('story.txt','r') as file:
   for line_number,line in enumerate(file,start=1):
      words=line.split()
      wordcount=len(words)
      print(f'Line {line}:{wordcount} words')
print(analyze_file('story.txt'))

#q4
def linecount(filename):
    with open('story.txt','r') as file:
        line_count=0
        for line in file:
            line_count+=1
    return(f'Total number of lines:{line_count}')
print(linecount('story.txt'))
  
#q5
def filter(filename,filename1):
   with open('employees.txt','r') as f, open('management.txt','w') as f1:
      for line in f:
            if 'Python' in line:
                f1.write(line)
   return "Filtering complete."
print(filter("employees.txt","management.txt"))

#q6
def convert(filename,filename1):
    with open('numbers.txt', 'r') as f, open('squared.txt', 'w') as f1:
        for line in f:
            if line.strip():
                number = int(line.strip())
                squared_number = number ** 2
                f1.write(str(squared_number) + '\n')
    return "Calculation complete."
print(convert("numbers.txt","squared.txt"))

#q7
def message(filename):
    user_message = input("Enter the message you want to log: ")
    with open('history.log', 'a') as file:
        file.write(user_message + '\n')
    return "Message successfully added."
print(message("history.log"))

#q8
def cpaitalized(filename1,filename2):
    with open('input.txt', 'r') as infile, open('output.txt', 'w') as outfile:
        for line in infile:
            capitalized_line = line.upper()
            outfile.write(capitalized_line)
    return "Conversion complete."
print(cpaitalized("input.txt","output.txt"))