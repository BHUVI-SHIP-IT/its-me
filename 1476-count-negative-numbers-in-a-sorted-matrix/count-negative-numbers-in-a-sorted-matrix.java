class Solution {
    public int countNegatives(int[][] grid) {
        int row=grid.length;
        int col=grid[0].length;
        int i=row-1;
        int ans=0;
        int j=0;
        while(i>=0 && j<col)
        {
            if(grid[i][j]<0)
            {
                ans+=col-j;
                --i;
            }
            else
            {
                j++;
            }
        }
        return ans;

    }
}