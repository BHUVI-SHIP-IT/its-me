class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        int currgas=0;
        int startindex=0;
        int total_gas=0;
        int total_cost=0;
        for(int i=0;i<gas.size();i++){
            total_gas=total_gas+gas[i];
            total_cost=total_cost+cost[i];
            currgas+=gas[i]-cost[i];

            if(currgas<0){
                startindex=i+1;
                currgas=0;
            }
        }
        return(total_gas<total_cost) ? -1 : startindex;
    }
};