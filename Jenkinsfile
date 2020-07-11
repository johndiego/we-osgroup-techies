node("Django-Node") {

     stage (" BUILD "){
            
             stage("Code Checkout"){
               
                 checkout scm
             }
          
            stage("Latest Changes Pushed "){
                sh " git log -5 "
            }
     }
  
    stage (" TEST " ){
    
           sh "python devops4u/manage.py test devops4u/dsa"
 
   }


     
     
}
