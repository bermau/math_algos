package math_algos

object gcd {
    def main(args: Array[String]) {
    	if(args.length < 2){
    	    println("Requires two integers as parameters");
    		return
    	}
    	val num1 = args(0).toInt;
    	val num2 = args(1).toInt;
    	
    	println(gcd(num1,num2));
    }
    
    def gcd(num1: Int, num2: Int) : Int = {
        if(num2 == 0){
            return num1;
        }
        return gcd(num2, num1 % num2);
    }
}