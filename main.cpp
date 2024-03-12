// I want to delete an element in the array with indexes and shift the array by taking place of the delete element.
// help me solve it

// bool toRemoveOrReplace(int array[][10], int rows, int columns, int rowIndexToRR,
//                         int columnIndexToRR, int action){

//     if (action == 1) {
//         array[rowIndexToRR][columnIndexToRR] = 0;  // Replace
//     } else if (action == 2) { 
//         // Shift elements to remove the element
//         for (int i = rowIndexToRR; i < rows - 1; i++) {  // Corrected loop bounds
//             array[i][columnIndexToRR] = array[i + 1][columnIndexToRR];
//         }

//         // After shifting, set the last element in the column to 0
//         array[rows - 1][columnIndexToRR] = 0; 
//     }
//     return true;
// }


bool toRemoveOrReplace(int array[][10], int rows, int columns, int rowIndexToRR,
                        int columnIndexToRR, int action){

    if (action == 1) {
        array[rowIndexToRR][columnIndexToRR] = 0;  // Replace
    } else if (action == 2) { 
        // Shift elements to remove the element
        for (int i = rowIndexToRR; i < rows - 1; i++) {  // Corrected loop bounds
            array[i][columnIndexToRR] = array[i + 1][columnIndexToRR];
        }

        // After shifting, set the last element in the column to 0
        array[rows - 1][columnIndexToRR] = 0; 
    }
    return true;
}