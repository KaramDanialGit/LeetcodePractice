abstract class GenericMap<T> {
  void registerValue<T>(T item, {T ? key});
  getValue<T>({T ? key});
}

mixin MapPrinter {
  Map inventory = <dynamic, dynamic>{};
  
  void printGenericMap() {
    this.inventory.forEach((key, val) => {
      print((key, val))
    });
  }
}

class MyMap extends GenericMap with MapPrinter {
  
  void registerValue<T>(T item, {T ? key}) {
    inventory[key ?? T] = item;
  }
  
  getValue<T>({T ? key}) {
    return inventory[key ?? T];
  }
}

MyMap globalMap = MyMap();

void main() {
  globalMap.registerValue<String>("Hello World");
  globalMap.registerValue(1, key: "Test");
  globalMap.registerValue(4, key: 2);
  
  var value = globalMap.getValue<String>();
  var value1 = globalMap.getValue(key: "Test");
  var value2 = globalMap.getValue(key: 2);
  
  
  print(value);
  print(value1);
  print(value2);
  
  var myVector = [for (int i = 0; i < 10; i++) i];
  print(myVector);
  
  globalMap.printGenericMap();
  
  String test = "Test";
  String newTest = "R" + test.substring(1, test.length);
  print(newTest);
}