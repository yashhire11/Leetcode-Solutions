class Solution {
    public String fractionToDecimal(int numerator, int denominator) {
        // Handle cases with zero numerator or simple division
        if (numerator == 0) return "0";
        if (denominator == 0) return ""; // Undefined, but should be handled gracefully

        StringBuilder result = new StringBuilder();

        // Determine if the result is negative
        boolean isNegative = (numerator < 0) ^ (denominator < 0);
        if (isNegative) result.append("-");

        // Work with absolute values to simplify the logic
        long absNumerator = Math.abs((long) numerator);
        long absDenominator = Math.abs((long) denominator);

        // Compute the integral part
        long integralPart = absNumerator / absDenominator;
        result.append(integralPart);

        // Compute the remainder
        long remainder = absNumerator % absDenominator;
        if (remainder == 0) return result.toString(); // No fractional part

        result.append(".");

        // Compute the fractional part
        Map<Long, Integer> remainderMap = new HashMap<>();
        StringBuilder fractionalPart = new StringBuilder();

        while (remainder != 0) {
            // If the remainder has been seen before, it's a repeating fraction
            if (remainderMap.containsKey(remainder)) {
                int repeatIndex = remainderMap.get(remainder);
                fractionalPart.insert(repeatIndex, "(");
                fractionalPart.append(")");
                break;
            }

            // Record the position of this remainder
            remainderMap.put(remainder, fractionalPart.length());

            // Multiply the remainder by 10 and append the quotient
            remainder *= 10;
            fractionalPart.append(remainder / absDenominator);
            remainder %= absDenominator;
        }

        result.append(fractionalPart.toString());
        return result.toString();
    }
}
