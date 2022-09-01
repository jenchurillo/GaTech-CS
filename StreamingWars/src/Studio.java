import java.util.HashMap;
import java.util.HashSet;

public class Studio {

    //attribute declarations

    private String shortName;
    private String longName;
    private Event[] eventsOffered = new Event[20];
    private int[] eventLicensingPrices = new int[20];
    //private HashSet<String> eventsOffered = new HashSet<String>();
    private int totalAmountCollected = 0;
    private int monthlyAmountCollected = 0;
    private int previousMonthAmountCollected = 0;
    //private String[][] licensingPrice;
    //private HashMap<String,Double> licensingPrice = new HashMap<String, Double>();


    //method definitions

    Studio(String sName, String lName){
        shortName = sName;
        longName = lName;
    }//end of constructor class

    public void viewEventsOffered(){
        for(int i = 0;i<getEventsOffered().length;i++){
            if(getEventsOffered()[i]!=null){
                System.out.println(getEventsOffered()[i].getEventName()+"-"+getEventsOffered()[i].getYearProduced());
            }
            else{
                break;
            }
        }
    }

    public void addEventOffered(Event movieTitle){
        for(int i = 0;i<eventsOffered.length;i++){
            if(eventsOffered[i]==null){
                eventsOffered[i]=movieTitle;
                break;
            }
            else{

            }
        }

    }//end of addEventOffered method

    public Event[] getEventsOffered(){

        return eventsOffered;
    }//end of getEventsOffered method

    public void setLicensingPrice(Event movieTitle, int yearProduced, int price){

        //set the licensing fee in the event class
        movieTitle.setEventLicensingFee(price);

        //set the licensing fee in the studio class
        int n=-1;
        for(int i=0;i<eventsOffered.length;i++){
            if(eventsOffered[i]==movieTitle){
                n=i;
                break;
            }
        }//look through eventsOffered array and get index of Event movieTitle

        if(n==-1){
            System.out.println("event not offered");
        }//if movieName was not found
        else{
            eventLicensingPrices[n]=price;
        }//set PPVEventSingleViewPrices at determined index

    }//end of setLicensingPrice method

    public int getLicensingPrice(Event movieTitle){

        int n=-1;
        for(int i=0;i<eventsOffered.length;i++){
            if(eventsOffered[i]==movieTitle){
                n=i;
                break;
            }
        }//look through eventsOffered array and get index of Event movieTitle

        if(n==-1){
            System.out.println("Event not offered");
            return 0;
        }//if movieName was not found
        else{
            return movieTitle.getEventLicensingFee();
            //return  eventLicensingPrices[n];
        }//return PPVEventSingleViewPrices at determined index

    }//end of getLicensingPrice method


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

    public int getMonthlyAmountCollected(){
        return monthlyAmountCollected;
    }//end of getMonthlyAmountCollected method

    public void setMonthlyAmountCollected(int price){
        monthlyAmountCollected = price;
    }//end of setMonthlyAmountCollected method

    public int getPreviousMonthAmountCollected(){
        return previousMonthAmountCollected;
    }//end of getPreviousMonthlyAmountCollected

    public void setPreviousMonthAmountCollected(int price){
        previousMonthAmountCollected = price;
    }//end of setPreviousMonthlyAmountCollected method

    public void addTotalAmountCollected(int cost){
        totalAmountCollected += cost;
    }//end of addTotalAmountCollected method

    public void addMonthlyAmountCollected(int cost){
        monthlyAmountCollected += cost;
    }//end of addMonthlyAmountCollected method





}//end of Studio class
