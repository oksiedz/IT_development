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
public abstract class MyChessman { //class is abstract cause it contains abstract methods
    //base class for all other types of the figures

    private Color colour; //colour of the figure
    //location of the figure
    private int x;
    private int y;

    public MyChessman(Color colour, int x, int y) {
        this.colour = colour;
        this.x = x;
        this.y = y;
    }

    public int getY() {
        return y;
    }

    public void setY(int y) {
        this.y = y;
    }

    public Color getColour() {
        return colour;
    }

    public void setColour(Color colour) {
        this.colour = colour;
    }

    public int getX() {
        return x;
    }

    public void setX(int x) {
        this.x = x;
    }

    public abstract boolean IsMoveOk(int a, int b); //this is abstract method which should be overwritten by child classes, a, b - new locations, it return true or false if the move is correct

    public abstract void drawChessman(Graphics g, int b);//this is abstract method to paint the figure, b - lenght of the rectangle defining field
}
