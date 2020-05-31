/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
int dep = 0, par = 0, xD = -1,yD = -1,xP = -1,yP = -1;
void recTree(struct TreeNode* root, int x, int y){
    dep++;
    xP = root->val == x?par:xP;
    yP = root->val == y?par:yP;
    if(root->left != NULL){
        par = root->val;
        printf("left dep->%d root->%d\n",dep,root->val);
        recTree(root->left,x,y);
    }
    if(root->right != NULL){
        par = root->val;
        printf("right dep->%d root->%d\n",dep,root->val);
        recTree(root->right,x,y);
    }
    dep--;
    printf("end dep->%d root->%d\n",dep,root->val);
    xD = root->val == x?dep:xD;
    yD = root->val == y?dep:yD;
}

bool isCousins(struct TreeNode* root, int x, int y){
    recTree(root,x,y);
    return (xD == yD)&&(xP != yP)?true:false;
}
