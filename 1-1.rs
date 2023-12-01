use std::io;

fn first_digit(line: &str) -> u32
{
    for c in line.chars() {
        if c.is_digit(10) {
            return c.to_digit(10).unwrap();
        }
    }

    return 0;
}

fn last_digit(line: &str) -> u32
{
    return first_digit(line.chars().rev().collect::<String>().as_str());
}

fn calculate_line(line: &str) -> u32
{
    return (first_digit(line) * 10) + last_digit(line);
}

fn main() {
    let lines = io::stdin().lines();
    let mut calibrations = Vec::new();

    for line in lines {
        calibrations.push(calculate_line(line.unwrap().as_str()));
    }

    println!("{}", calibrations.into_iter().reduce(|acc, e| acc + e).unwrap());
}