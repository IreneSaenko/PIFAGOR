from django.shortcuts import render
from CntPif.models import Pifs, Numbers


def first(request):#запускает страницу с селектором

     if 'Sudba/' in request.path:
        name = 'Расчёт числа судьбы по дате рождения:'
     else:
        name = 'Расчёт психоматрицы по дате рождения (Квадрат Пифагора):'
     return render(request, 'CntPif/table.html', {'name': name})

def sudba(request):

    d = int(request.POST['Day'])
    m = int(request.POST['Month'])
    y = int(request.POST['Year'])
    sum = 0
    if (d>=10) and (d!=11) and (d!=22):
         d=d%10+d//10
    if (m>=10) and (m!=11) and (m!=22):
         m=m%10+m//10
    t=0
    while y!=0:
          t+=y%10
          y=y//10
    if (t >= 10) and (t != 11) and (t != 22):
        t = t % 10 + t // 10
    sum =t+m+d
    if (sum >= 10) and (sum != 11) and (sum != 22):
        sum = sum % 10 + sum // 10
    sum = str(sum)
    res = Numbers.objects.get(name=sum)
    return render(request, 'CntPif/Sudba.html', {'res': res})

def second(request):#рассчитывает психоматрицу и переходит 
#на страницу результата
    d = request.POST['Day']
    m = request.POST['Month']
    y = request.POST['Year']
    s = ''
    s = s+d+m+y
    first = 0
    lst =[0 for i in range(9)]
    for i in range(len(s)):
    		first+=int(s[i])
    		if int(s[i])!=0:
    		   lst[int(s[i])-1]=lst[int(s[i])-1]+1
    if first>=10:
    		second=first%10+first//10
    else:
            second=first
    
    therd=first-2*int(d[0])
    if therd>=10:
            forth=therd%10+therd//10
    else:
    	    forth=therd
    for j in [first, second, therd, forth]:
    	    if j>=10:
    	       c=j%10
    	       k=j//10
    	       if c!=0:
    	           lst[c-1]=lst[c-1]+1
    	       if k!=0:
    	           lst[k-1]=lst[k-1]+1
    	    else:
    	    	lst[j-1]=lst[j-1]+1
    res = []
    res.append(Pifs.objects.get(number=lst[0]).one)
    res.append(Pifs.objects.get(number=lst[1]).two)
    res.append(Pifs.objects.get(number=lst[2]).three)
    res.append(Pifs.objects.get(number=lst[3]).four)
    res.append(Pifs.objects.get(number=lst[4]).five)
    res.append(Pifs.objects.get(number=lst[5]).six)
    res.append(Pifs.objects.get(number=lst[6]).seven)
    res.append(Pifs.objects.get(number=lst[7]).eight)
    res.append(Pifs.objects.get(number=lst[8]).nine)
    lst1 = []
    for i in range(len(lst)):
        s=''
        if lst[i]!=0:
           for j in range(lst[i]):
                  s+=str(i+1)
           lst1.append(s)
        else:
           lst1.append('-')

    context = {'lst1': lst1, 'res': res}
    return render(request, 'CntPif/Date.html', context)
   
def menu(request):
    return render(request, 'CntPif/Menu.html')
