use std::fs::File;
use std::io::prelude::*;

struct Wepon{
    name: String, 
    damage: f32, 
    attack_delay: f32, 
    accuracy: f32, 
    crit: f32, 
}

impl Wepon{
    fn get_expect_value(&self) -> f32 {
        let delay = 60.0 / ((2.07 * 
            if self.attack_delay >= 1.0 { self.attack_delay }
            else { 1.0 - self.attack_delay }
             * 100.0).floor() / 100.0);

        let damage_weight = 0.2_f32;
        let crit_weight = 0.2_f32;
        let accurac_weight = 0.3_f32;
        let delay_weight = 0.3_f32;

        assert_eq!(1.0, (damage_weight + crit_weight + accurac_weight + delay_weight).floor(), "weight is not 100%");

        let num = 
            (self.damage * damage_weight) + 
            (self.crit * crit_weight) + 
            (self.accuracy * accurac_weight) + 
            (delay * delay_weight);
        println!("at line 31 delay weight: {:.2}", (delay * delay_weight));
        return (num * 100.0).floor() / 100.0;
    }
}

/*
fn check_type<T>(_: &T) {
    println!("{}", std::any::type_name::<T>());
}
*/

fn write_file(file_name: &str, content: String) -> std::io::Result<()>  {
    let mut file:File = File::create(file_name)?;
    file.write_all(&content.into_bytes())?;
    return Ok(());
}

fn read_file(file_name: &str) -> std::io::Result<String> {
    let mut file = File::open(file_name)?;
    let mut contents = String::new();
    file.read_to_string(&mut contents)?;
    return Ok(contents);
}

fn main(){
    let content = read_file("wepon_list.json").unwrap();
    let wepons_list = json::parse(&(content.to_owned())).unwrap();
    let mut new_wepon_list = Vec::new();
    let mut expect = String::new();
    for wepon in wepons_list["wepon_list"].members() {
        new_wepon_list.push(
            Wepon{
                name: String::from(wepon["name"].as_str().unwrap()),
                damage: wepon["damage"].as_f32().unwrap(),
                attack_delay: wepon["attack_delay"].as_f32().unwrap(),
                accuracy: wepon["accuracy"].as_f32().unwrap(),
                crit: wepon["crit"].as_f32().unwrap(),
            }
        );

        let get_wepon = &new_wepon_list[new_wepon_list.len() - 1];
        let wepon_name: &String = &get_wepon.name;
        expect.push_str(wepon_name.as_str());
        if wepon_name.len() < 20 {
            for _ in wepon_name.len()..20{
                expect.push(' ');
            }
        }
        else { break; }
        expect.push_str(": ");
        expect.push_str(get_wepon.get_expect_value().to_string().as_str());
        expect.push('\n');
    }

    let _ = write_file("expect.txt", expect);
}