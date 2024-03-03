use std::io;
fn main() {
    println!("guess a number from 1 to 10");
    println!("input your guess:");
    let mut guess = String::new(); // if no mut than just read only
    io::stdin()
        .read_line(&mut guess)
        .expect("Faiiled to read line");
    
    println!("you guessed: {guess}")
}