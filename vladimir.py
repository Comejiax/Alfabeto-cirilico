'''А ="a"
Б ="be"
В ="ve"
Г ="gue"
Д ="de"
Е ="ie"
Ё ="io"
Ж ="zhe"
З ="ze"
И ="i"
Й ="ik"
К ="ka"
Л ="el"
М ="em"
Н ="en"
О ="o"
П ="pe"
Р ="er"
С ="es"
Т ="te"
У ="u"
Ф ="ef"
Х ="ja"
Ц ="tse"
Ч ="che"
Ш ="she"
Щ ="shia"
Ъ =""
Ы ="y"
Ь =""
Э ="e"
Ю ="iu"
Я ="ia"'''

import random



ruso=["А","Б" ,"В","Г","Д","Е","Ё","Ж","З","И","Й","К","Л","М","Н","О","П","Р","С","Т","У","Ф","Х","Ц","Ч","Ш","Щ","Ы","Э","Ю","Я"]
pronunciacion=["a","be","ve","gue","de","ie","io","zhe","ze","i","ik","ka","el","em","en","o","pe","er","es","te","u","ef","ja","tse","che","she","shia","y","e","iu","ia"]
print(ruso.index("Я"));
print(pronunciacion.index("ia"));
def rusito():

    numero_random = random.randint(0,30);
    abc=ruso[numero_random]
    pc=pronunciacion[numero_random]
    print(numero_random);
    print(abc);
    idk2=True;
    intentos = 0;
    
    #r=input("Cómo se pronuncia esa letra " + abc + ": ");
    while idk2:
        intentos+=1;
        r=input("Cómo se pronuncia esa letra " + abc + ": ");
        if r == pc:
            print(f"Correcto, le atinaste a la {intentos} vez");
            idk2=False;
        else:
            #a=True;
            print("No, intenta de nuevo.");
            
            
xd = True;
while xd:
    rusito();

