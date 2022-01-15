/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Chess;

import java.awt.Color;
import java.awt.Graphics;
import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;
import javax.swing.JPanel;

/**
 *
 * @author ja
 */
public class MyPanel extends JPanel {

    @Override
    public void paint(Graphics g) {
        super.paint(g);

        if (ChessMainFrame.p1 != null) {
            ///painting the board
            int b; //variable to handle 1/8 of panel to paint the board
            //setting the value of b
            if (getWidth() > getHeight()) {
                b = getHeight() / 8;
            } else {
                b = getWidth() / 8;
            }
            int p = 0; //additional variable to print the colours of the board
            for (int i = 0; i < 8; i++) {
                for (int j = 0; j < 8; j++) {
                    if (p % 2 == 0) {
                        g.setColor(new Color(255, 229, 204)); //light brown
                    } else {
                        g.setColor(new Color(204, 102, 0)); //darker brown
                    }
                    g.fillRect(i * b, j * b, b, b);
                    p++;
                }
                p++;
            }

            //painting the figures for player
            g.setColor(ChessMainFrame.p1.getColour()); //setting colour from the Player
            for (int i = 0; i < ChessMainFrame.p1.getTab().size(); i++) { //i<ChessMainFrame.p1.getTab().size() - printing all figures from container of 
                //g.fillOval(ChessMainFrame.p1.getTab().get(i).getX()*b, ChessMainFrame.p1.getTab().get(i).getY()*b, b, b); //ChessMainFrame.p1.getTab().get(i).getX() -- takes X (column) value from figure of from the container of figures from p1
                ChessMainFrame.p1.getTab().get(i).drawChessman(g, b);
            }
            g.setColor(ChessMainFrame.p2.getColour()); //setting colour from the Player
            for (int i = 0; i < ChessMainFrame.p2.getTab().size(); i++) { //i<10 - printing 10 first figures
                //g.fillOval(ChessMainFrame.p1.getTab().get(i).getX()*b, ChessMainFrame.p1.getTab().get(i).getY()*b, b, b); //ChessMainFrame.p1.getTab().get(i).getX() -- takes X (column) value from figure of from the container of figures from p1
                ChessMainFrame.p2.getTab().get(i).drawChessman(g, b);
            }
        }

    }
}
