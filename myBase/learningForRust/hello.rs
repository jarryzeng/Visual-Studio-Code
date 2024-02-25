fn main(){
    use std::io::{stdout, Write};
    
    let mut lock = stdout().lock();
    writeln!(lock, "hello world").unwrap();
}