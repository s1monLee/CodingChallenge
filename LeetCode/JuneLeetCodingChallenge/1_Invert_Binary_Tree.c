/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

void swap(struct TreeNode* root){
    if(root == NULL)return;
    struct TreeNode* tmp = root->left;
    root->left = root->right;
    root->right = tmp;
    swap(root->left);
    swap(root->right);
}
struct TreeNode* invertTree(struct TreeNode* root){
    swap(root);
    return root;
}
