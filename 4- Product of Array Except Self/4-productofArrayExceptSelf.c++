#include<iostream>
#include<vector>

using namespace std;

class Solution{
    public:
        vector<int> productExceptSelf(vector<int>& nums) {
            int n = nums.size();
            vector<int> output(n, 1);
            int left = 1;
            for (int i = 0; i < n; i++) {
                output[i] *= left;
                left *= nums[i];
            }
            int right = 1;
            for (int i = n - 1; i >= 0; i--) {
                output[i] *= right;
                right *= nums[i];
            }
            return output;
        }
};

int main(){
    Solution s;
    vector<int> nums={1,2,3,4};
    vector<int> output = s.productExceptSelf(nums);
    for (int i = 0; i < output.size(); i++) {
        cout << output[i] << " ";
    }
    cout << endl;
}