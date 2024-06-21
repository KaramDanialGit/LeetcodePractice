use std::cmp::max;

impl Solution {
    pub fn max_satisfied(customers: Vec<i32>, grumpy: Vec<i32>, minutes: i32) -> i32 {
        let mut max_sat = 0;
        let length = customers.len();

        for i in 0..length {
            let i = i as usize;
            let mut current = i;
            let mut score = 0;
            let mut j = minutes as usize;

            while j > 0 && current != length{
                score += customers[current];
                
                if grumpy[current] == 0 {
                    current += 1;
                } else {
                    current += 1;
                    j -= 1;
                }
            }

            max_sat = max(max_sat, score);
        }

        max_sat as i32
    }
}