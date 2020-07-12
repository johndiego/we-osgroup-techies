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
  
         stage("IMAGE BUILD"){

         sh "docker build -t cidemo:${BRANCH_NAME}_${env.BUILD_NUMBER} ." 
        
        }

        stage("IMAGE TAGGING"){

        sh "docker tag  cidemo:${BRANCH}_${env.BUILD_NUMBER} osgroupgeeks/cidemo:${BRANCH}_${env.BUILD_NUMBER}"

        }

        stage ("DOCKER HUB LOGIN AND PUSH "){
     
        dir("/opt"){

          sh "docker login "

          sh "docker push osgroupgeeks/cidemo:${BRANCH}_${env.BUILD_NUMBER}"
         }

         }

    }

   
     
     
}
