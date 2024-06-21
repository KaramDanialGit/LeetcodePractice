use std::collections::VecDeque;

struct MyStack {
    primary: VecDeque<i32>,
    secondary: VecDeque<i32>,
}

impl MyStack {

    fn new() -> Self {
        MyStack {primary: VecDeque::new(), secondary: VecDeque::new()}
    }
    
    fn push(&mut self, x: i32) {
        while !self.primary.is_empty() {
            self.secondary.push_back(self.primary.pop_front().unwrap());
        }

        self.primary.push_back(x);

        while !self.secondary.is_empty() {
            self.primary.push_back(self.secondary.pop_front().unwrap());
        }
    }
    
    fn pop(&mut self) -> i32 {
        if self.primary.is_empty() {
            return -1;
        }
        
        return self.primary.pop_front().unwrap();
    }
    
    fn top(&self) -> i32 {
        self.primary[0]
    }
    
    fn empty(&self) -> bool {
        self.primary.is_empty()
    }
}