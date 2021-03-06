
#==================================================================================================================
#                                             2.5 Списки
#==================================================================================================================
'''
Напишите программу, на вход которой подается одна строка с целыми числами. Программа должна вывести сумму этих чисел.

Используйте метод split строки.
'''
def list_example_1():
    a = [int(i) for i in input().split()]
    s=0
    for i in a:
        s += i
    print (s)
    return 0
#==================================================================================================================
'''
Напишите программу, на вход которой подаётся список чисел одной строкой. 
Программа должна для каждого элемента этого списка вывести сумму двух его соседей. 
Для элементов списка, являющихся крайними, одним из соседей считается элемент, находящий на противоположном конце этого списка. 
Например, если на вход подаётся список "1 3 5 6 10", то на выход ожидается список "13 6 9 15 7" (без кавычек).

Если на вход пришло только одно число, надо вывести его же.

Вывод должен содержать одну строку с числами нового списка, разделёнными пробелом.
'''
def list_example_2():
    st = [int(i) for i in input().split()]
    for i in range(len(st)):
        if len(st)==1:
            print (st[i])
        elif i==(len(st)-1):
            print (st[i-1]+st[0])
        else:
            print (st[i-1]+st[i+1])
    return 0
#==================================================================================================================
'''
Напишите программу, которая принимает на вход список чисел в одной строке и выводит на экран в одну строку значения, 
которые встречаются в нём более одного раза.

Для решения задачи может пригодиться метод sort списка.

Выводимые числа не должны повторяться, порядок их вывода может быть произвольным.
'''
def list_example_3():
    st = [int(i) for i in input().split()]
    st.sort()
    x = st[0]
    i = 1
    l = len(st)
    while i<l:
        if st[i] == x:
            while st[i] == x and i<l-1:
                i += 1
            print (x,end=' ')
        x = st[i]
        i += 1
    return 0
#==================================================================================================================
#                                             2.6 Задачи по материалам раздела 2
#==================================================================================================================
'''
Напишите программу, на вход которой подаётся прямоугольная матрица в виде последовательности строк, 
заканчивающихся строкой, содержащей только строку "end" (без кавычек)

Программа должна вывести матрицу того же размера, у которой каждый элемент в позиции i, j равен сумме 
элементов первой матрицы на позициях (i-1, j), (i+1, j), (i, j-1), (i, j+1). У крайних символов соседний 
элемент находится с противоположной стороны матрицы.

В случае одной строки/столбца элемент сам себе является соседом по соответствующему направлению.
'''
def sec_26_1():
    j = 0
    k = 0
    a = []
    while j>=0:
        st = [i for i in input().split()]
        if st[0] == 'end':
            j = -1
        else:
#           for i in range(len(st)):
#               st[i] = int(st[i])
            st = [int(i) for i in st]
            a.append(st)
#           print (st)
#           print (a)
            j += 1
#   print (a)
    n = len(a)
    k = len(a[0])
    b = []
#   print (n,k)
    for i in range (n):
        c = []
        for j in range (k):
            x1 = i-1
            x2 = i+1
            y1 = j-1
            y2 = j+1
            if i == 0:
                x1 = n-1
            if i == n-1:
                x2 = 0
            if j == 0:
                y1 = k-1
            if j == k-1:
                y2 = 0
#           print (x1,x2,y1,y2)
#           c.append (a[x1][j]+a[x2][j]+a[i][y1]+a[i][y2])
            c += [a[x1][j]+a[x2][j]+a[i][y1]+a[i][y2]]
            print (c[j],end=' ')
        b.append (c)
        print ()
#   print (b)
    return 0
#==================================================================================================================

print('Списки. Примеры:')
print('1. Пример 1')
print('2. Пример 2')
print('3. Пример 3')
print('Задачи по разделу 2:')
print('4. Сумма соседних элементов матрицы')
print("\nВыберите пункт или нажмите любую буквенную клавишу для выхода...")

sec_26_1()
