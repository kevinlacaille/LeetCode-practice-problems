class Solution {
    public int[] runningSum(int[] nums) {

        int[] out = new int[nums.length];
        int total = 0;
        for (int i = 0; i < nums.length; i++) {
            total += nums[i];
            out[i] = total;
        }
        return out;

    }
}