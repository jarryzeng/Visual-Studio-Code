struct Student{
    name: String,
    age: u8,
    sex: Sex,
    physical_defects: CongenitalDefects,
}

impl Student{
    fn get_name(&self){
        println!("my name is {}!", self.name);
    }

    fn get_age(&self){
        println!("i'm {} years old right now!", self.age);
    }

    fn up_age(&mut self){
        self.age += 1;
    }

    fn say_hellow(){
        println!("hello!");
    }
}

impl Clone for Student{
    fn clone(&self) -> Student{
        return Student{
            name: self.name.clone(),
            age: self.age.clone(),
            sex: self.sex.clone(),
            physical_defects: self.physical_defects.clone(),
        };
    }
}
impl Drop for Student{
    fn drop(&mut self){
        println!("{} is freeze now", self.name);
    }
}

enum Sex{
    Male,
    Female,
    Error(String),
}

impl Clone for Sex{
    fn clone(&self) -> Sex{
        let respone: Sex;
        match self{
            Sex::Male => respone = Sex::Male,
            Sex::Female => respone = Sex::Female,
            _ => respone = Sex::Error(String::from("unknow error")),
        }
        return respone;
    }
}
impl Sex{
    fn check_sex(&self, sex: &Sex){
        match sex{
            Sex::Male => println!("is a boy"),
            Sex::Female => println!("is a girl"),
            Sex::Error(message) => println!("{}", message),
        }
    }
}

enum CongenitalDefects{
    None,
    // Head,   
    // Hand(u8),
    Body,
    // Leg(u8),
    Error(String),
}

impl Clone for CongenitalDefects{
    fn clone(&self) -> CongenitalDefects{
        let respone: CongenitalDefects;
        match self{
            CongenitalDefects::None => respone = CongenitalDefects::None,
            // CongenitalDefects::Head => respone = CongenitalDefects::Head,   
            // CongenitalDefects::Hand(hands) => respone = CongenitalDefects::Hand(hands),
            CongenitalDefects::Body => respone = CongenitalDefects::Body,
            // CongenitalDefects::Leg(legs) => respone = CongenitalDefects::Leg(legs),
            _ => respone = CongenitalDefects::Error(String::from("unknow error")),
        }
        return respone;
    }
}
impl CongenitalDefects{
    fn check_defects(&self, defects: &CongenitalDefects){
        match defects{
            CongenitalDefects::None => println!("is healthy!"),
            // CongenitalDefects::Head => println!("head..."),
            // CongenitalDefects::Hand() => println!("hand..."),
            CongenitalDefects::Body => println!("body..."),
            // CongenitalDefects::Leg() => println!("leg..."),
            CongenitalDefects::Error(message) => println!("{}", message),
        }
    }
}

fn older<'a>(first_student: &'a Student, seconed_student: &'a Student) -> Student {
    if first_student.age > seconed_student.age{
        return first_student.clone();
    }
    else{
        return seconed_student.clone();
    }
}

fn main() {
    Student::say_hellow();

    let mut student_1 = Student{
        name: String::from("Lily"),
        age: 8,
        sex: Sex::Female,
        physical_defects: CongenitalDefects::None
    };
    
    let student_2 = Student{
        name: String::from("Jhon"),
        age: 15,
        sex: Sex::Male,
        physical_defects: CongenitalDefects::Body
    };
    
    println!("-------------");

    {
        let mut older_student: Student = older(&student_1, &student_2);
        older_student.get_name();
        older_student.up_age();
        older_student.get_age();
        older_student.sex.check_sex(&older_student.sex);
        older_student.physical_defects.check_defects(&older_student.physical_defects);
        println!("----older----");
    }

    student_1.get_name();
    student_1.up_age();
    student_1.get_age();
    student_1.sex.check_sex(&student_1.sex);
    student_1.physical_defects.check_defects(&student_1.physical_defects);
    println!("----student1----");
    student_2.get_name();
    student_2.get_age();
    student_2.sex.check_sex(&student_2.sex);
    student_2.physical_defects.check_defects(&student_2.physical_defects);
    println!("----student2----");
}