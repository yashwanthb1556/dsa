package dsa_golang

import (
	"fmt"
)

func main() {
	nums1 := []int{4, 1, 2}
	nums2 := []int{1, 3, 4, 2}
	result := nextGreaterElement(nums1, nums2)
	fmt.Println(result) // Output: [-1, 3, -1]
}
