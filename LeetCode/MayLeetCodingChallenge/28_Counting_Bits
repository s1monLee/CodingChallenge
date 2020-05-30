
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* countBits(int num, int* returnSize){
    int* answer = (int*) malloc(sizeof(int)*(*returnSize=num+1));
    answer[0] = 0;
    for(int i=1;i<=num;i++)
        answer[i] = answer[(i>>1)]+i%2;
    return answer;
}
