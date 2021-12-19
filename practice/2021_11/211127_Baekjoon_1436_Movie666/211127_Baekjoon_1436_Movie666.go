package main

import (
	"bufio"
	"fmt"
	"os"
)

// func main() {
// 	var n int
// 	count := 0
// 	r := bufio.NewReader(os.Stdin)
// 	w := bufio.NewWriter(os.Stdout)
// 	defer w.Flush()
// 	fmt.Fscan(r, &n)
// 	for i := 0; count < n; i++ {
// 		if countSix(i) > 0 {
// 			count++
// 		}
// 		if count == n {
// 			fmt.Fprint(w, i)
// 		}
// 	}
// }

// func countSix(n int) int {
// 	s := strconv.Itoa(n)
// 	return strings.Count(s, "666")
// }

func main() {
	var n int
	count := 1
	title := 666
	r := bufio.NewReader(os.Stdin)
	w := bufio.NewWriter(os.Stdout)
	defer w.Flush()
	fmt.Fscan(r, &n)
	for i := 1666; count < n; i++ {
		temp := i
		for temp >= 666 {
			if temp%1000 == 666 {
				count++
				break
			}
			temp /= 10
		}
		title = i
	}
	fmt.Fprint(w, title)
}
