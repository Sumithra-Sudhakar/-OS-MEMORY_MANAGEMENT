block_size=[]
process_size=[]
p_num=int(input("number of processes"))
b_num=int(input("number of blocks"))
print("enter the memory requirement for each process")
for i in range(p_num):
  a=int(input())
  process_size.append(a)
print("enter the block size for each block")
for i in range(b_num):
  a=int(input())
  block_size.append(a)

def first_fit():
  for i in process_size:
    for j in block_size:
      if i<j:
     
        print("process",end=" ")
        print(process_size.index(i)+1,end=" ")
        print("is allocated to block",end=" ")
        print(block_size.index(j)+1)
        j-=i
        break
def best_fit():
 
  index=0
  found=0
  for i in process_size:
    d=1000
    for j in block_size:
      if i<=j:
        found=1
        diff=j-i
        if diff <d:
          d=diff
          index = block_size.index(j)
        
    if found==1:  
      
      print("process",end=" ")
      print(process_size.index(i)+1,end=" ")
      print("is allocated to block",end=" ")
      print(index+1)
      block_size[index]-=i
    
def worst_fit():
  index='x'
  found=0
  for i in process_size:
     
      m=max(block_size)
      if m>=i:
        index = block_size.index(m)
        found=1
        print("process",end=" ")
        print(process_size.index(i)+1,end=" ")
        print("is allocated to block",end=" ")
        print(index+1)
        block_size.remove(m)
      
      if found==0:
        print("process",end=" ")
        print(process_size.index(i)+1,end=" ")
        print("is allocated to block",end=" ")
        print(index)

        
        
print("enter the option ")
print("1. first fit ")
print("2. best fit")
print("3. worst fit")
opt=int(input())
if opt==1:
  first_fit()
elif opt==2:
  best_fit()
elif opt==3:
  worst_fit()
else:
  print("invalid option")

 