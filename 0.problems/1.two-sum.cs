public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        Dictionary<int, int> complements = new ();

        for (int i = 0; i < nums.Length; i++) {
            if (complements.TryGetValue(nums[i], out int index)) {
                return new int[] { index, i };
            }
            complements[target - nums[i]] = i;
        }
        return new int[] {}; // return an empty array if no solution is found
    }
}

