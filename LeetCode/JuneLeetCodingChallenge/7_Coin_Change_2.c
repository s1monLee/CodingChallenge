int change(int amount, int* coins, int coinsSize){
    int dp[500][5001] = {0};
    for(int i = 0;i<=coinsSize;++i){
        for(int j=0;j<=amount;++j){
            if(j == 0){
                dp[i][j] = 1;
                continue;
            }
            if(i == 0){
                dp[i][j] = 0;
                continue;
            }
            if(j-coins[i-1] >= 0)
                dp[i][j] = dp[i-1][j]+dp[i][j-coins[i-1]];
            else
                dp[i][j] = dp[i-1][j];
            //printf("%d ",dp[i][j]);
        }
         //printf("\n");
    }
    return dp[coinsSize][amount];
}
