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
public abstract class MyChessman {
    private Color color;
    private int x; //polozenie
    private int y; //polozenie na planszy

    public MyChessman(Color color, int x, int y) {
        this.color = color;
        this.x = x;
        this.y = y;
    }

    public int getY() {
        return y;
    }

    public void setY(int y) {
        this.y = y;
    }

    public Color getColor() {
        return color;
    }

    public void setColor(Color color) {
        this.color = color;
    }

    public int getX() {
        return x;
    }

    public void setX(int x) {
        this.x = x;
    }
    public abstract boolean isMoveOk(int a, int b);
    public abstract void drawChessman(Graphics g, int b);
    
}
