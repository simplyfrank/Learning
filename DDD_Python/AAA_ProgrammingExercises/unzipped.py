import re
import zipfile

f = zipfile.ZipFile("data/channel.zip")

# idx = 90052

# while True:
#     f = open('{}.txt'.format(idx), 'r')
#     text = f.read()
#     print(text)
#     res = re.search('Next nothing is ', text)
#     if res:
#         res = res.start()
#         idx = text[res+16:]
#         print(idx)
#     else:
#         print('Finished')
#         break



# Second Step
num = '90052'

comments = []
while True:
    content = f.read(num+'.txt').decode('utf-8')
    comments.append(f.getinfo(num+".txt").comment.decode('utf-8'))
    res = re.search('Next nothing is (\d+)', content)
    print(content)
    if res:
        num = res.group(1)
    else:
        comments = ''.join(comments)
        break

print(comments)






        
