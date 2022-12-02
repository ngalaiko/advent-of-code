package main

import "fmt"

func main() {
	sum1 := 0
	sum2 := 0
	for i := 372037; i < 905157; i++ {
		met := map[rune]int{}
		double := false
		decreases := false
		var last rune
		for _, d := range fmt.Sprint(i) {
			if met[d] > 0 {
				double = true
			}
			met[d]++

			if d < last {
				decreases = true
			}
			last = d
		}

		ok := false
		for d := range met {
			if met[d] == 2 {
				ok = true
			}
		}

		if double && !decreases {
			sum1++
		}
		if double && !decreases && ok {
			sum2++
		}
	}

	fmt.Println(sum1, sum2)
}
