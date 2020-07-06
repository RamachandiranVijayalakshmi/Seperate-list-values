def seperatelist(a):
    print('original list:',a)
    First=a[0:3]
    second=a[3:6]
    third=a[6:9]
    print('First List is:',First)
    print('First List Revers List is:',First[::-1])
    print('Second List is:',second)
    print('Second List Revers List is:',second[::-1])
    print('Third List is:',third)
    print('Third List Revers List is:',third[::-1])
sampleList=[11, 45, 8, 23, 14, 12, 78, 45, 89]
seperatelist(sampleList)