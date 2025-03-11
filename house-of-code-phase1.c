#include<stdio.h>
#include<string.h>
#include<stdbool.h>
    //problem 1 solving
int my_strlen(const char *str){
    int i=0;
    while(str[i]!= '\0'){
        i++;
    }
    return(i);
    }
    //problem 2 solving
void reverse_string(char *str){
    int length = my_strlen(str);
    char str1[100] ="";
    for(int i=0; i<length; i++){
       str1[i] = str[length-1-i];
    }
    str1[length]='\0';
    for(int i=0; i<length; i++){
        str[i] = str1[i];
    }
    str[length]='\0';
 }
    //problem 3 solving
 void reverse_words(char *str){
    int length = my_strlen(str);
    char str1[100] ="";
    int x=0;                     //index of str1
    for(int i=length-1; i>0; i--){
        if(str[i] == ' '){
            int j=i;
            do{
                str1[x++] = str[j];
                j++;
            }while((str[j] != '\0')&&(str[j] != ' '));
        }
    }
    // here my code stops in the index 0 cuz there is no space for accessing to the while loop inside of the for loop
    //so i add an exeptional situation for the last word
            int j=0;
            str1[x++]=' '; // adding a space before the last word
            do{
                str1[x++] = str[j];
                j++;
            }while((str[j] != '\0')&&(str[j] != ' '));

    str1[length+1]='\0';
    for(int i=1; i<length+1; i++){
        str[i-1] = str1[i];
    }
    str[length]='\0';
 }
    //problem 4 solving
bool isValid(const char *str){
    int length = my_strlen(str);
    int x=0;
    int y=0;
    int z=0;
    for(int i=0; i<length; i++){
           //for )
        if(str[i]=='('){
            x++;
            for(int j=i; j<length; j++){
                if(str[j]==')'){
                    x--;
                    break;
                }
            }
           }
           //for ]
           else if(str[i]=='['){
            y++;
            for(int j=i; j<length; j++){
                if(str[j]==']'){
                    y--;
                    break;
                }
            }
           }
           //for }
           else if(str[i]=='{'){
            z++;
            for(int j=i; j<length; j++){
                if(str[j]=='}'){
                    z--;
                    break;
                }
            }
           }
    }
    if(((x==0)&&(y==0))&&(z==0))
        return(true);
        else return(false);
}


 int main(void){
     //problem 1 testing
 const char *test1 = "IAE CLUB";
 const char *test2 = "House Of Code";
 const char *test3 = "G";
 const char *test4 = "";
 printf("Test 1: %s\n", test1);
 printf("Length: %d\n", my_strlen(test1));
 printf("Test 2: %s\n", test2);
 printf("Length: %d\n", my_strlen(test2));
 printf("Test 3: %s\n", test3);
 printf("Length: %d\n", my_strlen(test3));
 printf("Test 4: %s\n", test4);
 printf("Length: %d\n", my_strlen(test4));

     //problem 2 testing
 char Test1[] = "edoc fo esuoH oT emocleW";
 char Test2[] = "uoy pleh lliw ti ;3 melborp ni noitcnuf siht esU";
 char Test3[] = "Hello World";
 char Test4[] = "G";
 printf("Before: %s\n", Test1);
 reverse_string(Test1);
 printf("After: %s\n\n", Test1);
 printf("Before: %s\n", Test2);
 reverse_string(Test2);
 printf("After: %s\n\n", Test2);
 printf("Before: %s\n", Test3);
 reverse_string(Test3);
 printf("After: %s\n\n", Test3);
 printf("Before: %s\n", Test4);
 reverse_string(Test4);
 printf("After: %s\n\n", Test4);

        //problem 3 testing
 char tesT1[] = "The dragons are coming";
 char tesT2[] = "code love I";
 char tesT3[] = "G";
 printf("Before: %s\n", tesT1);
 reverse_words(tesT1);
 printf("After: %s\n\n", tesT1);
 printf("Before: %s\n", tesT2);
 reverse_words(tesT2);
 printf("After: %s\n\n", tesT2);
 printf("Before: %s\n", tesT3);
 reverse_words(tesT3);
 printf("After: %s\n\n", tesT3);

        //problem 4 testing
 const char *teSt1 = "()";
 const char *teSt2 = "[{()}]";
 const char *teSt3 = "{[(a+b) * x}";
 const char *teSt4 = "{[a+b]*(x/y)}";
 printf("Test 1: %s\n", teSt1);
 printf("Is valid: %d\n", isValid(teSt1));
 printf("Test 2: %s\n", teSt2);
 printf("Is valid: %d\n", isValid(teSt2));
 printf("Test 3: %s\n", teSt3);
 printf("Is valid: %d\n", isValid(teSt3));
 printf("Test 4: %s\n", teSt4);
 printf("Is valid: %d\n", isValid(teSt4));


 return 0;
 }
