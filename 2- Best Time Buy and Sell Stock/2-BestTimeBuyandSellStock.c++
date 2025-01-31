#include<vector>
#include<iostream>
using namespace std;

class Solution {
    public:
    int maxStock(vector<int>& prices){
        int lPointer = 0;
        int rPointer = 1;
        int maxProfit = 0;
        while(rPointer < prices.size()){
            if(prices[lPointer] < prices[rPointer]){
                int profit = prices[rPointer] - prices[lPointer];
                maxProfit = max(maxProfit, profit);
            }
            else{
                lPointer = rPointer;
            }
            rPointer++;
        }
        return maxProfit;
    }
};

int main(){
    Solution sol;
    vector<int> prices = {7,1,5,3,6,4};
    cout << sol.maxStock(prices) << endl;
    return 0;
}

