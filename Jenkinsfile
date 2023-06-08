// CODE_CHANGES = getGitChanges()
pipeline{
    agent any
    environment {
        NEW_VERSION = '1.3.8'
        // SERVER_CREDENTIALS = credentials('server-credentials')
    }
    stages {
        stage("build"){
            when {
                expression{
                    BRANCH_NAME == 'main' 
 
                }
            }
            steps  {
                echo 'building the application'
                echo "building version ${NEW_VERSION}"
               // echo 'building version ${NEW_VERSION}' // doesnt interpret new_version as variable

            }
        }
        stage("test"){
            // test will execute if branch is main
            when {
                expression{
                    BRANCH_NAME == 'main'
                }
            }
            steps  {
                echo 'testing the application'
            }
        }
        stage("deploy"){
            steps  {
                echo 'deploying the application'
                withCredentials([
                    // creating an object and fetching username and pwd from jenkins credentials and storing in USER and PWD
                    usernamePassword(credentials: 'server-credentials', usernameVariable: USER, passwordVariable: PWD)
                ]){
                    sh "some script ${USER} ${PWD}"
                }
            }
        }
        
    }
    post {
        // always {
        //     //it will be executed irrespective of what happens to the pipeline
        // }
        success{
            echo 'build is successful'
        }
        failure{
            echo 'build failed'
        }
    }


}