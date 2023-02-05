file = open('file_test.txt' ,'w')  # a 는 뒤에 추가하는 append 가 됨
file.write('조중혁이다' )
file.close()


##############################################################################


file = open('file_test.txt' ,'r')  # a 는 뒤에 추가하는 append 가 됨
data=file.read()
print(data)
file.close()



##############################################################################
