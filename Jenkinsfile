node("Django-Node") {

     MESG="TEST CODE GOES HERE"

     stage (" CHECKOUT AND TEST "){
            
             stage("Code Checkout"){
               
                 checkout scm
             }
          
            stage("Latest Changes Pushed "){
                sh " git log -5 "
            }
     }
  
    stage (" TEST " ){
    
           sh "echo ${MESG} "
 
   }


    stage(" BUILD IMAGE AND PUSH TO REGISTRY "){

         sh "docker build -t cidemo:${BRANCH_NAME}_${env.BUILD_NUMBER} ." 

    }

   
     
     
}
