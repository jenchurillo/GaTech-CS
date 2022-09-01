import java.beans.DesignMode;
import java.util.Scanner;

public class Main {
    public static void main(String[] args){




    Scanner commandLineInput = new Scanner(System.in);
    String wholeInputLine;
    String[] tokens;
    final String DELIMITER = ",";
    DemographicGroup[] demoGroup = new DemographicGroup[10];
    Studio[] studios = new Studio[10];
    Event[] events = new Event[20];
    StreamingService[] services = new StreamingService[10];
    int currentMonth = 10;
    int currentYear = 2020;


        while(true) {

        wholeInputLine = commandLineInput.nextLine();
        tokens = wholeInputLine.split(DELIMITER);


        if (tokens[0].equals("create_demo")) {
            System.out.println("> "+tokens[0]+","+tokens[1]+","+tokens[2]+","+tokens[3]);
            String demoShortName = tokens[1];
            String demoLongName = tokens[2];
            int numOfAccounts = Integer.parseInt(tokens[3]);

            for (int i = 0; i < 10; i++) {
                if (demoGroup[i] == null) {
                    demoGroup[i] = new DemographicGroup(demoShortName, demoLongName, numOfAccounts);
                    break;
                } else {

                }
            }


        }//end of create_demo command

        else if (tokens[0].equals("create_studio")){
            System.out.println("> "+tokens[0]+","+tokens[1]+","+tokens[2]);
            String studioShortName = tokens[1];
            String studioLongName = tokens[2];

            for (int i = 0; i < 10; i++) {
                if (studios[i] == null) {
                    studios[i] = new Studio(studioShortName, studioLongName);
                    break;
                } else {

                }
            }


        }//end of create_studio command

        else if (tokens[0].equals("create_event")){
            System.out.println("> "+tokens[0]+","+tokens[1]+","+tokens[2]+","+tokens[3]+","+tokens[4]+","+tokens[5]+","+tokens[6]);
            String eventType = tokens[1];
            String eventName = tokens[2];
            int eventYear = Integer.parseInt(tokens[3]);
            int eventDuration = Integer.parseInt(tokens[4]);
            String studioName = tokens[5];
            int fee = Integer.parseInt(tokens[6]);
            Studio studio = null;
            Event movie = null;

            for(int i = 0; i<studios.length;i++){
                if(studios[i].getShortName().equals(studioName)){
                    studio = studios[i];
                    break;
                }
            }//get event studio object


            for (int i = 0; i < 10; i++) {
                if (events[i] == null) {
                    events[i] = new Event(eventType, eventName, eventYear, eventDuration, studioName, fee);
                    studio.addEventOffered(events[i]);
                    //System.out.println(studio.getEventsOffered());
                    //System.out.println("HERE");
                    //System.out.println(events[i].getEventName());
                    break;
                } else {

                }
            }



        }//end of create_event command


        else if (tokens[0].equals("create_stream")){
            System.out.println("> "+tokens[0]+","+tokens[1]+","+tokens[2]+","+tokens[3]);
            String shortName = tokens[1];
            String longName = tokens[2];
            int serviceFee = Integer.parseInt(tokens[3]);

            for (int i = 0; i < 10; i++) {
                if (services[i] == null) {
                    services[i] = new StreamingService(shortName, longName, serviceFee);
                    break;
                } else {

                }
            }


        }//end of create_stream command

        else if (tokens[0].equals("display_demo")){
            System.out.println("> "+tokens[0]+","+tokens[1]);

            String shortName = tokens[1];

            for(int i = 0; i<demoGroup.length; i++){
                if(demoGroup[i].getShortName().equals(shortName)){
                    System.out.println("demo,"+demoGroup[i].getShortName()+","+demoGroup[i].getLongName());
                    System.out.println("size,"+demoGroup[i].getNumOfAccounts());
                    System.out.println("current_period,"+demoGroup[i].getCurrentMonthlyCost());
                    System.out.println("previous_period,"+demoGroup[i].getPreviousMonthlyCost());
                    System.out.println("total,"+demoGroup[i].getTotalCost());
                    break;
                }
                else{

                }

            }

        }//end of display_demo command

        else if (tokens[0].equals("display_studio")){
            System.out.println("> "+tokens[0]+","+tokens[1]);
            String shortName = tokens[1];


            for(int i = 0; i<studios.length; i++){
                if(studios[i].getShortName().equals(shortName)){
                    System.out.println("studio,"+studios[i].getShortName()+","+studios[i].getLongName());
                    System.out.println("current_period,"+studios[i].getMonthlyAmountCollected());
                    System.out.println("previous_period,"+studios[i].getPreviousMonthAmountCollected());
                    System.out.println("total,"+studios[i].getTotalAmountCollected());
                    break;
                }
                else{

                }

            }

        }//end of display_studio command

        else if (tokens[0].equals("display_stream")){
            System.out.println("> "+tokens[0]+","+tokens[1]);
            String shortName = tokens[1];

            for(int i = 0; i<services.length; i++){
                if(services[i].getShortName().equals(shortName)){
                    System.out.println("stream,"+services[i].getShortName()+","+services[i].getLongName());
                    System.out.println("subscription,"+services[i].getFlatRateSubscriptionPrice());
                    System.out.println("current_period,"+services[i].getMonthlyAmountCollected());
                    System.out.println("previous_period,"+services[i].getPreviousMonthlyAmountCollected());
                    System.out.println("total,"+services[i].getTotalAmountCollected());
                    System.out.println("licensing,"+services[i].getMonthlyAmountPaid());
                    break;
                }
                else{

                }

            }

        }//end of display_stream command

        else if (tokens[0].equals("offer_movie")){
            System.out.println("> "+tokens[0]+","+tokens[1]+","+tokens[2]+","+tokens[3]);
            String shortName = tokens[1];
            String movieName = tokens[2];
            int movieYear = Integer.parseInt(tokens[3]);


            //String movieStudioShortName = tokens[1];
            String movieStudioShortName = "";
            Studio movieStudio = null;
            StreamingService service = null;
            Event movie = null;

//            System.out.println(events[0].getEventName());
//            System.out.println(events[0].getYearProduced());



            for(int i = 0;i<events.length;i++){

                if(events[i]!=null){

//                    System.out.println(events[i].getEventName());
//                    System.out.println(events[i].getYearProduced());
//                    System.out.println(movieName);
//                    System.out.println(movieYear);


                if(events[i].getEventName().toLowerCase().equals(movieName.toLowerCase())&&events[i].getYearProduced()==movieYear){
                    //events[i].getEventName().equals(movieName)&&
                    //movieStudioShortName = events[i].getEventStudio();
                    //System.out.println("name and year equal");
                    movie = events[i];
                    movieStudioShortName = events[i].getEventStudio();
                    break;
                }

                }
            }//get event object and get event studio short name


            for(int i=0;i<studios.length;i++){
                if(studios[i]!=null) {
                    // System.out.println(movieStudio.getShortName());
                    if (studios[i].getShortName().equals(movieStudioShortName)) {
                        movieStudio = studios[i];
                        break;
                    }

                }

            }//get studio object

            for(int i = 0;i<services.length;i++){
                if(services[i]!=null) {
                    if (services[i].getShortName().equals(shortName)) {
                        service = services[i];
                        break;
                    }
                }
            }//get StreamingService object




//            System.out.println(movie);
//            System.out.println(movie.getEventName());
//            System.out.println(movieYear);
//            System.out.println(movieStudio);
//            System.out.println(movieStudio.getShortName());



            service.buyEventFromStudio(movie, movieYear, movieStudio, "movie" );

        }//end of offer_movie command


        else if (tokens[0].equals("offer_ppv")){
            System.out.println("> "+tokens[0]+","+tokens[1]+","+tokens[2]+","+tokens[3]+","+tokens[4]);
            String shortName = tokens[1];
            String ppvName = tokens[2];
            int ppvYear = Integer.parseInt(tokens[3]);
            int singleViewPrice = Integer.parseInt(tokens[4]);


            //String ppvStudioShortName = tokens[1];
            String ppvStudioName = "";
            Studio ppvStudio = null;
            StreamingService service = null;
            Event ppv = null;


            for(int i = 0;i<events.length;i++) {
                if (events[i] != null) {
                    if (events[i].getEventName().toLowerCase().equals(ppvName.toLowerCase()) && events[i].getYearProduced() == ppvYear) {
                        //ppvStudioShortName = events[i].getEventStudio();
                        ppv = events[i];
                        ppvStudioName = events[i].getEventStudio();
                        break;
                    }
                }//get event object and get event studio name

            }
            for(int i=0;i<studios.length;i++){
                if(studios[i]!=null) {
                    if (studios[i].getShortName().equals(ppvStudioName)) {
                        ppvStudio = studios[i];
                        break;

                    }
                }

            } //get studio object

            for(int i = 0;i<services.length;i++){
                if(services[i]!=null) {
                    if (services[i].getShortName().equals(shortName)) {
                        service = services[i];
                        break;
                    }
                }
            }//get StreamingService object


            service.buyEventFromStudio(ppv, ppvYear, ppvStudio, "ppv" );
            service.setSingleViewPrice(ppv, ppvYear,singleViewPrice );

        }//end of offer_ppv command

        else if(tokens[0].equals("watch_event")){
            System.out.println("> "+tokens[0]+","+tokens[1]+","+tokens[2]+","+tokens[3]+","+tokens[4]+","+tokens[5]);
            String demoShortName = tokens[1];
            int demoPercentage = Integer.parseInt(tokens[2]);
            String serviceShortName = tokens[3];
            String eventShortName = tokens[4];
            int eventYear = Integer.parseInt(tokens[5]);

            Event currentEvent = null;
            StreamingService currentService = null;
            String eventType = "";
            DemographicGroup currentGroup = null;

            for(int i = 0;i<demoGroup.length;i++){
                if(demoGroup[i]!=null){
                    if(demoGroup[i].getShortName().toLowerCase().equals(demoShortName.toLowerCase())){
                        currentGroup = demoGroup[i];
                    }
                }
            }

            for(int j = 0;j<events.length;j++){
                if(events[j]!=null){
                    if(events[j].getEventName().toLowerCase().equals(eventShortName.toLowerCase())&&events[j].getYearProduced()==eventYear){
                        currentEvent = events[j];
                        eventType = events[j].getEventType();
                    }
                }
            }//get Event object and Event Type

            for(int k = 0;k<services.length;k++){
                if(services[k]!=null) {
                    if (services[k].getShortName().toLowerCase().equals(serviceShortName.toLowerCase())) {

                        currentService = services[k];
                    }
                }
            }//get StreamingService object

//            System.out.println(currentEvent.getEventName());
//            System.out.println(eventYear);
//            System.out.println(currentService.getShortName());
//            System.out.println(serviceShortName);
//            System.out.println(eventType);



           currentGroup.watchEvent(currentEvent, eventYear, currentService, eventType, demoPercentage);


        }//end of watch_event command

        else if(tokens[0].equals("display_time")){
            System.out.println("> "+tokens[0]);

            System.out.println("time,"+currentMonth+","+currentYear);

        }//end of display_time command

        else if(tokens[0].equals("next_month")){
            System.out.println("> "+tokens[0]);

            if(currentMonth==12){
                currentMonth = 1;
                currentYear += 1;
            }
            else{
                currentMonth +=1;
            }

            for(int i = 0;i<studios.length;i++){
                if(studios[i]!=null){
                    studios[i].setPreviousMonthAmountCollected(studios[i].getMonthlyAmountCollected());
                    studios[i].setTotalAmountCollected(studios[i].getTotalAmountCollected()+studios[i].getMonthlyAmountCollected());
                    studios[i].setMonthlyAmountCollected(0);
                }

            }//circle through all studios and re-set amount collected

            for(int k = 0;k<services.length;k++){
                if(services[k]!=null){
                    services[k].setPreviousMonthlyAmountCollected(services[k].getMonthlyAmountCollected());
                    services[k].setTotalAmountCollected(services[k].getTotalAmountCollected()+services[k].getMonthlyAmountCollected());
                    services[k].setPreviousMonthlyAmountPaid(services[k].getMonthlyAmountPaid());
                    services[k].setMonthlyAmountCollected(0);
                    //services[k].setMonthlyAmountPaid(0);

                }

            }//circle through all services and re-set amount collected and paid

            for(int a = 0;a<demoGroup.length;a++){
                if(demoGroup[a]!=null){
                    demoGroup[a].setPreviousMonthlyCost(demoGroup[a].getCurrentMonthlyCost());
                    demoGroup[a].setTotalCost(demoGroup[a].getTotalCost()+demoGroup[a].getCurrentMonthlyCost());
                    demoGroup[a].setCurrentMonthlyCost(0);

                    for(int b=0;b<demoGroup[a].getSubscriptions().length;b++){
                        demoGroup[a].getSubscriptions()[b]=null;

                    }

                    for(int c=0;c<demoGroup[a].getSubscriptionsPercent().length;c++){
                        demoGroup[a].getSubscriptionsPercent()[c]=0;
                    }

                    for(int d=0;d<demoGroup[a].viewViewedPPV().length;d++){
                        demoGroup[a].viewViewedPPV()[d]=null;
                    }

                    for(int e=0;e>demoGroup[a].getWatchedPPVPercent().length;e++){
                        demoGroup[a].getWatchedPPVPercent()[e]=0;
                    }

                    for(int f=0;f<demoGroup[a].viewViewedMovies().length;f++){
                        demoGroup[a].viewViewedMovies()[f]=null;
                    }
                }

            }//circle through all demo groups and re-set amount paid
            


        }//end of next_month command

        else if(tokens[0].equals("display_events")){

            System.out.println("> "+tokens[0]);

            for(int i = 0;i<events.length;i++){
                if(events[i]!= null){
                    System.out.println(events[i].getEventType()+","+events[i].getEventName()+","+events[i].getYearProduced()+","+events[i].getEventDuration()+","+events[i].getEventStudio()+","+events[i].getEventLicensingFee());
                }
            }

        }//end of display_event command


        else if(tokens[0].equals("display_offers")){

            //circle through streamingService array
                //circle through directory of events for each streaming service
            System.out.println("> "+tokens[0]);

//            for(int i = 0;i<events.length;i++){
//                if(events[i]!=null){
//                    System.out.println(events[i].getEventStudio()+","+events[i].getEventType()+","+events[i].getEventName()+","+events[i].getYearProduced());
//                }
//            }

            for(int i = 0;i<services.length;i++){
                if(services[i]!=null){
                    for(int k = 0;k<services[i].getDirectoryOfMovieEvents().length;k++){
                        if(services[i].getDirectoryOfMovieEvents()[k]!=null){
                            System.out.println(services[i].getShortName()+","+"movie,"+services[i].getDirectoryOfMovieEvents()[k].getEventName()+","+services[i].getDirectoryOfMovieEvents()[k].getYearProduced());

                        }
                    }//circle through movie events for service

                    for(int k = 0;k<services[i].getDirectoryOfPPVEvents().length;k++){
                        if(services[i].getDirectoryOfPPVEvents()[k]!=null){
                            int singleViewPrice = services[i].getSingleViewPrice(services[i].getDirectoryOfPPVEvents()[k]);
                            System.out.println(services[i].getShortName()+","+"ppv,"+services[i].getDirectoryOfPPVEvents()[k].getEventName()+","+services[i].getDirectoryOfPPVEvents()[k].getYearProduced()+","+singleViewPrice);

                        }
                    }//circle through ppv events for service
                }
            }//circle through all streaming services
        }

        else if (tokens[0].equals("stop")) {
            System.out.println("> "+tokens[0]);
            //commandLineInput.close();
            System.exit(0);
        }


        }

    }
}
