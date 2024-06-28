class Solution {
public:
    int hIndex(vector<int>& citations) {
        int n = citations.size();
        int i = n-1;
        while(i >= 0){
            if(citations[i] < n-i)break;
            i--;
        }
        return n-i-1;
    }
};
