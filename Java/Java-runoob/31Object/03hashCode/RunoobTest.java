class RunoobTest {
    public static void main(String[] args) {
 
        // Object 使用 hashCode()
        Object obj1 = new Object();
 
        // obj1 赋值给 obj2
        Object obj2 = obj1;
 
        // 判断两个对象是否相等
        System.out.println(obj1.equals(obj2)); // true
 
        // 获取 obj1 与 obj2 的哈希值
        System.out.println(obj1.hashCode()); // 225534817 
        System.out.println(obj2.hashCode()); // 225534817
 
    }
}
