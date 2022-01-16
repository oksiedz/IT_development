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
public class MyBishop extends MyChessman {
//Class for Bishop figure
private int bishopNo;
    public MyBishop(Color colour, int x, int y, int bishopNo) {
        super(colour, x, y);
        setBishopNo(bishopNo);
    }

    @Override
    public boolean IsMoveOk(int a, int b) {
        return true;
    }

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
        g.drawString("Bishop"+ " "+bishopNo, getX() * b + b / 3, getY() * b + b / 2);
    }

    public int getBishopNo() {
        return bishopNo;
    }

    public void setBishopNo(int bishopNo) {
        this.bishopNo = bishopNo;
    }

}
