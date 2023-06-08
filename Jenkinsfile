// CODE_CHANGES = getGitChanges()
pipeline{
    agent any
    stages {
        stage("build"){
            when {
                expression{
                    BRANCH_NAME == 'main' 
 
                }
            }
            steps  {
                echo 'building the application'
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