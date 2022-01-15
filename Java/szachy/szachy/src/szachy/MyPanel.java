/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package szachy;

import java.awt.Color;
import java.awt.Graphics;
import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;
import javax.swing.JPanel;

/**
 *
 * @author ja
 */
public class MyPanel extends JPanel implements MouseListener{
    
    static MyChessman ch =null;
    MyPanel() {addMouseListener(this);}
    @Override
    public void paint(Graphics g) {
        super.paint(g);
        int b;
        if (getWidth() > getHeight()) {
            b = getHeight() / 8;
        } else {
            b = getWidth() / 8;
        }
        int p=0;
        for (int i = 0; i < 8; i++) {
            for (int j = 0; j < 8; j++) {
                if (p%2==0) {
                    g.setColor(Color.white);} else 
                    {g.setColor(Color.gray);}
                g.fillRect(i*b, j*b, b, b);
                p++;
            } p++;
        }
        if (ChessMainFrame.p1 != null) 
            {
               g.setColor(ChessMainFrame.p1.getColor());
               for (int i = 0; i < ChessMainFrame.p1.getTab2().size(); i++)                     
                {   //g.fillOval(ChessMainFrame.p1.getTab2().get(i).getX()*b, ChessMainFrame.p1.getTab2().get(i).getY()*b, b, b);
                    ChessMainFrame.p1.getTab2().get(i).drawChessman(g, b);
                
                }
            }
        if (ChessMainFrame.p2 != null) 
            {
               g.setColor(ChessMainFrame.p2.getColor());
               for (int i = 0; i < ChessMainFrame.p2.getTab2().size(); i++)                     
                {   //g.fillOval(ChessMainFrame.p1.getTab2().get(i).getX()*b, ChessMainFrame.p1.getTab2().get(i).getY()*b, b, b);
                    ChessMainFrame.p2.getTab2().get(i).drawChessman(g, b);
                }
            }

    }

    @Override
    public void mouseClicked(MouseEvent e) {
        //throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
        //ch = null;
        System.out.println(e.getX()+ " "+ e.getY()); 
        int x = e.getX();
        int y = e.getY();

        int b;
        if (getWidth() > getHeight()) {
            b = getHeight() / 8;
        } else {
            b = getWidth() / 8;
        }        
        int cx = x/b;
        int cy = y/b;
        System.out.println(cx+ " "+ cy); 

        if (ch == null)
        {
            if (ChessMainFrame.p1 != null) 
            {       
                for (int i = 0; i < ChessMainFrame.p1.getTab2().size(); i++) 
                { if ((ChessMainFrame.p1.getTab2().get(i).getX() == cx ) && (ChessMainFrame.p1.getTab2().get(i).getY() == cy ))
                    { ch = ChessMainFrame.p1.getTab2().get(i);
                    } 
                }
            }
            if (ChessMainFrame.p2 != null) 
            {       
                for (int i = 0; i < ChessMainFrame.p2.getTab2().size(); i++) 
                { if ((ChessMainFrame.p2.getTab2().get(i).getX() == cx ) && (ChessMainFrame.p2.getTab2().get(i).getY() == cy ))
                    { ch = ChessMainFrame.p2.getTab2().get(i);
                    } 
                }
            }            
            System.out.println(ch); 
        } else
        { 
            ch.setX(cx);
            ch.setY(cy);
            ch = null;
            repaint();
        }
        //w ismoveok sprawdzic czy ruch jest mozliwy
        
        
        
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
