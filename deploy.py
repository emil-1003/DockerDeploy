import subprocess
import os

def build_and_run_docker(project_path, image_name, container_name, ports):
    try:
        # Build the Docker image
        subprocess.run(["docker", "build", project_path, "-t", image_name], check=True)
        
        # Run the Docker container
        subprocess.run(["docker", "run", "--name", container_name, "-p", ports, "-d", image_name], check=True)
        
        print("Docker container deployed successfully.")
    except subprocess.CalledProcessError as e:
        print("Error:", e)

if __name__ == "__main__":
    project_path = input("Enter the path to the application directory: ")
    image_name = input("Enter the image name: ")
    container_name = input("Enter the container name: ")
    ports = input("Enter the ports (49160:8080): ")

    if not os.path.isdir(project_path):
        print("Invalid project path.")
    else:
        build_and_run_docker(project_path, image_name, container_name, ports)
