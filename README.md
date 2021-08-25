# AI_Sudoku_Solver
This is a project which is the Application of Computer vision library opencv![Sudoku_Pic]


Given a partially filled 9×9 2D array ‘grid[9][9]’, the goal is to assign digits (from 1 to 9) to the empty cells so that every row, column, and subgrid of size 3×3 contains exactly one instance of the digits from 1 to 9. 








Procedure to make this project

1.Sudoku grid is pre-processed using image blurring (noise-removal), canny-edge detection and erosion + dilation.

2.Each cell of grid is seperated and stored using suitable contours.

3.The contour based cells are sorted in left-to-right and top-to-bottom manner.

3.The digits in cells are recognized using Python,opencv,numpy.

4.Final Step, the grid is stored in an 2d-array. The puzzle is solved using backtracking algorithm.








![Sudoku_Pic](https://user-images.githubusercontent.com/77828640/130758733-38cb1b41-164e-4bbc-99d5-8fee9486317c.png)-





Soduku is solved by Backtracking Algorithms 


1.Create a function that checks if the given matrix is valid sudoku or not. Keep Hashmap for the row, column and boxes. If any number has a frequency greater than 1 in the hashMap return false else return true

2.Create a recursive function that takes a grid and the current row and column index.

3.Check some base cases. If the index is at the end of the matrix, i.e. i=N-1 and j=N then check if the grid is safe or not, if safe print the grid and return true else return false. The other base case is when the value of column is N, i.e j = N, then move to next row, i.e. i++ and j = 0.

4.if the current index is not assigned then fill the element from 1 to 9 and recur for all 9 cases with the index of next element, i.e. i, j+1. if the recursive call returns true then break the loop and return true.

5.if the current index is assigned then call the recursive function with index of next element, i.e. i, j+1









package used here:-

1.Python

2.opencv Library

3.Tensorflow

4.Keras

Algorithm :- Backtaracking
