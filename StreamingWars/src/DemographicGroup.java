import java.util.HashSet;
import java.util.HashMap;


public class DemographicGroup {

    //attribute declarations

    private String shortName;
    private String longName;
    private int numOfAccounts = 0;
    private int currentMonthlyCost = 0;
    private int previousMonthlyCost = 0;
    private int totalCost = 0;
    private StreamingService[] subscriptions = new StreamingService[10];
    private int subscriptionIndex;
    private int[] subscriptionsPercent = new int[10];
    private int percentSubscribed;

    private Event[] viewedPPV = new Event[20];
    private int watchedPPVIndex;
    private int[] watchedPPVPercent = new int[10];
    private int percentWatched;

    private Event[] viewedMovies = new Event[20];
    private int multiplyPercent;





    //method definitions

    DemographicGroup(String sName, String lName, int accounts){
        shortName = sName;
        longName = lName;
        numOfAccounts = accounts;
    }//end of constructor class

    public void setShortName(String shortDemoName){

        shortName = shortDemoName;
    }//end of setShortName method

    public String getShortName(){

        return shortName;
    }//end of getShortName method

    public void setLongName(String longDemoName){

        longName = longDemoName;
    }//end of setLongName method

    public String getLongName() {
        return longName;
    }//end of getLongName method

    public void createAccount(){

        numOfAccounts+=1;
    }//end of createAccount method

    public void removeAccount(){
        if(numOfAccounts<=0){

        }
        else{
            numOfAccounts-=1;
        }

    }// end of removeAccount method

    public void setNumOfAccounts(int numOfAccount){
        if (numOfAccount<0){
            System.out.println("A demographic group cannot have less than 0 accounts");
        }
        else{
            numOfAccounts=numOfAccount;
        }


    }//end of setNumOfAccounts method

    public int getNumOfAccounts(){

        return numOfAccounts;
    }//end of getNumOfAccounts Method

    public void watchEvent(Event eventName, Integer eventYear, StreamingService serviceName, String eventType, int percentDemo){



        if(eventType.toLowerCase().equals("movie")){

           int m = 0;
           for(int l=0;l<20;l++) {
               //System.out.println("Movie Event");
               if (serviceName.getDirectoryOfMovieEvents()[l] != null) {
                   //System.out.println("YOU ARE HERE");
                   //System.out.println(serviceName.getDirectoryOfMovieEvents()[l].getEventName());
                   if (serviceName.getDirectoryOfMovieEvents()[l].equals(eventName)) {
                      // System.out.println("NOW YOU ARE HERE");
                      // System.out.println("movie is offered");
                       m++;
                   }
               }//check to see if movie is offered buy streaming service
           }
           if(m>0){

               int j = 0;

               for(int i = 0; i<subscriptions.length;i++){
                   if(subscriptions[i]!=null) {
                       if (subscriptions[i] == serviceName) {
                           j++;
                       }
                   }
               }//end of for loop checking if demo group is already subscribed to streaming service

               if(j!= 0){

                   for(int h = 0;h<subscriptions.length;h++){
                       if(subscriptions[h]!=null){
                           if(subscriptions[h] == serviceName){
                               subscriptionIndex = h;
                           }
                       }
                   }




                   for(int k = 0; k<20;k++){
                       if(viewedMovies[k]==null){
                           viewedMovies[k]= eventName;
                           break;
                       }
                       else{

                       }
                   }

                   percentSubscribed = subscriptionsPercent[subscriptionIndex];

                   if(percentSubscribed==percentDemo){
                       multiplyPercent = 0;
                   }
                   else if(percentSubscribed<percentDemo){
                       multiplyPercent = percentDemo - percentSubscribed;
                   }
                   else if(percentSubscribed>percentDemo){
                       multiplyPercent = 0;
                   }

                   if(subscriptionsPercent[subscriptionIndex]<percentDemo){
                       subscriptionsPercent[subscriptionIndex]=percentDemo;
                   }


//                   System.out.println(percentDemo);
//                   System.out.println(percentSubscribed);
//                   System.out.println(multiplyPercent);

                   float cost = (float)((multiplyPercent)*(numOfAccounts))/(100)*(float)(serviceName.getFlatRateSubscriptionPrice());
                   int priceToAdd = (int) cost;

                   currentMonthlyCost += priceToAdd;
                   //totalCost += priceToAdd;
                   //serviceName.addTotalAmountCollected(priceToAdd);
                   serviceName.addMonthlyAmountCollected(priceToAdd);


                   //System.out.println("Movie already subscribed");

               }//if the demographic group is already subscribed, watch movie, add movie to viewedMovies, get past subscription percentage


               else{

                   for(int n = 0; n<10;n++){
                       if(subscriptions[n]==null){
                           subscriptions[n]= serviceName;
                           subscriptionIndex = n;
                           break;
                       }
                       else{

                       }
                   }//add StreamingService to subscription array

                   subscriptionsPercent[subscriptionIndex] = percentDemo;
                   multiplyPercent = percentDemo;

                   for(int k = 0; k<20;k++){
                       if(viewedMovies[k]==null){
                           viewedMovies[k]= eventName;
                           break;
                       }
                       else{

                       }
                   }//add movie to viewMovies array

                   //charge the demographic group
                   //System.out.println(demoPercent);
                   //System.out.println(serviceName.getFlatRateSubscriptionPrice());
                   //System.out.println((float)demoPercent/100);

                   float cost = (float)((multiplyPercent)*(numOfAccounts))/(100)*(float)(serviceName.getFlatRateSubscriptionPrice());
                   int priceToAdd = (int) cost;

                   currentMonthlyCost += priceToAdd;
                   //totalCost += priceToAdd;
                   //serviceName.addTotalAmountCollected(priceToAdd);
                   serviceName.addMonthlyAmountCollected(priceToAdd);

                   //System.out.println("Movie not already subscribed");

               }//if the demographic group is not subscribed, charge the demographic group, add the service to subscriptions and add the movie to viewedMovies

           }//event is offered by streaming service

            else{
                System.out.println("Movie not offered by selected service");
           }//event is not offered by streaming service




        }//end of eventType = movie case

        if(eventType.toLowerCase().equals("ppv")){


            int m = 0;
            for(int l=0;l<20;l++){
                if(serviceName.getDirectoryOfPPVEvents()[l]!=null) {
                    if (serviceName.getDirectoryOfPPVEvents()[l].equals(eventName)) {
                        m++;
                    }
                }
            }//check to see if PPV is offered buy streaming service

            if(m>0){

                int j = 0;
                for(int i = 0; i<viewedPPV.length;i++){
                    if(viewedPPV[i]!=null) {
                        if (viewedPPV[i].equals(eventName)) {
                            j++;
                        }
                    }
                }//end of for loop checking if demo group has already watched

                if(j!=0){


                    percentWatched = watchedPPVPercent[watchedPPVIndex];

                    if(percentWatched==percentDemo){
                        multiplyPercent = 0;
                    }
                    else if(percentWatched<percentDemo){
                        multiplyPercent = percentDemo - percentSubscribed;
                    }
                    else if(percentWatched>percentDemo){
                        multiplyPercent = 0;
                    }

                    if(watchedPPVPercent[watchedPPVIndex]<percentDemo){
                        watchedPPVPercent[watchedPPVIndex]=percentDemo;
                    }



                    float cost = (float)((multiplyPercent)*(numOfAccounts))/(100)*(float)(serviceName.getSingleViewPrice(eventName));
                    int priceToAdd = (int) cost;

                    //charge the demographic group
                    currentMonthlyCost += priceToAdd;
                    // totalCost +=priceToAdd;
                    //serviceName.addTotalAmountCollected(priceToAdd);
                    serviceName.addMonthlyAmountCollected(priceToAdd);

                    //System.out.println("PPV already watched");


                }//if the demoGroup has already watched the movie, they can re-watch for no charge



                else{

                    for(int n = 0; n<20;n++){
                        if(viewedPPV[n]==null){
                            viewedPPV[n]= eventName;
                            watchedPPVPercent[n] = percentDemo;
                            break;
                        }
                        else{

                        }
                    }

//                    System.out.println(percentDemo);
//                    System.out.println(serviceName.getSingleViewPrice(eventName));
//                    System.out.println(numOfAccounts);


                    multiplyPercent = percentDemo;



                    float cost = (float)((multiplyPercent)*(numOfAccounts))/(100)*(float)(serviceName.getSingleViewPrice(eventName));
                    int priceToAdd = (int) cost;

                    //System.out.println(priceToAdd);

                    //charge the demographic group
                    currentMonthlyCost += priceToAdd;
                   // totalCost +=priceToAdd;
                    //serviceName.addTotalAmountCollected(priceToAdd);
                    serviceName.addMonthlyAmountCollected(priceToAdd);


                    //System.out.println("PPV NOT already watched");

                }//if they have not watched the movie, charge the demoGroup, add the movie to viewedPPV
            }//PPV event is offered

            else{
                System.out.println("PPV not offered by selected service.");
            }//PPV event is not offered



        }//end of eventType = ppv case

    }//end of watchEvent method

//    public void watchMovie(Movie movieName, Integer movieYear, StreamingService serviceName){
//
//
//
//        //check subscriptions Hashset to see if the demographic group is already subscribed to the service
//
//            if(subscriptions.contains(serviceName)){
//
//                viewedMovies.put(movieName, movieYear);
//
//            }//if the demographic group is already subscribed, watch movie and add movie to viewedMovies
//
//            else{
//
//                //charge the demographic group
//                currentMonthlyCost += serviceName.getFlatRateSubscriptionPrice();
//                totalCost += serviceName.getFlatRateSubscriptionPrice();
//                serviceName.addTotalAmountCollected(serviceName.getFlatRateSubscriptionPrice());
//                serviceName.addMonthlyAmountCollected(serviceName.getFlatRateSubscriptionPrice());
//
//                subscriptions.add(serviceName);
//                viewedMovies.put(movieName, movieYear);
//
//            }//if the demographic group is not subscribed, charge the demographic group, add the service to subscriptions and add the movie to viewedMovies
//
//
//
//    }//end of watchMovie method

//    public void watchPPV(PPV movieName, Integer movieYear, StreamingService serviceName){
//
//
//        if(viewedPPV.containsKey(movieName)){
//
//        }//if the demoGroup has already watched the movie, they can re-watch for no charge
//
//        else{
//
//            //charge the demographic group
//            currentMonthlyCost += serviceName.getSingleViewPrice(movieName, movieYear);
//            totalCost += serviceName.getSingleViewPrice(movieName, movieYear);
//            serviceName.addTotalAmountCollected(serviceName.getSingleViewPrice(movieName, movieYear));
//            serviceName.addMonthlyAmountCollected(serviceName.getSingleViewPrice(movieName, movieYear));
//
//            viewedPPV.put(movieName, movieYear);
//
//        }//if they have not watched the movie, charge the demoGroup, add the movie to viewedPPV
//
//    }//end of watchPPV method


    public int getCurrentMonthlyCost(){

        return currentMonthlyCost;
    }//end of getCurrentMonthlyCost method

    public void setCurrentMonthlyCost(int price){
        currentMonthlyCost = price;
    }//end of setCurrentMonthlyCost method

    public void setPreviousMonthlyCost(int price){
        previousMonthlyCost = price;
    }//end of setPreviousMonthlyCost method

    public int getPreviousMonthlyCost(){

        return previousMonthlyCost;
    }//end of getPreviousMonthlyCost method

    public int getTotalCost(){

        return totalCost;
    }//end of getTotalCost method

    public void setTotalCost(int price){
        totalCost = price;
    }

    public void viewSubscriptions(){
        for(int i = 0; i<subscriptions.length;i++){
            if(subscriptions[i]!=null) {
                System.out.println(subscriptions[i].getLongName());
            }
            else{
                break;
            }
        }
    }//end of viewSubscriptions method

    public void getViewedMovies(){
        for(int i = 0; i<viewedMovies.length;i++){
            if(viewedMovies[i]!=null){
                System.out.println(viewedMovies[i].getEventName());
            }
            else{
                break;
            }
        }

    }//end of getViewedMovies method

    public void getViewedPPV(){
        for(int i = 0;i<viewedPPV.length;i++){
            if(viewedPPV[i]!=null){
                System.out.println(viewedPPV[i].getEventName());
            }
            else{
                break;
            }
        }
    }//end of getViewedPPV method

    public StreamingService[] getSubscriptions(){
        return subscriptions;
    }//end of getSubscriptions method

    public int[] getSubscriptionsPercent(){
        return subscriptionsPercent;
    }//end of getSubscriptionPercent method

    public Event[] viewViewedPPV(){
        return viewedPPV;
    }//end of viewViewedPPV method

    public Event[] viewViewedMovies(){
        return viewedMovies;
    }//end of viewViewedMovies

    public int[] getWatchedPPVPercent(){
        return watchedPPVPercent;
    }//end of getWatchedPPCPercent method


}// end of DemographicGroup Class
