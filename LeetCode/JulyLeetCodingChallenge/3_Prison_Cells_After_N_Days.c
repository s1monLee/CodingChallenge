#define BYTE_TO_BINARY_PATTERN "%c%c%c%c%c%c%c%c\n"
#define BYTE_TO_BINARY(byte)  \
  (byte & 0x80 ? '1' : '0'), \
  (byte & 0x40 ? '1' : '0'), \
  (byte & 0x20 ? '1' : '0'), \
  (byte & 0x10 ? '1' : '0'), \
  (byte & 0x08 ? '1' : '0'), \
  (byte & 0x04 ? '1' : '0'), \
  (byte & 0x02 ? '1' : '0'), \
  (byte & 0x01 ? '1' : '0') 

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* prisonAfterNDays(int* cells, int cellsSize, int N, int* returnSize){
    int *ans = (int*)malloc(sizeof(int)*cellsSize);
    *returnSize = cellsSize; 
    uint8_t num = 0;
    for(int i=0;i<cellsSize;++i){
        num|=cells[i];
        num=i==7?num:num<<1;
    }
    N=N%14==0?14:N%14;
    for(int i=0;i<N;++i){
        //printf("%d "BYTE_TO_BINARY_PATTERN, i,BYTE_TO_BINARY(num));
        num = (~((num>>1)^(num<<1)))&126;
    }
    //printf(BYTE_TO_BINARY_PATTERN, BYTE_TO_BINARY(num));
    
    for(int i=7;i>=0;--i){
        ans[i] = num & 1;
        num>>=1;
    }
    
    return ans;
}
