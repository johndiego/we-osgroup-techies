node("Django") {

  try{

    // Declare Variables

    def STAGE_REGISTRY="cideo_stage"
    

    // Stage 1: Get The Code From SCM
    stage("Get The Latest Code") {

      checkout scm

      stage ("Get The Latest Changes") {
        sh ('git log  --pretty=format:"%Cred%an - %ar%n %Cblue %h -%Cgreen %s %n" -n 5')
      }

    }



   // Stage 2: Test The code 
   stage ("Get The Code Tested"){
   
       
      
   }

   // --------------------------------------------------------
   stage("Build The Docker Image and Push To The DockerHub "){

         stage("Building Image "){

         sh "docker build -t cidemo:${BRANCH}_${env.BUILD_NUMBER} ."

        }

        stage("Tagging Image"){

        sh "docker tag  cidemo:${BRANCH}_${env.BUILD_NUMBER} osgroupgeeks/cidemo:${BRANCH}_${env.BUILD_NUMBER}"

        }

        stage ("Docker Login"){

        dir("/opt"){

          sh "docker login"

          sh "docker push osgroupgeeks/cidemo:${BRANCH}_${env.BUILD_NUMBER}"
         }

         }

  }
  }
  catch(err){}
  finally{}
}

