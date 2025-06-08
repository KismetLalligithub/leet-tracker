int findLHS(vector<int>& nums) {
	std::unordered_map<int, int> freq; 

	for(int i=0;i<nums.size();++i) ++freq[nums[i]]; 
	int best = 0; 

	for(const auto& pair : freq) {
		if (freq.find(pair.first + 1) != freq.end())
			best = std::max(best, pair.second + freq[pair.first + 1])
	}
	return best; 
}
