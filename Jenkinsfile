node {

     stage (" BUILD "){
            
             stage("Code Checkout"){
               
                 checkout scm
             }
          
            stage("Latest Changes Pushed "){
                sh " git log -5 "
            }
     }
}
