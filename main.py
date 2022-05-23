out = open("output.txt", "w")

def first_fit(mem,pro):
    global out
    out.write("First-Fit Memory Allocation\n\n")
    out.write("------------------------------------\n\n")
    out.write("start =>")
    for i in mem:
        out.write(" "+str(i))
    out.write("\n\n")
    for i in range(0,len(pro)):
        kontrol=False
        for j in range(0,len(mem)):
            if(mem[j]>pro[i]):
                kontrol=True
                mem.append(-1)
                mem[j+1:len(mem)]=mem[j:len(mem)-1]
                mem[j+1]=mem[j]-pro[i]
                mem[j]=-1*pro[i]
                out.write(str(pro[i])+" =>")
                for i in mem:
                    if i < 0:
                        out.write(" "+str((-1*i))+"*")
                    elif i==0:
                        continue
                    else:
                        out.write(" "+str(i))
                out.write("\n\n")
                break
        if kontrol==False:
            out.write(str(pro[i])+" => not allocated, must wait")
            out.write("\n\n")


def best_fit(mem,pro):
    global out
    out.write("Best-Fit Memory Allocation\n\n")
    out.write("------------------------------------\n\n")
    out.write("start =>")
    for i in mem:
        out.write(" "+str(i))
    out.write("\n\n")
    for i in range(0,len(pro)):
        fark=100000
        index=-1
        for j in range(0,len(mem)):
            islem=mem[j]-pro[i]
            if islem >= 0 and islem<fark:
                fark=islem
                index=j
        if index==-1:
            out.write(str(pro[i])+" => not allocated, must wait")
            out.write("\n\n")
            continue
        mem.append(-1)
        mem[index+1:len(mem)]=mem[index:len(mem)-1]
        mem[index+1]=mem[index]-pro[i]
        mem[index]=-1*pro[i]
        out.write(str(pro[i])+" =>")
        for i in mem:
            if i < 0:
                out.write(" "+str((-1*i))+"*")
            elif i ==0:
                continue
            else:
                out.write(" "+str(i))
        out.write("\n\n") 
def worst_fit(mem,pro):
    global out
    out.write("Worst-Fit Memory Allocation\n\n")
    out.write("------------------------------------\n\n")
    out.write("start =>")
    for i in mem:
        out.write(" "+str(i))
    out.write("\n\n")
    for i in range(0,len(pro)):
        fark=0
        index=-1
        for j in range(0,len(mem)):
            islem=mem[j]-pro[i]
            if islem >= 0 and islem>fark:
                fark=islem
                index=j
        if index==-1:
            out.write(str(pro[i])+" => not allocated, must wait")
            out.write("\n\n")
            continue
        mem.append(-1)
        mem[index+1:len(mem)]=mem[index:len(mem)-1]
        mem[index+1]=mem[index]-pro[i]
        mem[index]=-1*pro[i]
        out.write(str(pro[i])+" =>")
        for i in mem:
            if i < 0:
                out.write(" "+str((-1*i))+"*")
            elif i ==0:
                continue
            else:
                out.write(" "+str(i))
        out.write("\n\n") 
f = open("input.txt", "r")
memory=f.readline()
process=f.readline()
f.close()
memory=memory.replace("\n","")
process=process.replace("\n","")
print(memory)
print(process)
memories=memory.split(",")
processes=process.split(",")
print(memories)
print(processes)
for i in range(0,len(memories)):
    memories[i]=int(memories[i])
for i in range(0,len(processes)):
    processes[i]=int(processes[i])
orjmem=[]
orjmem[:]=memories
first_fit(memories,processes)
memories[:]=orjmem
best_fit(memories,processes)
memories[:]=orjmem
worst_fit(memories,processes)