/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Chess;

import java.awt.Color;
import java.awt.Graphics;

/**
 *
 * @author tt
 */
public class MyPawn extends MyChessman {
private int pawnNo;
    public MyPawn(Color color, int x, int y, int pawnNo) {
        super(color, x, y); //constructor from Parent Class MyChessman
        setPawnNo(pawnNo+1);
    }

    public int getPawnNo() {
        return pawnNo;
    }

    public void setPawnNo(int pawnNo) {
        this.pawnNo = pawnNo;
    }

    @Override
    public boolean IsMoveOk(int a, int b) {
        return true;
    }
    //Class for Pawn

    @Override
    public void drawChessman(Graphics g, int b) {
        g.setColor(getColour());//setting the colour to the Player's colour
        g.fillOval(getX() * b, getY() * b, b, b); //drawing oval shape as a figure
        //setting the colour to the opposite colour to the Player's colour
        if (getColour() == Color.WHITE) {
            g.setColor(Color.BLACK);
        } else {
            g.setColor(Color.WHITE);
        }
        //drawing name of the figure
        g.drawString("Pawn"+" "+pawnNo, getX() * b + b / 3, getY() * b + b / 2);

    }
}