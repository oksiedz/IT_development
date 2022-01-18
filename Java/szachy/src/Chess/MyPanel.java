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
public class MyPanel extends JPanel implements MouseListener {//mouselsitener is an abstract listener

    static MyChessman ch = null;//creating object which will contain the figure on which we clicked

    public MyPanel() {
        addMouseListener(this); //we added the Panel as a tool to listen to mouse listener
    }

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

    @Override
    public void mouseClicked(MouseEvent e) { //e - event

        //ch = null; //by default we don't have anything clicked
        //System.out.println("X="+e.getX()+";Y="+e.getY());//returning location of click
        //checking if the click was done on one of the figure
        int x = e.getX();
        int y = e.getY();
        //assignment of field width/height on the board
        int b; //variable to handle 1/8 of panel to paint the board
        //setting the value of b
        if (getWidth() > getHeight()) {
            b = getHeight() / 8;
        } else {
            b = getWidth() / 8;
        }
        //index of field that we clicked
        int cx = x / b; //number of column which we have clicked
        int cy = y / b; //number of row which we have clicked
        System.out.println("X=" + x + ";cx=" + cx + ";Y=" + y + ";cy=" + cy + ";b=" + b);//returning location of click
        if (ch == null) { //if we don't have marked any figure then we are checking it

            if (ChessMainFrame.p1 != null) {
                //location we should divide by the b and check in the player container there is figure with such location
                //check if we clicked if the field on which we clicked is assigned to the one of the objects (figures) of the player
                for (int i = 0; i < ChessMainFrame.p1.getTab().size(); i++) {
                    if ((ChessMainFrame.p1.getTab().get(i).getX() == cx) && (ChessMainFrame.p1.getTab().get(i).getY() == cy)) {
                        ch = ChessMainFrame.p1.getTab().get(i); //if in container of figures there is object which have same location as click then assigned as ch
                    }

                }
            }
            if (ChessMainFrame.p2 != null) {
                //location we should divide by the b and check in the player container there is figure with such location
                //check if we clicked if the field on which we clicked is assigned to the one of the objects (figures) of the player
                for (int i = 0; i < ChessMainFrame.p2.getTab().size(); i++) {
                    if ((ChessMainFrame.p2.getTab().get(i).getX() == cx) && (ChessMainFrame.p2.getTab().get(i).getY() == cy)) {
                        ch = ChessMainFrame.p2.getTab().get(i); //if in container of figures there is object which have same location as click then assigned as ch
                    }

                }
            }
            //check if we hit the figure
            System.out.println(ch);
            System.out.println("PlayerNumber="+ch.playerNum);
            repaint(); //repaint the stage to check show the marked figure
        } else { //if we have already figure clicked, then in next click we have to indicate the new location of the figure

            if (cx >= 8 || cy >= 8) {
                System.out.println("Incorrect movement.");
            } else {

                //capture mechanism                
                MyChessman mch = null;
                //let's check if on the field that we want to land is already a figure which should be captured in such case
                if (ChessMainFrame.p1 != null) {
                    //location we should divide by the b and check in the player container there is figure with such location
                    //check if we clicked if the field on which we clicked is assigned to the one of the objects (figures) of the player
                    for (int i = 0; i < ChessMainFrame.p1.getTab().size(); i++) {
                        if ((ChessMainFrame.p1.getTab().get(i).getX() == cx) && (ChessMainFrame.p1.getTab().get(i).getY() == cy)) {
                            mch = ChessMainFrame.p1.getTab().get(i); //if in container of figures there is object which have same location as click then assigned as ch
                        }

                    }
                }
                if (ChessMainFrame.p2 != null) {
                    //location we should divide by the b and check in the player container there is figure with such location
                    //check if we clicked if the field on which we clicked is assigned to the one of the objects (figures) of the player
                    for (int i = 0; i < ChessMainFrame.p2.getTab().size(); i++) {
                        if ((ChessMainFrame.p2.getTab().get(i).getX() == cx) && (ChessMainFrame.p2.getTab().get(i).getY() == cy)) {
                            mch = ChessMainFrame.p2.getTab().get(i); //if in container of figures there is object which have same location as click then assigned as ch
                        }

                    }
                }
                //ch - figure which we are moving, mch - figure which is standing on the field where we want to land
                

                ch.setX(cx); //assigning as X cx - so new x location
                ch.setY(cy); //assigning as Y cy - so new y location
                ch = null; //null as ch cause now the figure won't be marked
                repaint(); //refresh the board
            }
        }
    }

    @Override
    public void mousePressed(MouseEvent e) {
        //throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }

    @Override
    public void mouseReleased(MouseEvent e) {
        //throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }

    @Override
    public void mouseEntered(MouseEvent e) {
        //throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }

    @Override
    public void mouseExited(MouseEvent e) {
        //throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }
}
