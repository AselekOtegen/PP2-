#EXAMPLE1
'''import re
file = open('row.txt', 'r', encoding='utf-8')
data = file.read()
word = r'ab*'
www = re.findall(word, data)
for i in www:
    print(i)'''
#EXAMPLE2
'''import re
file = open('row.txt', 'r', encoding = 'utf-8')
data = file.read()
word = r'ab{2,3}?'
www = re.findall(word,data)
for i in www:
    print(i)'''
#EXAMPLE3
'''import re

file = open('row.txt', 'r', encoding='utf-8')
data = file.read()
word_pattern = r'\b[a-z]+_[a-z]+\b'
matches = re.findall(word_pattern, data)
for i in matches:
    print(i)'''
#EXAMPLE4
'''import re
file = open('row.txt', 'r', encoding='utf-8')
data = file.read()
word_pattern = r'\b[A-Z][a-z]+\b'
matches = re.findall(word_pattern, data)
for i in matches:
    print(i)'''

#EXAMPLE5
'''import re
file = open('row.txt', 'r', encoding='utf-8')
data = file.read()
pattern = r'a.*b$'
matches = re.findall(pattern, data)
for i in matches:
    print(i)'''
#EXAMPLE6
'''import re
file = open('row.txt', 'r', encoding='utf-8')
data = file.read()
pattern = r'[ ,.]'
repl = re.sub(pattern, ':', data)

print(repl)'''

#EXAMPLE7
'''import re
file = open('row.txt', 'r', encoding='utf-8')
data = file.read()
words = data.split('_')
camel_case_string = words[0] + ''.join(word.capitalize() for word in words[1:])
print(camel_case_string)'''

#EXAMPLE8
'''import re
file = open('row.txt', 'r', encoding='utf-8')
data = file.read()
pattern = r'[A-Z][^A-Z]*'
matches = re.findall(pattern, data)
for i in matches:
    print(i)
'''
#EXAMPLE9
'''import re
file = open('row.txt', 'r', encoding='utf-8')
data = file.read()
def capital(data):
    return re.sub(r"(\w)([A-Z])", r"\1 \2", data)
result = capital(data)
print(result)'''
#EXAMPLE10

'''import re
file = open('row.txt', 'r', encoding='utf-8')
data = file.read()
def camel_to_snake(str):
        str = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', data)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', str).lower()
result = camel_to_snake(data)
print(result)

'''