// https://leetcode.com/problems/top-k-frequent-elements/
// https://leetcode.com/problems/top-k-frequent-elements/
import java.util.*;

public class TopKFreqElements {
    public int[] TopKFrequent(int[] nums, int k) {
        Map<Integer, Integer>count = new HashMap();
        for(int num:nums) {
            count.put(num, count.getOrDefault(num, 0));
        }
        List<Integer>[] buckets = new List[nums.length+1];
        for(int i=0;i<buckets.length;i++)
        {
            buckets[i] = new ArrayList<>();
        }
        for(int key: count.keySet()) {
            buckets[count.get(key)].add(key);
        }
        List<Integer> flattened = new ArrayList<>();
        for(int i = buckets.length-1;i>=0;i--) {
            for(int num:buckets[i]) {
                flattened.add(num);
            }
        }
        int [] top = new int[k];
        for(int i=0;i<k;i++) {
            top[i]=flattened.get(i);
        }
        return top;
    }
    // HEAP SOL ->
    // public int[] TopKFrequent(int[] nums, int k) {
    //     Map<Integer, Integer>count = new HashMap();
    //     for(int num:nums) {
    //         count.put(num, count.getOrDefault(num, 0));
    //     }
    //     Queue<Integer> heap = new PriorityQueue<>((n1, n2) -> count.get(n1) - count.get(n2));
    //     for(int num: count.keySet()) {
    //         heap.add(num);
    //         // poll -> removes & returns head
    //         if(heap.size() > k) heap.poll();
    //     }
    //     int [] top = new int[k];
    //     for(int i=k-1; i>=0; --i) {
    //         top[i]=heap.poll();
    //     }
    //     return top;
    // }

}
