package main

import "fmt"

func main() {
	var cases int 
	_, _ = fmt.Scanf("%d", &cases) // integer scanning

	// error handling has not been added as it wad indicated that script will be autotested.
	delegate(cases)
}

// for repeating for no. of cases
func delegate(cases int){
	if cases == 0{
		return
	}else{
		var array_length int 
		_, _ = fmt.Scanf("%d",&array_length)
		process(array_length, 0)
		delegate(cases-1)
	}
}

// for taking and processing input
func process(array_length int, sum int) {
	if array_length <= 0 {
		fmt.Println(sum)
		return
	}else{
		var number int
		fmt.Scanf("%d", &number)
		if number >0 {
			sum = sum + (number*number)
		}
		process(array_length-1, sum)
	}
}