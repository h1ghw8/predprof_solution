def first_task():
    list=[]
    with open('magical.csv','r', encoding='utf-8') as file:
        header=file.readline().strip().split(',')
        for l in file.readlines():
            s=l.strip().split(',')
            poison=s[0]
            count=int(s[1])
            if count==-1:
                count=0    
            flag=0
            for i in range(len(list)):
                if list[i][0]==poison:
                    flag+=1
                    list[i][1]+=count
            if flag==0:
                list.append([poison, count])
    
    with open('magicalPotions1.txt', 'w', newline='') as newfile:

        for x in range(len(list)):
             newfile.write(f'{list[x][0]} в запасах еще есть - {list[x][1]}'+'\n')
    for k in list:
        if k[0]=='Мощное Зелье':
            print(f'Данного зелья осталось - {k[1]}')

def quicksort(alist, start, end):
    '''Sorts the list from indexes start to end - 1 inclusive.'''
    i = start
    j = end-1
    pivot = alist[(start+end)//2][1]
    
    while True:
        while alist[i][1] < pivot:
            i = i + 1 
        while alist[j][1] > pivot:
            j = j - 1     
        if i < j:
            alist[i], alist[j] = alist[j], alist[i]
            i = i + 1
            j = j - 1
        else:
            break
    
    if start < j:
        quicksort(alist,start,j)
    if i < end-1:
        quicksort(alist,i,end)
def second_task():
    list=[]
    with open('magicalPotions1.txt','r') as file:
        for l in file.readlines():
            for i in range(len(l)):
                if l[i]=='-':
                    count=int(l[i+2:])
                    break
            list.append([l,count])
    quicksort(list, 0, len(list))
    for i in range(5):
        print(*list[i][0])
def third_task():
    list=[]
    with open('magical.csv','r', encoding='utf-8') as file:
        header=file.readline().strip().split(',')
        for l in file.readlines():
            s=l.strip().split(',')
            list.append([s[4], s[0], s[1]])
    
    while True:
        n=input()
        if n=='стоп':
            break
        f=0
        for j in list:
            if j[0]==n:
                print(f'По вашему запросу {j[0]} найден следующий вариант:\n{j[0]} используется в {j[1]}, его количество составляет : {j[2]}')
                f+=1
        if f==0:
            print('Такую траву мы не используем')

def fourth_task():
    list=[]
    with open('magicalPotions1.txt','r') as file:
        for l in file.readlines():
            l=l.split(' ')
            if l[2]=='в':
                    clas=l[1]
            else:
                    clas=l[1]+' '+l[2]
            summ=int(l[-1])
            flag=0
            for i in range(len(list)):
                if list[i][0]==clas:
                    flag+=1
                    list[i][1]+=summ
                    list[i][2]+=1

            if flag==0:
                list.append([clas, summ, 1])
    for x in list:
        print(f'{x[2]} зелий класса {x[0]}, общее количество зелий {x[1]}')
def hash(x):
    h=0
    with open('magical.csv','r', encoding='utf-8') as file:
        header=file.readline().strip().split(',')
        for l in file.readlines():
            s=l.strip().split(',')
            for i in range(2,5):
                if s[i]==x:
                    h+=1
    return(h)
def fifth_task():
    list=[]
    with open('magical.csv','r', encoding='utf-8') as file:
        header=file.readline().strip().split(',')
        for l in file.readlines():
            s=l.strip().split(',')
            
            for x in range(2,5):
                flag=0
                for i in range(len(list)):
                    if list[i][0]==s[x]:
                        flag+=1
                if flag==0:
                    list.append([s[x], hash(s[x])])
    for i in range(1, len(list)):
        j = i
        while (j > 0 and list[j][1] < list[j-1][1]):
            list[j], list[j-1] = list[j-1], list[j]
            j = j - 1
    for i in range(5):
        print(f'{list[len(list)-1-i][0]} - {list[len(list)-1-i][1]}')
'''first_task()
second_task()
third_task()
fourth_task()'''
fifth_task()

