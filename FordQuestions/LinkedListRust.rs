use std::mem;

struct LinkedList {
    head: Option<Box<Node>>,
    tail: Option<Box<Node>>,
}

impl LinkedList {
    fn new(head: Option<Box<Node>>) -> Self {
        let n1 = head.clone();
        let n2 = n1.clone();
        Self { head: n1, tail: n2 }
    }

    fn add(&mut self, val: i32) {
        let new_node = Box::new(Node {
            val,
            next: mem::replace(&mut self.head, None),
        });

        self.head = Some(new_node);
    }
}

#[derive(Clone)]
struct Node {
    val: i32,
    next: Option<Box<Node>>,
}

impl Node {
    fn new() -> Self {
        Self { val: 0, next: None }
    }
}

fn main() {
    let head = Some(Box::new(Node::new()));
    let mut list = LinkedList::new(head);

    list.add(6);
    list.add(4);
    list.add(7);

    let mut current = list.head;

    while let Some(curr) = current {
        println!("{}", curr.val);
        current = curr.next;
    }
}
