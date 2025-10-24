pub fn sum(xs:&[i32])->i32{ xs.iter().copied().sum() }
pub fn clamp(v:i32,lo:i32,hi:i32)->i32{ if v<lo{lo}else if v>hi{hi}else{v} }
#[cfg(test)]mod t{use super::*; #[test]fn ok(){assert_eq!(sum(&[1,2,3]),6); assert_eq!(clamp(10,0,5),5);}}
