/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Chess;

import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author tt
 */
public class TimeThread extends Thread {

    int number;

    public TimeThread(int number) {
        this.number = number;
    }

    @Override
    public void run() {

        System.out.println("Thread Number=" + number);
        //code for first thread
        if (number == 1) {
            while (ChessMainFrame.p1.getSecondsPlayed() != ChessMainFrame.gameLength) { //calculate time since the timer for Player1 won't reach time for the game
                if (ChessMainFrame.p1.getIsPlaying() == 1) {
                    ChessMainFrame.p1.setSecondsPlayed(ChessMainFrame.p1.getSecondsPlayed() + 1); //if it's Player 1 turn then add seconds
                } else {
                    ChessMainFrame.p1.setSecondsPlayed(ChessMainFrame.p1.getSecondsPlayed());//if it's not Player 1 turn then do not add seconds
                    System.out.println("Player1 is not playing");
                }
                System.out.println("secondsPlayed P1=" + ChessMainFrame.p1.getSecondsPlayed());
                try {
                    sleep(1000); //wait one second
                } catch (InterruptedException ex) {
                    Logger.getLogger(TimeThread.class.getName()).log(Level.SEVERE, null, ex);
                }
            }
        }
        //code for second thread
        if (number == 2) {
            while (ChessMainFrame.p2.getSecondsPlayed() != ChessMainFrame.gameLength) { //calculate time since the timer for Player2 won't reach time for the game
                if (ChessMainFrame.p2.getIsPlaying() == 1) {
                    ChessMainFrame.p2.setSecondsPlayed(ChessMainFrame.p2.getSecondsPlayed() + 1);//if it's Player 2 turn then add seconds
                } else {
                    ChessMainFrame.p2.setSecondsPlayed(ChessMainFrame.p2.getSecondsPlayed());//if it's not Player 1 turn then do not add seconds
                    System.out.println("Player2 is not playing");
                }
                System.out.println("secondsPlayed P2=" + ChessMainFrame.p2.getSecondsPlayed());
                try {
                    sleep(1000);
                } catch (InterruptedException ex) {
                    Logger.getLogger(TimeThread.class.getName()).log(Level.SEVERE, null, ex);
                }
            }

        }
        if (number == 3) {
            //refreshing the remaining time
            while (ChessMainFrame.p2.getSecondsPlayed() != ChessMainFrame.gameLength || ChessMainFrame.p1.getSecondsPlayed() != ChessMainFrame.gameLength) {
                ChessMainFrame.playedPlayerTime();
            }

        }
    }
}
