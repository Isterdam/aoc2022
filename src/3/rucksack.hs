module Main where
import System.IO
import Data.List
import Data.Maybe

main :: IO ()
main = do
  handle <- openFile "in.txt" ReadMode
  contents <- hGetContents handle
  let rows = lines contents
  print $ score $ common_character rows
  print $ score2 $ rows
  hClose handle

score :: [Char] -> Int 
score s = sum [(+) 1 (fromJust $ elemIndex c letters) | c <- s]
  where letters = union ['a'..'z'] ['A'..'Z']

score2 :: [String] -> Int
score2 rows = score $ concat $ map (\group -> take 1 $ intersect3 group) (group_by_three rows)
  where intersect3 a = intersect (intersect (a !! 0) (a !! 1)) (a !! 2)

common_character :: [String] -> String
common_character = concat . map (\row -> take 1 $ intersect (fst $ halve row) (snd $ halve row))

group_by_three :: [a] -> [[a]]
group_by_three [] = []
group_by_three rows = (take 3 rows) : (group_by_three (drop 3 rows))

halve :: [a] -> ([a], [a]) 
halve xs = ((take s xs), (drop s xs))
    where s = (length xs) `div` 2