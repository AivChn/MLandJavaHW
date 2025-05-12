package net.aiv.main;
// Amishav Cohen
import java.util.ArrayList;
import java.util.Random;

public class GoL {

    public static void main(String[] args) {

        boolean[][] map = createStartingMap(8, 8);

        printMap(map);

        int rounds = 5;

        for (int r = 0; r < rounds; r++){
            ArrayList<Cell> aliveCells = turn(map);

            map = updateMap(aliveCells, map.length, map[0].length);

            printMap(map);
        }

    }

    public static boolean[][] updateMap(ArrayList<Cell> cells, int xSize, int ySize){

        boolean[][] newMap = new boolean[xSize][ySize];

        for(Cell c : cells) {
            newMap[c.getxPos()][c.getyPos()] = true;
        }

        return newMap;

    }

    public static void printMap(boolean[][] map){

        for (int i = 0; i < map.length; i++){
            for (int j = 0; j < map[i].length; j++){
                System.out.print((map[i][j] ? 1 : 0) + " ");
            }
            System.out.println(" ");
        }

        System.out.println("------------------------------------------");

    }

    public static boolean[][] createStartingMap(int xSize, int ySize){
        Random rn = new Random();
        boolean[][] map = new boolean[xSize][ySize];

        for (int i = 0; i < map.length; i++)
            for (int j = 0; j < map[i].length; j++){
                map[i][j] = rn.nextBoolean();
            }

        return map;

    }

    public static ArrayList<Cell> turn(boolean[][] map){

        ArrayList<Cell> aliveNeighbours = new ArrayList<>();

        for (int i = 0; i < map.length; i++)
            for (int j = 0; j < map[i].length; j++){
                byte neighbours = countNeighbours(map, i, j);
                Cell tmpCell = new Cell(map[i][j], neighbours, i, j);

                if (tmpCell.nextState){
                    aliveNeighbours.add(tmpCell);
                }

            }

        return aliveNeighbours;

    }

    public static byte countNeighbours(boolean[][] map, int x, int y){

        boolean[][] tmp = new boolean[map.length+2][map[0].length+2];

        for (int i = 0; i < map.length; i++){
            for (int j = 0; j < map[i].length; j++){
                tmp[i+1][j+1] = map[i][j];
            }
        }

        byte count = 0;

        for (int i = -1; i <= 1; i++){
            for (int j = -1; j <= 1; j++){
                count += tmp[x+i+1][y+j+1] ? (byte)  1 : 0;
            }
        }

        return count;

    }


    public static class Cell {

        private int xPos;
        private int yPos;
        private boolean nextState;

        public Cell(boolean state, byte neighboursCount, int xPos, int yPos) {

            this.xPos = xPos;
            this.yPos = yPos;
            this.updateNextState(state, neighboursCount);
        }

        public void updateNextState(boolean state, byte neighboursCount){
            if (state)
                this.nextState = neighboursCount == 3 || neighboursCount == 2;
            else
                this.nextState = neighboursCount == 3;
        }

        public int getxPos() {
            return xPos;
        }

        public int getyPos() {
            return yPos;
        }
    }

}