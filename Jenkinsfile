pipeline {
    agent any
    stages {
        stage ("cloning the code") {
            steps {
                echo "cloning the code"
                git url: "https://github.com/Azharpasha1996/django-project-001.git", branch: "master"
            }
        }
        stage ("Building the image") {
            steps {
                echo "building the image"
                sh "docker build -t hello-world ."
            }
        }
        stage ("pushing the image to DockerHub") {
            steps {
                echo "pushing image to dockerHub"
                withCredentials ([usernamePassword(credentialsId:"dockerHub",passwordVariable:"dockerHubPass",usernameVariable:"dockerHubUser")]) {
                sh "docker tag hello-world ${env.dockerHubUser}/hello-world:latest"
                sh "docker login -u ${env.dockerHubUser} -p ${env.dockerHubPass}"
                sh "docker push ${env.dockerHubUser}/hello-world:latest"
                }
            }
        }
        stage ("Deploying to server") {
            steps {
                echo "deploying the containers"
                sh "docker run -d -p 80:8000 azharpasha/hello-world:latest"
            }
        }
    }
}
