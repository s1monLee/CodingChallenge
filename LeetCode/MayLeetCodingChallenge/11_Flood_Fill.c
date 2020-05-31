

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */

void recPaint(int** arr,int i,int j,int size,int colSize,int color,int newColor){
    arr[i][j] = newColor;
    if(j!=0){
        if(arr[i][j-1]==color)
            recPaint(arr,i,j-1,size,colSize,color,newColor);
    }
    if(i!=0){
        if(arr[i-1][j]==color)
            recPaint(arr,i-1,j,size,colSize,color,newColor);
    } 
    if(j+1<colSize){
        if(arr[i][j+1]==color)
            recPaint(arr,i,j+1,size,colSize,color,newColor);
    }
    if(i+1<size){
        if(arr[i+1][j]==color)
            recPaint(arr,i+1,j,size,colSize,color,newColor);
    }
}
int** floodFill(int** image, int imageSize, int* imageColSize, int sr, int sc, int newColor, int* returnSize, int** returnColumnSizes){
    *returnColumnSizes = malloc(sizeof(int)*(*returnSize = imageSize));
    for(int i=0;i<imageSize;++i){
        (*returnColumnSizes)[i] = imageColSize[i];
    }
    int oldColor = image[sr][sc];
    if(oldColor== newColor)
        return image;
    recPaint(image,sr,sc,imageSize,imageColSize[0],oldColor,newColor);
    return image;
}


/*


void recPaint(int** arr,int i,int j,int size,int colSize,int color,int newColor){
    arr[i][j] = newColor;
    if(j!=0){
        if(arr[i][j-1]==color)
            recPaint(arr,i,j-1,size,colSize,color,newColor);
    }
    if(i!=0){
        if(arr[i-1][j]==color)
            recPaint(arr,i-1,j,size,colSize,color,newColor);
    } 
    if(j+1<colSize){
        if(arr[i][j+1]==color)
            recPaint(arr,i,j+1,size,colSize,color,newColor);
    }
    if(i+1<size){
        if(arr[i+1][j]==color)
            recPaint(arr,i+1,j,size,colSize,color,newColor);
    }
}
int** floodFill(int** image, int imageSize, int* imageColSize, int sr, int sc, int newColor, int* returnSize, int** returnColumnSizes){
    *returnColumnSizes = malloc(sizeof(int)*(*returnSize = imageSize));
    int** result = (int**)malloc(sizeof(int*)*(*returnSize));
    for(int i=0;i<imageSize;++i){
        result[i] = malloc(sizeof(int)*((*returnColumnSizes)[i] = imageColSize[i]));
        for(int j=0;j<imageColSize[i];++j){
            result[i][j] = image[i][j];
        }
    }
    int oldColor = image[sr][sc];
    if(oldColor== newColor)
        return result;
    recPaint(result,sr,sc,imageSize,imageColSize[0],oldColor,newColor);
    return result;
}
*/
