package lib.havefun.mybrother;

public class Abdullah extends RashedKarim {
    private String gameName;
    private boolean lazy;
    private static boolean playingGame;

    public Abdullah() {
        
    }

    public Abdullah(boolean house, String houseName, boolean family, String gameName, boolean lazy, boolean playingGame) {
        super(house, houseName, family);
        this.gameName = gameName;
        this.lazy = lazy;
        Abdullah.playingGame = playingGame;
    }

    public void setPlayingGame(boolean playingGame) {
        Abdullah.playingGame = playingGame;
    }
    public boolean getPlayingGame() {
        return Abdullah.playingGame;
    }

    public static void Action() {
        if (Abdullah.playingGame == true) {
            RashedKarim.Action();
        } else {
            System.out.println("Survived");
        }
    }

    public void setLazy(boolean lazy) {
        this.lazy = lazy;
    }
    public boolean getLazy() {
        return lazy;
    }
    public void setGameName(String gameName) {
        this.gameName = gameName;
    }
    public String getGameName() {
        return gameName;
    }

    @Override
    public String toString() {
        Abdullah.Action();
        return super.toString()+" Abdullah \n[Game Name = " + gameName + "]\n[Lazy = " + lazy + "]\n" + "[Playing Game = " + playingGame + "]\n";
    }
}
