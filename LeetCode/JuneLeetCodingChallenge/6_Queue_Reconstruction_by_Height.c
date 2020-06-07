

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */

int cmp(const void* a, const void* b){
    return (*(const int**)a)[0] - (*(const int**)b)[0];
}
int** reconstructQueue(int** people, int peopleSize, int* peopleColSize, int* returnSize, int** returnColumnSizes){
    *returnColumnSizes = (int*)malloc(sizeof(int)*(*returnSize=peopleSize));
    int** queue = (int**)malloc(sizeof(int*)*(*returnSize));
    for(int i=0;i<*returnSize;++i){
        queue[i]=(int*)malloc(sizeof(int)*((*returnColumnSizes)[i]=2));
        queue[i][0] = -1;
    }
    qsort(people,peopleSize,sizeof(people),cmp);
    for(int i=0;i<*returnSize;++i){
        int k = people[i][1];
        for(int j=0;j<*returnSize;++j){
            if(queue[j][0] == -1){
                if(k<=0){
                    queue[j][0] = people[i][0];
                    queue[j][1] = people[i][1];
                    break;
                }
                --k;
            }else if(queue[j][0]>=people[i][0]){
                --k;
            }
        }
    }
    return queue;
}
