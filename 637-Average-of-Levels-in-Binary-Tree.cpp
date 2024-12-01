class Solution {
public:

    vector< pair<double, int> >ans;
    void dfs(int level, TreeNode* root)
    {
        if(!root)
            return;
        
        if(ans.size() < level)
            ans.push_back({root->val,1});
        else
        {
            ans[level-1].first  = ans[level-1].first + root->val;
            ans[level-1].second = ans[level-1].second + 1;
        }
        dfs(level+1, root->left);
        dfs(level+1, root->right); 
    }


    vector<double> averageOfLevels(TreeNode* root) 
    {
        if(!root)
            return { };

        vector<double> res;
        dfs(1,root);

        for(int i=0; i<ans.size(); i++)
            res.push_back(ans[i].first / ans[i].second);

        return res;
    }
};