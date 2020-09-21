# 문제
```
int[] nums, int target 가 주어지고
exactly one solution 을 가진다

Input: nums = [2,7,11,15], target = 9 
Output: [0,1] 
Output: Because nums[0] + nums[1] == 9, we return [0, 1].

더해서 target이 되는 배열의 자리를 리턴한다.
```

# 1. Brute Force 
```
class Solution {
    public int[] twoSum(int[] nums, int target) {
        int n = nums.length;
        
        for(int i=0; i<n-1; i++) {
            for(int j=i+1; j<n; j++) {
                if(nums[j] == target - nums[i]) {
                    return new int[] {i, j};
                }
            }
        }
        
        throw new IllegalArgumentException("No two sum solution");
    }
}
```
```
nums[i]+nums[j]=target 도 되는데... j를 기준으로 돌고있으니까 nums[j]=target-nums[i] 를 해준건가?

new int[] {i, j}
IllegalArgumentException("No two sum solution");

Time complexity: O(n^2)
Space complexity: O(1)
```
​
# 2. Two-pass Hash Table
```
해시맵 HashMap
동일키 불가능
put(키, 값);
get(키);
remove(키);
clear();
entrySet();
keySet();
```
```
//entrySet() 활용
for (Entry<Integer, String> entry : map.entrySet()) {
    System.out.println("[Key]:" + entry.getKey() + " [Value]:" + entry.getValue());
}
//entrySet().iterator()
Iterator<Entry<Integer, String>> entries = map.entrySet().iterator();
while(entries.hasNext()){
    Map.Entry<Integer, String> entry = entries.next();
    System.out.println("[Key]:" + entry.getKey() + " [Value]:" +  entry.getValue());
}

//KeySet() 활용
for(Integer i : map.keySet()){ //저장된 key값 확인
    System.out.println("[Key]:" + i + " [Value]:" + map.get(i));
}
//keySet().iterator()
Iterator<Integer> keys = map.keySet().iterator();
while(keys.hasNext()){
    int key = keys.next();
    System.out.println("[Key]:" + key + " [Value]:" +  map.get(key));
}
```
```
public int[] twoSum(int[] nums, int target) {
    Map<Integer, Integer> map = new HashMap<>();
    for (int i = 0; i < nums.length; i++) {
        map.put(nums[i], i);
    }
    for (int i = 0; i < nums.length; i++) {
        int complement = target - nums[i];
        if (map.containsKey(complement) && map.get(complement) != i) {
            return new int[] { i, map.get(complement) };
        }
    }
    throw new IllegalArgumentException("No two sum solution");
}
```
```
* index 0 부터 for문을 돌려, 2가 나왔어 10-2를 해서 8이 나왔어 
* 이 8을 맵에 등록을해 (8,1) 
* 얘인덱스가 1이니깐 index를 돌려서 맵에있는거랑 매치가 되면 결국 index를 구할수있다.

Time complexity : O(n), 키값이 있으면 O(1) + 처음에 맵에 집어 넣을 때 O(n)
Space complexity : O(n)
```
