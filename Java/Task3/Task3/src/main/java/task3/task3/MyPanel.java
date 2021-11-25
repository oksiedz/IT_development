/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package task3.task3;

import java.awt.Color;
import java.awt.Graphics;
import javax.swing.JPanel;

/**
 *
 * @author tt
 */
public class MyPanel extends JPanel {
    int ax1;
    int ay1;
    int ax2;
    int ay2;
    int ax3;
    int ay3;
    int ax4;
    int ay4;

    
    
    public void setParams(int ax1, int ay1, int ax2, int ay2, int ax3, int ay3, int ax4, int ay4) {
        this.ax1 = ax1;
        this.ay1 = ay1;
        this.ax2 = ax2;
        this.ay2 = ay2;
        this.ax3 = ax3;
        this.ay3 = ay3;
        this.ax4 = ax4;
        this.ay4 = ay4;
    }
     

    @Override
    public void paint(Graphics g) {
        super.paint(g); //To change body of generated methods, choose Tools | Templates.
        //g.setColor(Color.red);
        
        int x[] = {ax1, ax2, ax3, ax4};
        int y[] = {ay1, ay2, ay3, ay4};
        int noofpoints = 4;
        g.drawPolygon(x, y, noofpoints);
        /*
g.setColor(new Color(123,132,13));
        
        
     // g.drawLine(20, 20, 67, 76);
     // g.drawLine(JOkno.x1, JOkno.y1, JOkno.x2, JOkno.y2);     
        g.drawLine(ax1, ay1, ax2, ay2);
        g.drawLine(ax2, ay2, ax3, ay3);
        g.drawLine(ax3, ay3, ax4, ay4);
        g.drawLine(ax4, ay4, ax1, ay1);
*/
    }
    
    
    
    
    
}
