# https://www.hackerrank.com/challenges/three-month-preparation-kit-camel-case/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-one
# Enter your code here. Read input from STDIN. Print output to STDOUT

def changeform(line):
    sc=line[0]
    tp=line[2]
    name=line[4:]
    
    ord_a=ord('a')
    ord_z=ord('z')
    ord_A=ord('A')
    ord_ZZ=ord('Z')
    if sc=='S':
        if tp=='M':
            name=name[:-2]
            # insert ' '
        n=len(name)
        for i in reversed(range(1,n)):
            chrord=ord(name[i])
            if ord_A<=chrord and chrord<=ord_ZZ:
                name=name[:i]+' '+name[i:]
        name=name.lower()
    elif sc=='C':
        wrd=name.split(' ')
        for i in range(1,len(wrd)):
            wrd[i]=wrd[i][0:1].upper()+wrd[i][1:]
        
        if tp=='M': # ()
            wrd[-1] += "()"
        if tp=='C': # first one
            wrd[0]=wrd[0][0:1].upper()+wrd[0][1:]
        
        name="".join(wrd)
    return name

    
while True:
    try:
        line=input()
        print(changeform(line))
    except EOFError:
        break
