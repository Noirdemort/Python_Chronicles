package main
import (
	"bufio"
	"strconv"
	"strings"
	"fmt"
	"os"
	)

func main() {
	reader := bufio.NewReader(os.Stdin)
	for true {
		fmt.Println("Enter hex to convert or -1 to exit")
		text, _ := reader.ReadString('\n')
		text = strings.Replace(text, "\n", "", -1)

		if text == "-1" || text == ""{
			fmt.Println("Exiting...")
			os.Exit(0)
		}

		letters := strings.Split(text, "")

		if len(letters) != 6 {
			fmt.Println("Invalid hex!")
			continue
		}

		if s, err := strconv.ParseUint(letters[0]+letters[1], 16, 64); err == nil {
			fmt.Printf("red: %v\n", s)
		} else {
			fmt.Println("Invalid hex!")
			continue
		}
		if s, err := strconv.ParseUint(letters[2] + letters[3], 16, 64); err == nil {
			fmt.Printf("green: %v\n", s)
		}else {
			fmt.Println("Invalid hex!")
			continue
		}

		if s, err := strconv.ParseUint(letters[4]+letters[5], 16, 64); err == nil {
			fmt.Printf("blue: %v\n", s)
		} else {
			fmt.Println("Invalid hex!")
			continue
		}
	}
}
