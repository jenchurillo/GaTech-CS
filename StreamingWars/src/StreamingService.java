import java.util.HashSet;
import java.util.HashMap;


public class StreamingService {

    //attribute declarations

    private String shortName;
    private String longName;
    private int numOfMoviesOffered = 0;
    private int numOfPPVOffered = 0;
    private int flatRateSubscriptionPrice = 0;
    //private String[][] singleViewPrice;
    //private String[][] directoryOfEvents;
    //private HashMap<PPV,Double> singleViewPrice = new HashMap<PPV, Double>();
    //private HashMap<String, String> directoryOfEvents = new HashMap<String, String>();
    private Event[] directoryOfMovieEvents = new Event[20];
    private Event[] directoryOfPPVEvents = new Event[20];
    private int[] PPVEventSingleViewPrices = new int[20];
    private int totalAmountCollected = 0;
    private int monthlyAmountCollected = 0;
    private int previousMonthlyAmountCollected = 0;
    private int totalAmountPaid = 0;
    private int monthlyAmountPaid = 0;
    private int previousMonthlyAmountPaid = 0;
    private String lastDateBought;



    //method definitions

    StreamingService(String sName, String lName, int price){
        shortName = sName;
        longName = lName;
        flatRateSubscriptionPrice = price;
    }//end of constructor class

    public void buyEventFromStudio(Event movieName, int movieYear, Studio studioName, String eventType){
        int n = 0;
//        System.out.println("HERE");
//        System.out.println(studioName.getEventsOffered());
//        System.out.println(studioName.getEventsOffered()[0]);

        for(int i = 0;i<studioName.getEventsOffered().length;i++){
            if(studioName.getEventsOffered()[i]!= null){
                if(studioName.getEventsOffered()[i].equals(movieName)){
                    //System.out.println(studioName.getEventsOffered()[i].getEventName());
                    n++;
                    break;

                }

            }

        }//check to see if event is offered by studio


        if(n>0){

            if(eventType.toLowerCase()=="movie"){


                int j = 0;
                int q = 0;
                for(int i = 0; i<directoryOfMovieEvents.length;i++){
                    if(directoryOfMovieEvents[i]==movieName){
                        j++;
                    }
                }//end of for loop checking if service already bought movie

                for(int k = 0; k<directoryOfPPVEvents.length;k++){
                    if(directoryOfPPVEvents[k]==movieName){
                        q++;
                    }
                }

                if(j!= 0){

                    System.out.println("Streaming Service already offers this Movie Event");
                    }//Streaming Service already has movie

                else if (q!=0){

                    for(int k = 0; k<20;k++){
                        if(directoryOfMovieEvents[k]==null){
                            directoryOfMovieEvents[k]= movieName;
                            numOfMoviesOffered +=1;
                            break;
                        }
                        else{

                        }
                    }
                }//this means the streaming service currently offers this movie as a ppv event


            else{

                //charge the Streaming Service
                //totalAmountPaid += studioName.getLicensingPrice(movieName);
                monthlyAmountPaid += studioName.getLicensingPrice(movieName);
                studioName.addMonthlyAmountCollected(studioName.getLicensingPrice(movieName));
                //studioName.addTotalAmountCollected(studioName.getLicensingPrice(movieName));

                for(int k = 0; k<20;k++){
                    if(directoryOfMovieEvents[k]==null){
                        directoryOfMovieEvents[k]= movieName;
                        numOfMoviesOffered +=1;
                        break;
                    }
                    else{

                    }
                }

            }//if the streaming service does not have movie, add movie to directory of movie events, increase numOfMoviesOffered, and add licensing price



            }//buying movie event from studio



            else if(eventType.toLowerCase()=="ppv"){

                int j = 0;
                int q = 0;
                for(int i = 0; i<directoryOfPPVEvents.length;i++){
                    if(directoryOfPPVEvents[i]==movieName){
                        j++;
                    }
                }//end of for loop checking if service already bought ppv event

                for(int k = 0; k<directoryOfMovieEvents.length;k++){
                    if(directoryOfMovieEvents[k]==movieName){
                        q++;
                    }
                }
                if(j!= 0){

                    System.out.println("Streaming Service already offers this Pay-Per-View Event");

                }//Streaming Service already has ppv event

                else if(q!=0){
                    for(int k = 0; k<20;k++){
                        if(directoryOfPPVEvents[k]==null){
                            directoryOfPPVEvents[k]= movieName;
                            numOfPPVOffered +=1;
                            break;
                        }
                        else{

                        }
                    }

                }//this means the event is currently offered as a movie by the streaming service, but not as a ppv event

                else{

                    //charge the Streaming Service
                    //totalAmountPaid += studioName.getLicensingPrice(movieName);
                    monthlyAmountPaid += studioName.getLicensingPrice(movieName);
                    studioName.addMonthlyAmountCollected(studioName.getLicensingPrice(movieName));
                    //studioName.addTotalAmountCollected(studioName.getLicensingPrice(movieName));

                    for(int k = 0; k<20;k++){
                        if(directoryOfPPVEvents[k]==null){
                            directoryOfPPVEvents[k]= movieName;
                            numOfPPVOffered +=1;
                            break;
                        }
                        else{

                        }
                    }

                }//if the streaming service does not have movie, add movie to directory of movie events, increase numOfMoviesOffered, and add licensing price


            }//buying PPV event from studio

        }//this means that the studio offered the event

        else{
            System.out.println("Event not offered by Studio");
        }//this means the studio does not offer the event

    }//end of buyEventFromStudio Method


    public Event[] getDirectoryOfMovieEvents(){
        return directoryOfMovieEvents;
    }//end of getDirectoryOfMovieEvents array

    public Event[] getDirectoryOfPPVEvents(){
        return directoryOfPPVEvents;
    }//end of getDirectoryOfPPCEvents array

    public void viewDirectoryOfMovieEvents(){
        for(int i = 0;i<directoryOfMovieEvents.length;i++){
            if(directoryOfMovieEvents[i]!=null){
                System.out.println(directoryOfMovieEvents[i].getEventName()+"-"+directoryOfMovieEvents[i].getYearProduced());
            }
            else{
                break;
            }
        }
    }//end of getDirectoryOfMovieEvents array

    public void viewDirectoryOfPPVEvents(){
        for(int i = 0;i<directoryOfPPVEvents.length;i++){
            if(directoryOfPPVEvents[i]!=null){
                System.out.println(directoryOfPPVEvents[i].getEventName()+"-"+directoryOfPPVEvents[i].getYearProduced());
            }
            else{
                break;
            }
        }
    }//end of getDirectoryOfPPCEvents array


    public int getFlatRateSubscriptionPrice(){
        return flatRateSubscriptionPrice;
    }//end of getFlatRateSubscriptionPrice method

    public void setFlatRateSubscriptionPrice(int price){
        flatRateSubscriptionPrice=price;
    }//end of setFlatRateSubscriptionPrice

    public int getSingleViewPrice(Event movieName){

        int n=-1;
        for(int i=0;i<directoryOfPPVEvents.length;i++){
            if(directoryOfPPVEvents[i]==movieName){
                n=i;
                break;
            }
        }//look through directoryOfPPVEvents array and get index of Event movieName

        if(n==-1){
            System.out.println("PPV event not offered");
            return 0;
        }//if movieName was not found
        else{
          return  PPVEventSingleViewPrices[n];
        }//return PPVEventSingleViewPrices at determined index


    }//end of getSingleViewPrice method

    public void setSingleViewPrice(Event movieName, int movieYear, int price){

        int n=-1;
        for(int i=0;i<directoryOfPPVEvents.length;i++){
            if(directoryOfPPVEvents[i]==movieName){
                n=i;
                break;
            }
        }//look through directoryOfPPVEvents array and get index of Event movieName

        if(n==-1){
            System.out.println("PPV event not offered");
        }//if movieName was not found
        else{
            PPVEventSingleViewPrices[n]=price;
        }//set PPVEventSingleViewPrices at determined index

    }//end of setSingleViewPrice method

    public void setShortName(String sName){
        shortName = sName;
    }//end of setShortName method

    public String getShortName(){
        return shortName;
    }//end of getShortName method

    public void setLongName(String lName){
        longName = lName;
    }//end of setLongName method

    public String getLongName(){
        return longName;
    }//end of getLongName method

    public int getTotalAmountCollected(){

        return totalAmountCollected;
    }//end of getTotalAmountCollected method

    public void setTotalAmountCollected(int price){
        totalAmountCollected = price;
    }

    public void addTotalAmountCollected(int cost){

        totalAmountCollected +=cost;
    }//end of addTotalAmountCollected method

    public int getMonthlyAmountCollected(){
        return monthlyAmountCollected;
    }//end of getMonthlyAmountCollected method

    public void setMonthlyAmountCollected(int price){
        monthlyAmountCollected = price;
    }//end of setMonthlyAmountCollected method

    public void addMonthlyAmountCollected(int price){

        monthlyAmountCollected += price;
    }//end of addMonthlyAmountCollected method

    public int getPreviousMonthlyAmountCollected(){
        return previousMonthlyAmountCollected;
    }//end of getPreviousMonthlyAmountCollected method

    public void setPreviousMonthlyAmountCollected(int price){
        previousMonthlyAmountCollected = price;
    }//end of setPreviousMonthlyAmountCollected


    public int getTotalAmountPaid(){
        return totalAmountPaid;
    }//end of getTotalAmountPaid method


    public int getMonthlyAmountPaid(){
        return monthlyAmountPaid;
    }//end of getMonthlyAmountPaid method

    public void setMonthlyAmountPaid(int price){
        monthlyAmountPaid = price;

    }//end of setMonthlyAmountPaid method

    public int getPreviousMonthlyAmountPaid(){
        return previousMonthlyAmountPaid;
    }//end of getPreviousMonthlyAmountPaid method

    public void setPreviousMonthlyAmountPaid(int price){
        previousMonthlyAmountPaid = price;
    }//end of setPreviousMonthlyAmountPaid method

}// end of StreamingService class
