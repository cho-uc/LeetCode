/* Given an integer x, return true if x is palindrome integer.
Example :
Input: x = 121 -> true
Input: x = -121 ->false
*/

#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
	static int reversNumber(int x) {
		long y = 0;
		while (x > 0) {
			int tmp = x % 10;
			x = x / 10;
			y = y * 10 + tmp;
		}
		return (int)y;
	}

	static bool isPalindrome(int x) {
		if (x < 0) {
			return false;
		}

		int revers_num = reversNumber(x);
		if (revers_num == x)
			return true;
		return false;
	}
};

int main()
{
    std::cout << "Running Palindrome checker \n";
	int target = -121;
	int target2 = 121;
	auto ans = Solution::isPalindrome(target);
	auto ans2 = Solution::isPalindrome(target2);
	cout << "Is "<< target<<" Palindrom ? "<< ans<<endl;
	cout << "Is " << target2 << " Palindrom ? " << ans2 << endl;
}
