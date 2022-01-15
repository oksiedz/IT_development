/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package szachy;

import java.awt.Color;
import java.awt.Graphics;


/**
 *
 * @author ja
 */
public class MyKing extends MyChessman {

    public MyKing(Color color, int x, int y) {
        super(color, x, y);
    }
    @Override
    public boolean isMoveOk(int a, int b) {
        return true;
    }

    @Override
    public void drawChessman(Graphics g, int b) {
        g.setColor(getColor());
        g.fillOval(getX()*b, getY()*b, b, b);
        g.setColor(Color.BLACK);
        g.drawString("K", getX()*b+b/2, getY()*b+b/2);
        
    }
    
}
