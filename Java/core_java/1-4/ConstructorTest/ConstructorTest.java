import java.util.*;

public class ConstructorTest{
	public static void main(String[] args){
		Employee[] staff = new Employee[3];

		staff[0] = new Employee("Harry", 400000);
		staff[1] = new Employee(600000);
		staff[2] = new Employee();

		for (Employee e : staff)
			System.out.println("name=" + e.getName() + ",id=" + e.getId() +
					",salary=" + e.getSalary());
	}
}

class Employee{
	private static int nextId;

	private int id;
	private String name = "";
	private double salary;

	static{
		Random generator = new Random();
		nextId = generator.nextInt(10000);
	}

	{
		id = nextId;
		nextId++;
	}
	public Employee(String name, double salary){
		this.name = name;
		this.salary = salary;
	}

	public Employee(){
	}

	public Employee(double salary){
		this("Employee #" + nextId, salary);
	}

	public String getName(){
		return name;
	}

	public int getId(){
		return id;
	}

	public double getSalary(){
		return salary;
	}
}
