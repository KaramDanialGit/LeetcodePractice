// getit: 
// Register singltons with a runtime type or a string as a registration key
// retrieve a registered singleton via a runtime type or String
// the service locator should have static access such that it is available everywhere

abstract interface class GetIt {
  void register<T>(T instance, {String key});
  get<T>({String key});
}

class GetItClass implements GetIt {
  var instanceMap = <dynamic, dynamic>{};
  
  void register<T>(T instance, {String? key}) {
    instanceMap[key ?? T] = instance;
  }
  
  get<T> ({String? key}) {
    return instanceMap[key ?? T];  
  }
}

GetIt globalInstance = GetItClass();

void main() {
  globalInstance.register("Book", key: "myString");
  globalInstance.register("Book2");
  globalInstance.register("Book3");
  
  print(globalInstance.get(key: "myString"));
  print(globalInstance.get<String>());
}