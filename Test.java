import java.util.Vector;

class ThreadTest implements Runnable{
    private String name;
    public ThreadTest(String name){
        this.name=name;
    }
    @Override
    public void run() {
        for(int i=0;i<10;i++){
            /*if (Thread.currentThread().isInterrupted()) {
                System.out.print("Interrupted\n");
                break;
            }*/
            System.out.print(name+":\t"+i+"\n");
            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                System.out.print(Thread.currentThread().getName()+"\tIsInterrupted\n");
                break;
                //e.printStackTrace();
            }
            /*Thread.yield();*/
        }

    }
}
public class Test {
    public static void main(String[] args){
        /*new Thread(new ThreadTest("A")).start();
        new Thread(new ThreadTest("B")).start();
        new Thread(new ThreadTest("C")).start();*/
        Vector vector = new Vector();
        for(int i=0;i<64;i++){
            Thread thread=new Thread(new ThreadTest(String.valueOf(i)));
            thread.start();
            vector.add(thread);
            if((i+1) % 4 == 0){
                System.out.print("Now Join\n");
                for(int x=0;x<i+1;x++){
                    Thread th =(Thread)vector.get(x);
                    System.out.print(th.getName()+"\n");
                    try {
                        th.join(1000);
                        if(th.isAlive()){
                            th.interrupt();
                        }
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }
                }
            }
        }
    }
}
