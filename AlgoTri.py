##triFusion##

list=[6,4,5,2,1,3,8,9,7]
def triFusion(list):
  i=len(list)
  if i<2:
    return list
  else:
    y=i//2
    return Fusion (triFusion(list[:y])),triFusion(list[y:])
print(triFusion(list))

list1=(triFusion(list[:y]))
list2=(triFusion(list[y:]))

def Fusion(list1,list2):
  result=[]
  j=0
  for i in list1:
    while i < list2:
      result.append (list2[j])
    else:
      result.append (list1[i])
  return Fusion
  
print(Fusion(list))

##triSelectif##

list=[4,3,8,7,1,2,9,5,6]
def tri_selection(list):
    for i in range(len(list)):
        min = i
        for j in range(i+1, len(list)):
            if list[min] > list[j]:
                min = j
    tmp = list[i]
    list[i] = list[min]
    list[min] = tmp
    return list
print (tri_selection(list))
