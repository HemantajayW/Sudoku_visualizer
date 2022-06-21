public class sudoko_solve {
    public static void main(String[] args) {
        int[][] input = { { 7, 8, 0, 4, 0, 0, 1, 2, 0 }, { 6, 0, 0, 0, 7, 5, 0, 0, 9 }, { 0, 0, 0, 6, 0, 1, 0, 7, 8 },
                { 0, 0, 7, 0, 4, 0, 2, 6, 0 }, { 0, 0, 1, 0, 5, 0, 9, 3, 0 }, { 9, 0, 4, 0, 6, 0, 0, 0, 5 },
                { 0, 7, 0, 3, 0, 0, 0, 1, 2 }, { 1, 2, 0, 0, 0, 7, 4, 0, 0 }, { 0, 4, 9, 2, 0, 6, 0, 0, 7 } };

        printBoard(input);
        System.out.println("Solution: ");
        if (solve(input)) {
            printBoard(input);
        }
    }

    static boolean solve(int[][] arr) {
        // for(int i=0;i<arr.length;i++){
        // for(int k=0;k<arr.length;k++){
        // if(arr[i][k])
        // }
        // }
        int i = 0;
        int k = 0;
        loop: {
            for (i = 0; i < arr.length; i++) {
                for (k = 0; k < arr.length; k++) {
                    // System.out.println(arr[i][k]);
                    if (arr[i][k] == 0) {
                        break loop;
                    }
                }
            }
        }
        if (i == 9 && k == 9) {
            return true;
        } else {
            for (int ele = 1; ele <= 9; ele++) {
                if (!(checkColumn(k, arr, ele) || checkRow(i, arr, ele) || checkSquare(i, k, arr, ele))) {
                    arr[i][k] = ele;
                    if (solve(arr)) {
                        return true;
                    }
                    arr[i][k] = 0;
                }
            }

        }

        return false;

    }

    static boolean checkRow(int i, int[][] arr, int ele) {
        for (int k = 0; k < 9; k++) {
            if (arr[i][k] == ele) {
                return true;
            }
        }
        return false;

    }

    static boolean checkColumn(int i, int[][] arr, int ele) {
        for (int k = 0; k < 9; k++) {
            if (arr[k][i] == ele) {
                return true;
            }
        }
        return false;

    }

    static boolean checkSquare(int row, int col, int[][] arr, int ele) {
        row = (row) / 3;
        col = (col) / 3;
        row = row * 3;
        col = col * 3;
        // System.out.println(row+" "+col);
        for (int i = row; i < row + 3; i++) {
            for (int k = col; k < col + 3; k++) {
                if (arr[i][k] == ele) {
                    return true;
                }
            }
        }
        return false;

    }

    static void printBoard(int[][] arr) {
        for (int i = 0; i < arr.length; i++) {
            for (int k = 0; k < arr[0].length; k++) {
                if (k % 3 == 0 && k != 0) {
                    System.out.print("| ");
                }
                System.out.print(arr[i][k] + " ");
            }
            System.out.println();
            if ((i + 1) % 3 == 0 && i != 8) {
                System.out.println("---------------------");
            }

        }

    }
}
