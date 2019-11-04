#string declaration ways
a='anirudh dua'
b=' ' 'anirudh dua' ' '
c="anirudh dua"
d=" " "anirudh dua" " "
#print('a:',a,'\nb:',b,'\nc:',c,'\nd',d)

#skiping special characters
st=' my name is \'anirudh dua\' '#using \ to skip the special characters
#print(st)
rt=r"my name is 'anirudh dua' "#usning r to declare th string as a raw string
#print(rt)


#multine  string
#way 1
mt1="my name is \'anirudh dua\' \
i love to code "#using \ in  last of every line
#print(mt)

#way 2
mt2="""my name is \'anirudh dua\' 
i love to code """#or use """ """
#print(mt2)

#way3
mt3=('my name  is anirudh dua'
' python is easy  ')#using (''   '')
#print(mt3)


#ACCESSING STRING ELEMENTS
name='anirudh'
'''print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])
print(name[6])
print(name[-0])
print(name[-1])
print(name[-2])
print(name[-3])
print(name[-4])
print(name[-5])
print(name[-6])'''

#STRING SLICING

rudh=name[3:7]#start to end-1
#print(rudh)#gives out rudh
fullm1=name[:-1]#start to end-1
#print(full)#gives the full string
full=name[0:]#from start to end
#print(full)
ful=name[:7]#from start to end -1
#print(ful)
fulll=name[-0:]#-start included to end
#print(fulll)
fuulll=name[:-1]# from begin to -end-1
#print(fuulll)


#STRING PROPERTIES
nam='dua'
#print(type(nam))#shows that all string are object of  class type str
#nam[0]='m'#string are immutable  whereas name can be assigned new value
fullname=name+nam#conatenation
#print(fullname)


#STRING OPREATIONS

string='anir9639'
'''print(string.isalpha())#check for all are alphabets or not
print(string.isdigit())#check for all are numbers or not
print(string.isalnum())#check for alphanumeric or  not
print(string.islower())#check for all are lower or not
print(string.isupper())#check for all are upper or not
print(string.startswith('a'))#check for if the string start with a particular value or not
print(string.endswith('9'))#check for if the string ends with a particular value or not'''

#STRING CONVERSION
myname='ANIrudh'
#print(myname.upper())
#print(myname.lower())
#print(myname.capitalize())
#print(myname.swapcase())

#SEARCH AND REPLACE
#print(myname.find('h'))
#print(myname.replace('AN','SN'))
#print(ord('A'))#gives the unicode
#print(chr(65))#gives the char word ascii equivalent of 65


