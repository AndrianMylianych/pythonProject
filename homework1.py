# task 1.1

#list1 = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]

# print(min(list1))

# or

# list1.sort()
# list1 = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]
#
# print(list1[:1])

# task 1.2

# noDup = []

# [noDup.append(x) for x in list1 if x not in noDup]

# print(noDup)

# or

# noDup = []

# for x in list1:
#    if x not in noDup:
#        noDup.append(x)

# print(noDup)

# task 1.3

#list2 = list1.copy()
#for i in range(3, len(list2), 4):
#    list2[i] = 'X'
#    print(list2)

# task 2

#x = int(input('how many "*" you want?'))
#i = x
#while i >= 1:
#    if i == x or i == 1:
#        j = x
#        while j > 0:
#            print('*', end='')
#            j -= 1
#        print()
#    else:
#        j = x - 2
 #       print('*', end='')
 #       while j > 0:
 #           print(' ', end='')
  #          j -= 1
  #      print('*')
 #   i -= 1

# task 3

#i = 1
#size = 10
#while i <= size:
#    j = 1
#    while j <= size:
#        res = i * j
#        if res // 10:
#            print(res, end='  ')
#        else:
#            print(res, end='   ')
#        j += 1
#    print()
#    i += 1


# task 4

list1 = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]

while True:
    print('1. find min value in list1')
    print('2. delete every repeated value')
    print('3. change every 4th value to "X"')
    print('4. find the element of list1, which is the closest one to average value of all item in list1')
    print('5. exit')

    choose = input('choose an option: ')

    if choose not in '12345':
        continue

    elif choose == '1':
        print(min(list1))

    elif choose == '2':
        noDup = []

        for x in list1:
            if x not in noDup:
                noDup.append(x)

        print(noDup)

    elif choose == '3':
        list2 = list1.copy()

        for i in range(3, len(list2), 4):
            list2[i] = 'X'
            print(list2)

    elif choose == '4':
        print('List =', list1)
        list1.sort()
        sum = 0
        for i in list1:
            sum += i
        avg = sum / len(list1)

        candidates = []

        for i in range(len(list1)):
            if list1[i] > avg:
                candidates.append(list1[i])
                candidates.append(list1[i - 1])
                break
        print("Avg =", avg)

        if not len(candidates):
            print('result:', avg)
        else:
            print('result = ', candidates[0] if avg > (candidates[0] + candidates[1]) / 2 else candidates[1])

    elif choose == '5':
        break

