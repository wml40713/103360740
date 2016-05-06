from Node import UnorderedList
u = UnorderedList()

u.add('30')
u.add('45')
u.add('67')
print (u.size())
print (u.search('45'))
print (u.search('53'))
print (u.isEmpty())
u.remove('30')
print (u.size())
u.append('83')
print (u.size())
u.insert(1, '21')
print (u.index('356'))
print (u.pop(1))
print (u.pop())
print (u.isEmpty())



