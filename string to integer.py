class Solution:
    def myAtoi(self, s):
        # Step 0: Define 32-bit integer bounds
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        # Step 1: Remove leading whitespaces
        s = s.lstrip()
        if not s:
            return 0

        # Step 2: Determine the sign
        sign = 1
        if s[0] == '-':
            sign = -1
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]

        # Step 3: Read digits
        result = 0
        for char in s:
            if char.isdigit():
                result = result * 10 + int(char)
                # Step 4: Handle overflow immediately
                if sign * result < INT_MIN:
                    return INT_MIN
                if sign * result > INT_MAX:
                    return INT_MAX
            else:
                break

        return sign * result

# Example usage:
sol = Solution()
print(sol.myAtoi("42"))          # Output: 42
print(sol.myAtoi("   -042"))     # Output: -42
print(sol.myAtoi("1337c0d3"))    # Output: 1337
print(sol.myAtoi("0-1"))         # Output: 0
print(sol.myAtoi("words and 987")) # Output: 0
