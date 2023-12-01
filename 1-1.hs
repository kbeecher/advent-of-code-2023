import Data.Char
import System.IO

firstDigit :: String -> Char
firstDigit []     = '0'
firstDigit (x:xs) = if isDigit x then x else firstDigit xs

lastDigit :: String -> Char
lastDigit s = firstDigit (reverse s)

calculateLine :: String -> Int
calculateLine s = read [firstDigit(s), lastDigit(s)]

calculateCalibration :: [String] -> Int
calculateCalibration []   = 0
calculateCalibration (l:ls) = calculateLine l + calculateCalibration ls


main :: IO ()
main =  do
    putStr "Result: "
    x <- getContents
    print(calculateCalibration (lines x))