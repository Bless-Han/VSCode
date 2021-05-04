import java.io.*;
public class Employee {
	public String name;
	private double salary;
	public Employee (String empName){
		name = empName;
	}
	public void setSalary(double empSal){
		salary = empSal;
	}
	public void printEmp(){
		System.out.println("名字：" + name);
		System.out.println("薪水：" + salary);
	}

	public static void main(String[] args) {
		Employee empOne = new Employee("RUN00B");
		empOne.setSalary(1000.0);
		empOne.printEmp();
	}
}
