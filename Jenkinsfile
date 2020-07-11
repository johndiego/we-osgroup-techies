node("Django-Node") {

     stage (" CHECKOUT AND TEST "){
            
             stage("Code Checkout"){
               
                 checkout scm
             }
          
            stage("Latest Changes Pushed "){
                sh " git log -5 "
            }
     }
  
    stage (" TEST " ){
    
           sh "echo "TEST CODE GOES HERE" "
 
   }


    stage(" BUILD IMAGE AND PUSH TO REGISTRY "){

     

    }

   
     
     
}
