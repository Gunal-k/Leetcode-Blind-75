#include<vector>
#include<unordered_set>
#include<iostream>
using namespace std;

class Solution {
    public:
        bool containsDuplicate(vector<int>& nums) {
            // unordered_set<int> s;
            // for (int i = 0; i < nums.size(); i++) {
            //     if (s.find(nums[i]) != s.end()) {
            //         return true;
            //     }
            //     s.insert(nums[i]);
            // }
            // return false;

            unordered_set<int> s(nums.begin(), nums.end());
            return s.size() < nums.size();
        }
};

int main(){
    Solution s;
    vector<int> nums={1,2,3,1};
    cout << s.containsDuplicate(nums) << endl;
}