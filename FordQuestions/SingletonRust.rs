use std::collections::HashMap;

trait GetIt<T>{
    fn register(&mut self, item: T, key: String);
    fn get_item(&self, key: String) -> Option<&T>;
}

struct Manager<T> {
    get_map: HashMap<String, T>
}

impl<T> GetIt<T> for Manager<T> {
    fn register(&mut self, item: T, key: String) {
        self.get_map.insert(key, item);
    }
    
    fn get_item(&self, key: String) -> Option<&T> {
        return self.get_map.get(&key);
    }
}

fn main() {
    let mut global_manager: Manager<i32> = Manager{get_map: HashMap::new()};
    global_manager.register(2, "String Object".to_string());
    let test_var = global_manager.get_item("String Object".to_string());
    
    if !test_var.is_none() {
        println!("{:}", test_var.unwrap());   
    }
}