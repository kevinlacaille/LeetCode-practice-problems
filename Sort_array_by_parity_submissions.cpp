class Solution {
public:
    vector<int> sortArrayByParity(vector<int>& A) {

        // Initialize a vectory where we'll store our sorted list
        vector<int> sorted_list;

        // Check to see if A is empty
        if (A.size() == 0){
            return A;
        }

        // Otherwise, add even elements to front of vector and odd to the back
        else{

            for(int i = 0; i < A.size(); i++){

                // Add even elements to front of the vector
                if (A[i] % 2 == 0){

                    sorted_list.insert(sorted_list.begin(), A[i]);

                }

                // Add odd elements to back of the vector
                else{

                    sorted_list.push_back(A[i]);

                }

            }

            return sorted_list;
        }

    }
};
