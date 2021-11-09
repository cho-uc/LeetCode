/* Roman (string) to Integer converter
Example :
Input: s = "IX" -> 9
*/

#include <iostream>
#include <vector>

using namespace std;

int romanToInt(char* s) {
	int numeral[22];    // enough space for 'C' to 'X'
	numeral[6] = 1;     // indexes are offset by 'C' ('I'-'C')
	numeral[19] = 5;
	numeral[21] = 10;
	numeral[9] = 50;
	numeral[0] = 100;
	numeral[1] = 500;
	numeral[10] = 1000;

	int tmp, res = 0;
	int prev = 0;

	while (*s != 0) {
		tmp = numeral[*s - 67];
		res += (prev < tmp) ? tmp - 2 * prev : tmp;

		prev = tmp;
		s++;
	}

	return res;
}

int main()
{
    std::cout << "Roman (string) to Integer converter \n";
	char a1[10]= "VIII";
	auto ans1 = romanToInt(a1);
	char a2[10] = "XIV";
	auto ans2 = romanToInt(a2);
	cout << "Roman "<< a1<<" equals to numeric "<< ans1<<endl;
	cout << "Roman " << a2 << " equals to numeric " << ans2 << endl;
}
