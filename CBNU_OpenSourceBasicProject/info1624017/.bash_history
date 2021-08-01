passwd
exit
passwd
pwd
passwd
#pwunconv
passwd
/etc
/bin
ls
/etc/passwd
/home/info1
ls
ls -l
ls -la
cd /
cd
ls
cd home
ls
pwd
ls -i
ls -l
ls -d
cat helloWorld.c
ls
cat helloWorld.c
cat > testfile
chmod absolute-mode file
vi testfile
cat helloWorld.c
cat > helloWorld.c
cc helloWorld.c
a.out
vi helloWorld.c
cat helloWorld.c
cc helloWorld.c
a.out
./a.out
exit
passwd
ls -l
cd test
ls -l
vim
cd -
cd test
cd -
cd test1
ls
ls -l
cd
rm -ri test1
cd test2
ls
cd
mv test2 test
ls
mkdir week04
touch practice01
vim practice01
ls
mv practice01 week04
cd week04
ls
vim practice01
touch practice02
vim practice02
touch practice03
vim practice03
cc practice01
mv practice01 practice01.c
cc practice01.c
ls
cat practice01.c
vim practice01.c
cc practice01.c
ls
gcc practice01.c
ls -l
vim practice02
cat practice01.c
cat practice02
mv practice02 practice02.c
gcc practice02.c
mv practice03 practice03.c
ls -l
vim practice03.c
c d-
cd -
ls
cat sortData
cp sortData week04
cd week04
cc -o sortData practice01.c
ls
./practice01.c
./sortData
cat sortData
clear
./sortData < practice01.c
./sortData < practice01.c > result
cc practice01.c
vim practice01.c
cc practice01.c
ls
cat result
rm result
rm sortData
ls -l
cat practice01.c
gcc practice01.c -o a
ls
cat practice01.c
gcc practice01.c -std=c99 a
gcc -std=c99 practice01.
ls
touch test.c
vim test.c
gcc practice01.c
gcc test.c
ls
vim test.c
gcc test.c
ls
./a.out
ls
cat test.c
a.out
./a.out
gcc test.c -o result
./result
ls
rm a.out
ls
rm practice01.c
mv test.c practice01.c
rm result
gcc practice01.c -o practice01
ls
vim practice02.c
gcc practice02.c -o practice02
./practice02
ls
vim practice03.c
gcc practice03.c
./practice03
rm a.out
gcc practice03.c -o practice03
./practice03
ls
c
cd
ls
mkdir week03
cp test week03
cd -r test week03
cp -r test week03
cd week03
ls
cd test
ls
mv helloWorld.c large memo memo2 sumM2N.c test.c testfile week03
mv helloWorld.c large memo memo2 sumM2N.c test.c testfile ~
./
cd week03
cd ../week03
cd ./week03
cd
cd week03
ls
cd
ls
mv helloWorld.c memo result sortsumM2N.c test.c memo2 large week03
mv helloWorld.c memo result sumM2N.c test.c memo2 large week03
ls
cd week03
ls
rm -r test
ls
cat sumM2N.c
gcc sumM2N.c
ls
rm a.out
gcc sumM2N.c -o sumM2N
cat test.c
gcc test.c -o test
./test
./sumM2N
ls
clear
cd
ls
rm sum2
mkdir week02
mv sum2.c week02
mv testfile week02
cat selSort.c
mv serSort.c week03
mv selSort.c week03
cat data
mv data week03
ls
mv sortData week03
cd week03
ls
mv helloWorld ../week02
mv helloWorld.c ../week02
ls
cd
clear
ls
cd test
ls
cd
rm -r test
rm -r backup
ls
clear
ls
mkdir week05
cd week05
vim practice01.c
gcc practice01.c -o practice01
cat practice01.c
vim practice01.c
gcc practice01.c -o practice01
gcc practice01.c -o -std=c99  practice01
vim practice01.c
gcc practice01.c -o practice01
./practice01
clear
vim practice02.c
gcc practice02.c -o practice02
vim practice02.c
gcc practice02.c -o practice02
vim practice02.c
gcc practice02.c -o practice02
./practice02
clear
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX_SIZE_STACK 100
 
typedef struct {
    int stack[MAX_SIZE_STACK];
    int top;
}StackType;
 
void init(StackType *s)
{     s->top = -1; }
 
int is_empty(StackType *s){
    return s->top == -1;
}
 
int is_full(StackType *s){
    return s->top == MAX_SIZE_STACK - 1;
} 
 
void push(StackType *s, int item){
    if(is_full(s))
        exit(1);
    s->stack[++(s->top)] = item;
}
 
int pop(StackType *s){
    if(is_empty(s))
        exit(1);
    return s->stack[(s->top)--];
} 
 
int calc(char *exp)
{     int op1, op2, value, i;     int len = (int)strlen(exp);
    char ch;
    StackType s;
    
    init(&s);
    
    for(i=0; i<len; i++)
    {         ch = exp[i];                  if(ch!='*' && ch!='+' && ch!='/' && ch!='-');         {             value = ch - '0';             push(&s, value);
            continue;
        }
        
        op2 = pop(&s);
        op1 = pop(&s);
        
        switch(ch){
            case '*': value = op1*op2; break;
            case '+': value = op1+op2; break;
            case '/': value = op1/op2; break;
            case '-': value = op1-op2; break;
            default : exit(1); break;
        }
        
        push(&s, value);
    }
    
    return pop(&s);
}
 
int main(void)
{     int result;     char *postfix = "82/3-32*+";     result = calc(postfix);
    printf("후위 표기식 %s의 계산 결과 : %d\n", postfix, result);
    return 0;
}
clear
ls
cat top
rm top
touch practice03.c
vim practice03.c
gcc practice03.c -o practice03
./practice03
ls
vim practice04.c
gcc practice04.c -o practice04
./practice04
vim practice05.c
gcc practice05.c -p practice05
gcc practice05.c -o practice05
./practice05
cat practice05
cat practice05.c
ls
rm practice05 practice05.c
ls
vim practice05.c
gcc practice05.c -o practice05
rm practice05
ls
vim practice05.c
gcc practice05.c -o practice05
ls
cd
ls
quit
q
exit
l
li
-li
ㅣㄴ
ls
mkdir week06
ls
cd week06
vim cat2.c
ls
cat2.c
cat2 -n file
rm cat2.c
vi cat2.c
cat2 f1
gcc cat2.c -o cat2
clear
gcc -o cat2 cat2.c
ls
gcc cat2.c -o cat2
cat2.c
cat cat2.c
vim cat2.c
gcc cat2.c -o cat2
cat2 f1
ls
cat2 -n file
/.cat2 test
./cat2 >> test
ls
cat test
rm test
cat >> test
./cat2 test
cat2 >> test1
cat2 -n file
rm cat2.c
rm cat2
vi cat2.c
./cat2 cat2.c
cat2 > test
ls
rm test
rm test1
clear
ls
gcc -o cat2 cat2.c
./cat2 cat2.c
cat2 -n file
cat2 > test
./cat2 > test
rm test
cat f1
cat > f1
cat > f2
clear
cat2 f1
cat2 > f1
./cat2 > f1
cat f1
cat f2
ls
cat2 > test
rm cat2
rm cat2.c
vim cat2.c
ls
rm f1
clear
gcc -o cat2 cat2.c
cat2 f1
./cat2 f1
./cat2 f2
vim cp2.c
gcc cp2 -o cp2.c
ls
gcc cp2.c -o cp2
cat cp2.c
vim cp2.c
clear
gcc cp2.c -o cp2
cp2 f1 f2
./cp2 f1 f2
ls
cat f1
cat f2
vim chdir.c
./cat2 f1
./cat2 f2
./cat2 > f1
./cat2 > f2
./cat2 f1
./cat2 f2
./cat2 -n f2
./cp2 f1 f2
cat f2
mkdir cpdir
./cp2 f1 f2 cpdir
ls
gcc chdir -o chdir.c
gcc chdir.c -o chdir
cat chdir.c
vim chdir.c
gcc chdir.c -o chdir
clear
ls
./cp2 f1 cpdir
cd cpdir
ls
cat cpdir
cd ./
cd /
cd
ls
cd week06
ls
./cp2 f2 cpdir
cd cpdir
ls
./
/
/.
//
cd week06
cd ./week06
cd /week06
cd
cd week06
exit
ls
mkdir -m 750------ protection
mkdir midexam
mkdir protection
chmod 700------ protection
chmod rwx------protection
chmod rwx------ protection
cd midexam
vi maxmin.c
gcc maxmin.c -o maxmin
gcc maxmin -o maxmin.c
gcc maxmin.c -o maxmin
vim maxmin.c
gcc maxmin.c -o maxmin
vim maxmin.c
gcc maxmin.c -o maxmin
cat indata
cat > indata
ls
./maxmin < indata
vim maxmin
vi maxmin.c
rm maxmin
gcc maxmin.c -o maxmin
./maxmin < indata
vim fibo.c
ls
gcc fibo.c -o fibo
cat > result2
./maxmin < result2 > result2
./fibo < result2 > result2
cat result2
./fibo < 2
./fibo < result2
vim fibo.c
fibo
cat fibo
clear
rm fibo
vim fibo.c
gcc fibo.c -o fibo
./fibo < result2 > result2
./fibo < result2
rm fibo
vim fibo.c
gcc fibo.c -o fibo
./fibo < result2
rm result2
./fibo > result2
cat result2
rm fibo
vim fibo.c
gcc fibo.c -o fibo
./fibo > result2
cat fibo.c
./fibo > result2
cat resutl2
cat result2
./fibo > result2
cat result2
ls
cd
chmod 777 midexam
ls -l midexam
ls -l
vim wc2.c
ls
rm wc2.c
cd midexam
ls -l
clear
ls
history > mycommands
exit
