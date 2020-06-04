void revers(char* s, int head, int tail){
    if(head>=tail)
        return;
    revers(s,head+1,tail-1);
    char tmp = s[head];
    s[head] = s[tail];
    s[tail] = tmp;  
}

void reverseString(char* s, int sSize){
    revers(s,0,sSize-1);
}
