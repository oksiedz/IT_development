/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Chess;

import java.awt.Color;
import java.util.ArrayList;

/**
 *
 * @author tt
 */
public class MyPlayer {

    private Color colour; //variable defining colour of the player
    private String name; //Name of the Player
    private int playerNum; //number of the player 1 - first, 2 - second
    //Player contains also figures - so we need to have table with all figures

//container for 16 objects which is owned by the player
    //MyChessman tab[] = new MyChessman[16]; //one method
    private ArrayList<MyChessman> tab = new ArrayList<MyChessman>(); //second method

    //constructor for MyPlayer
    public MyPlayer(Color colour, String Name, int playerNum) {
        this.colour = colour;
        this.name = Name;
        this.playerNum = playerNum;

        if (getPlayerNum() == 1) {
            //setting pawns
            for (int i = 0; i < 8; i++) {
                //creation of Pawns for Player
                tab.add(new MyPawn(colour, i, 6, i, playerNum)); //adding Pawns in second row in each column
            }
            //setting first rook
            tab.add(new MyRook(colour, 0, 7, 1, playerNum)); //first row, position one
            tab.add(new MyRook(colour, 7, 7, 2, playerNum)); //first row, position eight
            //setting Knights
            tab.add(new MyKnight(colour, 1, 7, 1, playerNum)); //first row, position two
            tab.add(new MyKnight(colour, 6, 7, 2, playerNum));//first row, position seven
            //setting Bishops
            tab.add(new MyBishop(colour, 2, 7, 1, playerNum));//first row, position three
            tab.add(new MyBishop(colour, 5, 7, 2, playerNum));//first row, position six
            //setting Queen
            tab.add(new MyQueen(colour, 3, 7, playerNum));//first row, position four
            //setting King
            tab.add(new MyKing(colour, 4, 7, playerNum));//first row, position five
        } else {
            //setting pawns
            for (int i = 0; i < 8; i++) {
                //creation of Pawns for Player
                tab.add(new MyPawn(colour, i, 1, i, playerNum)); //adding Pawns in second row in each column
            }
            //setting first rook
            tab.add(new MyRook(colour, 0, 0, 1, playerNum));
            tab.add(new MyRook(colour, 7, 0, 2, playerNum));
            //setting Knights
            tab.add(new MyKnight(colour, 1, 0, 1, playerNum));
            tab.add(new MyKnight(colour, 6, 0, 2, playerNum));
            //setting Bishops
            tab.add(new MyBishop(colour, 2, 0, 1, playerNum));
            tab.add(new MyBishop(colour, 5, 0, 2, playerNum));
            //setting Queen
            tab.add(new MyQueen(colour, 4, 0, playerNum));
            //setting King
            tab.add(new MyKing(colour, 3, 0, playerNum));
        }

    }

    public Color getColour() {
        return colour;
    }

    public void setColour(Color colour) {
        this.colour = colour;
    }

    public String getName() {
        return name;
    }

    public void setName(String Name) {
        this.name = Name;
    }

    public ArrayList<MyChessman> getTab() {
        return tab;
    }

    public void setTab(ArrayList<MyChessman> tab) {
        this.tab = tab;
    }

    public int getPlayerNum() {
        return playerNum;
    }

    public void setPlayerNum(int playerNum) {
        this.playerNum = playerNum;
    }

}
