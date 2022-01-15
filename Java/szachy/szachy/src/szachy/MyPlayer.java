/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package szachy;

import java.awt.Color;
import java.util.ArrayList;

/**
 *
 * @author ja
 */
public class MyPlayer {
    Color color ;
    String name;

    //MyChessman tab[] = new MyChessman[16];
    ArrayList<MyChessman> tab2 = new ArrayList<MyChessman> ();

    public MyPlayer(Color color, String name) {
        this.color = color;
        this.name = name;
        if (color == Color.GREEN) 
        {
            for (int i = 0; i < 8; i++) 
            {   
                tab2.add(new MyPawn(color, i, 1));
            }
            tab2.add(new MyTower(color, 0, 0));
            tab2.add(new MyTower(color, 7, 0));
            tab2.add(new MyKing(color, 4, 0));
            tab2.add(new MyQueen(color, 3, 0));
            tab2.add(new MyHorse(color, 1, 0));
            tab2.add(new MyHorse(color, 6, 0));
            tab2.add(new MyBishop(color, 2, 0));
            tab2.add(new MyBishop(color, 5, 0));
        } else
        {
            for (int i = 0; i < 8; i++) 
            {   
                tab2.add(new MyPawn(color, i, 6));
            }
            tab2.add(new MyTower(color, 0, 7));
            tab2.add(new MyTower(color, 7, 7));
            tab2.add(new MyKing(color, 3, 7));
            tab2.add(new MyQueen(color, 4, 7));
            tab2.add(new MyHorse(color, 1, 7));
            tab2.add(new MyHorse(color, 6, 7));      
            tab2.add(new MyBishop(color, 2, 7));
            tab2.add(new MyBishop(color, 5, 7));            
        }            
    }

    public Color getColor() {
        return color;
    }

    public void setColor(Color color) {
        this.color = color;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public ArrayList<MyChessman> getTab2() {
        return tab2;
    }

    public void setTab2(ArrayList<MyChessman> tab2) {
        this.tab2 = tab2;
    }
    
    
}
