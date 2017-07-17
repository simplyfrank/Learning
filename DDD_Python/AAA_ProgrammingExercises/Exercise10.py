# a = [1, 11, 21, 1211, 111221

# b = [1, 11, 21, 1211, 111221, 312211, 13112221, 1113213211, 31131211131221]


def conway_folge(start, limit, count=0):
    numberString = str(start[-1])
    print('Starting the run with {}'.format(numberString))
    result = ''
    last = numberString[0]
    count_current = 0
    for idx,s in enumerate(numberString):
        if s == last:
            print('found an other {}, adding it up'.format(s))
            count_current += 1
            print('We have counted {}, {}s'.format(count_current, s))
        elif int(s) != last:
            print('breaking with a count of {}, {}s'.format(count_current,last))
            result += str(count_current) + str(last)
            last = str(s)
            count_current = 1
            print('We continue with round {} with {}s, at a count of {}'.format(idx, s, count_current))
        
        # When the list has been passed trough
        if idx + 1 == len(numberString):
            result += str(count_current) + str(last)
            print('FINISH: {}'.format(result))

            # See if we reached the limit for the 
            if count == limit:
                print('DONE:::: We completed {} out of {} rounds of calculation'.format(count, limit))
                break
            start.append(result)
            conway_folge(start, limit=limit, count = count + 1)


    return start

results = conway_folge([1], limit=30)
print(len(results[-1]))    

# Answer
"http://www.pythonchallenge.com/pc/return/5808.html"
        
        
