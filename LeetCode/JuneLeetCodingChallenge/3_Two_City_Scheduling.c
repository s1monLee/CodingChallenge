#define fr(N) for(int i = 0;i<N;++i)
int cmp(void* a, void* b){
    int* pa = *(int**)a;
    int* pb = *(int**)b;
    return ((pa[1]-pa[0]) - (pb[1]-pb[0]));
}

int twoCitySchedCost(int** costs, int costsSize, int* costsColSize){
    qsort(costs,costsSize,sizeof(costs),cmp);
    int ans = 0;
    fr(costsSize)
        ans+=(costsSize>>1)<=i?costs[i][0]:costs[i][1];
    return ans; 
}
