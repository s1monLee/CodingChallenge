

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */

typedef struct point{
    int key;
    int x;
    int y;
}_arr;
int cmp(const void *a, const void *b) {
    _arr* A = (_arr*)a;
    _arr* B = (_arr*)b;
    return A->key - B->key;
}
int** kClosest(int** points, int pointsSize, int* pointsColSize, int K, int* returnSize, int** returnColumnSizes){
    *returnColumnSizes = (int*) malloc(sizeof(int)*(*returnSize=K));
    int** ans = (int**) malloc(sizeof(int*)*(*returnSize));
    _arr* dist = (_arr*)malloc(sizeof(struct point)*pointsSize);
    for(int i=0;i<*returnSize;++i){
        ans[i] = (int*) malloc(sizeof(int)*((*returnColumnSizes)[i]=*pointsColSize));
    }
    
    for(int i=0;i<pointsSize;++i){
        dist[i].key = points[i][0]*points[i][0]+points[i][1]*points[i][1];
        dist[i].x = points[i][0];
        dist[i].y = points[i][1];
    }
    
    qsort(dist,pointsSize,sizeof(struct point),cmp);

    for(int i=K-1;i>=0;--i){
        ans[i][0]=dist[i].x;
        ans[i][1]=dist[i].y;
    }
    //free(dist);
    return ans;
}
