#create class group
class Group:
    namegroup = ''
    member = []
    
    def setNameMember(self,name):
        self.namegroup = name
        
    def addMember(self,member):
        self.member.append(member)

#initialization group as p1
p1 = Group()

#set name group and member
p1.setNameMember('kelompok 1')
p1.addMember('fajar')
p1.addMember('randy')
p1.addMember('aya')
p1.addMember('ici')

#print namegroup and member
print(p1.namegroup,' : ',p1.member)