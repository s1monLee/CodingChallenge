int hammingDistance(int x, int y){
    int dist = 0;
    x ^= y;
    while(x){
        x &= (x-1);
        dist++;
    }
    return dist;
}
