package dsa_golang

func nextGreaterElement(nums1 []int, nums2 []int) []int {
    nge := make(map[int]int)
    stack := []int{}
    for i := len(nums2) - 1; i > -1 ; i-- {
        for len(stack) > 0 && nums2[i] > stack[len(stack) - 1]{
            stack = stack[:len(stack) - 1]
        }
        if len(stack) == 0 {
            nge[nums2[i]] = -1
        } else {
            nge[nums2[i]] = stack[len(stack)-1]
        }
        stack = append(stack, nums2[i])
    }
    for i := range nums1 {
        nums1[i] = nge[nums1[i]]
    }
    return nums1
}