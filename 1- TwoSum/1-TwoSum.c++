#include<unordered_map>
#include<vector>
#include<iostream>
using namespace std;

class Solution {
    public:
        vector<int> twoSum(vector<int>& nums, int target) {
            unordered_map<int,int> hashMap;
            for(auto it=nums.begin();it!=nums.end();it++){
                if(hashMap.find(target-*it)!=hashMap.end()){
                    return {hashMap[target-*it],static_cast<int>(it-nums.begin())};
                }
                hashMap[*it]=it-nums.begin();
            }
            return {};
        }
};

int main(){
    Solution s;
    vector<int> nums={2,1,5,3};
    int target=4;
    vector<int> result=s.twoSum(nums,target);
    cout << "[";
    for(auto it=result.begin();it!=result.end();it++){
        cout<<*it;
        if( it!=result.end()-1){
            cout<<",";
        }
    }
    cout<<"]"<<endl;
    return 0;
}

