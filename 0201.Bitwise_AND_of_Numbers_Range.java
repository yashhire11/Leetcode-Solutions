class Solution {
    public int rangeBitwiseAnd(int m, int n) {
        int count = 0;
        while(n != m)
        {
            n = n>>1;
            m = m>>1;
            count++;
        }
        return n << count;
    }
}
