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
public class MyKnight extends MyChessman {
//class for horse figure
private int knightNo;
    public MyKnight(Color colour, int x, int y , int knightNo) {
        super(colour, x, y);
        setKnightNo(knightNo);
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
        g.drawString("Knight"+" "+knightNo, getX() * b + b / 3, getY() * b + b / 2);
    }

    public int getKnightNo() {
        return knightNo;
    }

    public void setKnightNo(int knightNo) {
        this.knightNo = knightNo;
    }

}