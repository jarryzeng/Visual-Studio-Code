struct Student{
    name: String,
    age: u8,
    grade: u8,
}

impl Student{
    fn get_name(&self){
        println!("my name is {}!", self.name);
    }

    fn get_age(&self){
        println!("i'm {} years old right now!", self.age);
    }

    fn get_grade(&self){
        println!("i'm {} grade!", self.grade);
    }

    fn up_age(&mut self){
        self.age += 1;
    }

    fn up_grade(&mut self){
        self.grade += 1;
    }

    fn say_hellow(){
        println!("hello!");
    }
}

impl Clone for Student{
    fn clone(&self) -> Self{
        return Student{
            name: self.name.clone(),
            age: self.age.clone(),
            grade: self.grade.clone(),
        };
    }
}

impl Drop for Student{
    fn drop(&mut self){
        println!("{} is freeze now", self.name);
    }
}

fn older<'a>(first_student: &'a Student, seconed_student: &'a Student) -> &'a Student {
    if first_student.age > seconed_student.age{
        return first_student;
    }
    else{
        return seconed_student;
    }
}

fn main() {
    Student::say_hellow();

    let mut student_1 = Student{
        name: String::from("Lily"),
        age: 8,
        grade: 1,
    };
    
    let mut student_2 = Student{
        name: String::from("Jhon"),
        age: 15,
        grade: 9,
    };
    
    println!("-------------");

    {
        let older_student: &Student = older(&student_1, &student_2);
        older_student.get_name();
        older_student.get_age();
        older_student.get_grade();
        println!("----older----");
    }

    student_1.get_name();
    student_1.up_age();
    student_1.get_age();
    student_1.get_grade();
    println!("----student1----");
    student_2.get_name();
    student_2.get_age();
    student_2.up_grade();
    student_2.get_grade();
    println!("----student2----");
}
