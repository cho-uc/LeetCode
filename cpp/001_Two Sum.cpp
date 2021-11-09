/* Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
Example :Input: nums = [2,7,11,15], target = 9
Output: [0, 1]
*/

#include <iostream>
#include <vector>

using namespace std;

vector<int> twoSum(vector<int>& nums, int target) {
	int a, b;
	for (int i = 0; i < nums.size(); i++) {
		if (find(nums.begin(), nums.end(), target - nums[i]) != nums.end()) {
			/*distance basically returns the distance of an iterator from the first iterator.
			so here i am checking the second index where i found the target -nums[i]*/
			a = distance(nums.begin(), find(nums.begin(), nums.end(), target - nums[i]));
			b = i;
			/* if both the indexes are equal then there's no point in breaking the loop as same
			indexes aren't allowed.*/

			if (a == b) {
				continue;
			}
			// if the indexes aren't equal we can break the loop
			break;
		}
	}
	vector<int> ans;
	ans.push_back(b);
	ans.push_back(a);
	return ans;
}

int main()
{
    std::cout << "Running Twosums \n";
	vector <int> nums = { 2,7,11,15 };
	int target = 9;
	vector<int> ans = twoSum(nums, target);
	cout << "Index of Two sums = "<< ans[0]<<" and "<< ans[1]<<endl;
}
