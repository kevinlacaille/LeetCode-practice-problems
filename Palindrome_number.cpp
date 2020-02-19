class Solution {
public:
    bool isPalindrome(int x) {

        if(x < 0){

            return false;

        }

        else{

            std::string reversed_x = std::to_string(x);
            std::string x_str = reversed_x;

            std::reverse(reversed_x.begin(), reversed_x.end());

            if(reversed_x == x_str){
                return true;
            }
            else{
                return false;
            }
        }
    }
};
