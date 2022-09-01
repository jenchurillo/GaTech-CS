public class Event {

    //attribute declarations
    private String eventType;
    private String eventName;
    private String eventStudioShortName;
    private int eventYear;
    private int eventDuration;
    private int eventLicensingFee;
    private String eventGenre;
    private String[] generes;



    //method definitions

    Event(String type, String name, int year, int duration, String studioName, int fee){
        eventType = type;
        eventName = name;
        eventYear = year;
        eventDuration = duration;
        eventStudioShortName = studioName;
        eventLicensingFee = fee;
    }//end of constructor class

    public void createNewGenre(String genre){

    }//end of createNewGenre method

    public void setEventType(String type){
        eventType = type;
    }//end of setEventType Method

    public String getEventType(){
        return eventType;
    }//end of getEventType method

    public void setEventName(String name){
        eventName = name;
    }//end of setEventName method

    public String getEventName(){
        return eventName;
    }//end of getEventName method

    public void setEventDuration(int duration){
        eventDuration = duration;
    }//end of setEventDuration method

    public int getEventDuration(){
        return eventDuration;
    }//end of getEventDuration method

    public void setYearProduced(int year){
        eventYear = year;
    }//end of setYearProduced method

    public int getYearProduced(){
        return eventYear;
    }//end of getYearProduced method

    public void setEventGenre(String genre){
        eventGenre = genre;
    }//end of setEventGenre method

    public String getEventGenre(){
        return eventGenre;
    }//end of getEventGenre method

    public void setEventStudio(String studioName){
        eventStudioShortName = studioName;
    }//end of setEventStudio method

    public String getEventStudio(){
        return eventStudioShortName;
    }//end of getEventStudio method

    public void setEventLicensingFee(int fee){
        eventLicensingFee=fee;
    }//end of setEventLicensingFee method

    public int getEventLicensingFee(){
        return eventLicensingFee;
    }//end of getEventLicensingFee method






}//end of Event class
