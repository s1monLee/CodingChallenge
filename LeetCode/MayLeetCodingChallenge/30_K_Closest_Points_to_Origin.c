

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */

int cmp(const void *a, const void *b) {
    int* A = *(const int**)a;
    int* B = *(const int**)b;
    return (A[0]*A[0] + A[1]*A[1]) - (B[0]*B[0] + B[1]*B[1]);
}
int** kClosest(int** points, int pointsSize, int* pointsColSize, int K, int* returnSize, int** returnColumnSizes){
    *returnColumnSizes = (int*) malloc(sizeof(int)*(*returnSize=K));
    int** ans = (int**) malloc(sizeof(int*)*(*returnSize));
    for(int i=0;i<*returnSize;++i)
        ans[i] = (int*) malloc(sizeof(int)*((*returnColumnSizes)[i]=*pointsColSize));
        
    qsort(points,pointsSize,sizeof(points),cmp);

    for(int i=K-1;i>=0;--i){
        ans[i][0]=points[i][0];
        ans[i][1]=points[i][1];
    }
    
    return ans;
}
