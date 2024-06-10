impl Solution {
    pub fn height_checker(mut heights: Vec<i32>) -> i32 {
        let mut expected = heights.clone();
        expected.sort();
        let mut non_matches: i32 = 0;

        for i in 0..heights.len() {
            if heights[i] != expected[i] {
                non_matches += 1;
            }
        }

        non_matches
    }
}
