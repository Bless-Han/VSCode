import java.time.*;

class Employee{
	private static int nextId = 1;
	private static int numberS = 0;
	private int id;
	private int number;
	private final String name;
	private double salary;
	private LocalDate hireDay;

	public Employee(String s, double d, int year, int month, int day){
		name = s;
		salary = d;
		hireDay = LocalDate.of(year, month, day);
		setId();
	}

	public static void main(String[] args){
		Employee e = new Employee("Romeo", 50000, 2003, 3, 31);
		e.raiseSalary(10);
		System.out.println(e.getName() + " " + e.getSalary());
	}

	public String getName(){
		return name;
	}

	public double getSalary(){
		return salary;
	}

	public LocalDate getHireDay(){
		return hireDay;
	}

	public void raiseSalary(double byPercent){
		double raise = salary * byPercent / 100;
		salary += raise;
	}

	private void setId(){
		id = nextId;
		nextId++;
		number = numberS;
		numberS += 10;
	}

	public static int getNextId(){
		return nextId;
	}
}
