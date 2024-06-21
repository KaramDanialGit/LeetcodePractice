use std::collections::HashMap;

trait InventoryManager<T> {
    fn new() -> Inventory<T>;
    fn add_item(&mut self, id: i32, item: T);
    fn remove_item(&mut self, id: i32);
}

struct Inventory<T> {
    inv_map: HashMap<i32, T>,
}

impl<T> InventoryManager<T> for Inventory<T> {
    fn new() -> Self {
        Inventory {
            inv_map: HashMap::new(),
        }
    }

    fn add_item(&mut self, id: i32, item: T) {
        self.inv_map.insert(id, item);
    }

    fn remove_item(&mut self, id: i32) {
        self.inv_map.remove(&id);
    }
}

fn main() {
    let mut my_inv: Inventory<String> = Inventory::new();
    my_inv.add_item(1, "Stehoscope".to_string());
    my_inv.add_item(2, "Heartrate Monitor".to_string());

    for (key, device) in my_inv.inv_map.iter() {
        println!("{:?}", device);
    }
}
