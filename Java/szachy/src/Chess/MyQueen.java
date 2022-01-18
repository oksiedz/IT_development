/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Chess;

import java.awt.BasicStroke;
import java.awt.Color;
import java.awt.Graphics;
import java.awt.Graphics2D;

/**
 *
 * @author tt
 */
public class MyQueen extends MyChessman {
//class for Queen figure

    public MyQueen(Color colour, int x, int y, int playerNum) {
        super(colour, x, y, playerNum);
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
        g.drawString("Queen", getX() * b + b / 3, getY() * b + b / 2);
        //if the figure was clicked then it should be marked with new circle colour (this == ch from MyPanel
        if (this == MyPanel.ch) {
            g.setColor(Color.GREEN); //changing colour to green
            Graphics2D g2 = (Graphics2D) g;//conversion to Graphics2D to set stroke
            g2.setStroke(new BasicStroke(8));//setiing the width of the oval which we draw
            g.drawOval(getX() * b, getY() * b, b, b); //draving oval around the figure which was clicked
        }
    }

}
