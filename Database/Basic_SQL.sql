CREATE TABLE employes (
	ID SERIAL PRIMARY KEY,
	Name VARCHAR(50),
	Age INT,
	Salary DECIMAL(10, 2),
	City VARCHAR(50),
	Country VARCHAR(50)
);

INSERT INTO employees (Name, Age, Salary, City, Country) VALUES
('Ravi', 21, 2000.00, 'Maryland', 'Germany'),
('Farhan', 30, 5000.00, 'New York', 'USA'),
('Teja', 28, 4500.00, 'Muscat', 'Dubai'),
('Yash', 27, 2500.00, 'Kolkata', 'India'),
('Ashin', 26, 3500.00, 'Bhopal', 'India');