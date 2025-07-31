#Homework 
#Threaded Prime Number Checker
import threading
def prime_check1():
    primes=[]
    for i in range(1,51):
        if i<=1:
            continue
        if i==2:
            primes.append(i)
        if i%2==0:
            continue
        is_prime = True
        for x in range(3, int(i**0.5)+1,2):
            if i%x==0:
                is_prime=False
                break
        if is_prime:
            primes.append(i)
    print( primes)

range1 = range(1,50)
range2=range(50, 101)


def prime_check2():
    primes=[]
    for i in range(50,101):
        if i<=1:
            continue
        if i==2:
            primes.append(i)
        if i%2==0:
            continue
        is_prime = True
        for x in range(3, int(i**0.5)+1,2):
            if i%x==0:
                is_prime=False
                break
        if is_prime:
            primes.append(i)
    print( primes)
 
thread1 = threading.Thread(target=prime_check1)
thread2 = threading.Thread(target=prime_check2)

thread1.start()
thread2.start()

#Exercise 2: Threaded File Processing
import threading
def count_words(word_list, result_dict, lock):
    local_count = {}
    for word in word_list:
        if word != '':
            word = word.lower()
            if word not in local_count:
                local_count[word] = 1
            else:
                local_count[word] += 1
    with lock:
        for word, count in local_count.items():
            if word in result_dict:
                result_dict[word] += count
            else:
                result_dict[word] = count

def split_list(lst, num_parts):
    chunk_size = len(lst) // num_parts
    chunks = []
    for i in range(num_parts):
        start = i * chunk_size
        end = (i + 1) * chunk_size if i < num_parts - 1 else len(lst)
        chunks.append(lst[start:end])
    return chunks
with open("msg.txt") as f:
    data = f.read()
symbols = [',','.','*','-',':','?',';','!']
for i in symbols:
    data = data.replace(i,'')
data = data.replace('\n',' ')
words = data.split(' ')
result = {}
lock = threading.Lock()
num_threads = 4
chunks = split_list(words, num_threads)
threads = []
for chunk in chunks:
    t = threading.Thread(target=count_words, args=(chunk, result, lock))
    t.start()
    threads.append(t)
for t in threads:
    t.join()
print(result)
