import Data.Char
import Data.List
import System.IO

numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

-- Find a numString at beginning of string
findNumString :: [String] -> String -> Maybe Int
findNumString [] _ = Nothing
findNumString (n:ns) s = if (take (length n) s) == n 
    then elemIndex n numbers
    else findNumString ns s

-- Find a numString at end of string
findNumStringReverse :: [String] -> String -> Maybe Int
findNumStringReverse [] _ = Nothing
findNumStringReverse (n:ns) s = if (take (length n) (reverse s) ) == reverse n 
    then elemIndex n numbers
    else findNumStringReverse ns s

-- Try and get either first digit or first numString, going from left to right
getDigit :: String -> Int
getDigit (x:xs) = if isDigit x 
    then digitToInt x
    else case findNumString numbers (x:xs) of
        Just n  -> n
        Nothing -> getDigit xs

-- Try and get either first digit or first numString, going from right to left
getDigitReverse :: String -> Int
getDigitReverse s = if isDigit (last s)
    then digitToInt (last s)
    else case findNumStringReverse numbers s of
        Just n  -> n
        Nothing -> getDigitReverse (init s)


firstDigit :: String -> Int
firstDigit s  = getDigit s


lastDigit :: String -> Int
lastDigit s = getDigitReverse s

calculateLine :: String -> Int
calculateLine s = firstDigit(s) * 10 + lastDigit(s)

calculateCalibration :: [String] -> Int
calculateCalibration []   = 0
calculateCalibration (l:ls) = calculateLine l + calculateCalibration ls


main :: IO ()
main =  do
    putStr "Result: "
    x <- getContents
    print(calculateCalibration (Prelude.lines x))