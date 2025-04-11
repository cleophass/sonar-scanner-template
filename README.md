# 🧪 Python SonarQube Template

This repository serves as a template to perform **static code analysis** on Python projects using **SonarQube** and **SonarScanner**.

## 📂 Project Structure

- Your main Python code should be placed in `main.py`.
- You can also add additional `.py` files in the root directory — they will be analyzed as well.

---

## ⚙️ Setup Instructions

### 1. Edit the `sonar-project.properties` File

Update the following fields in the `sonar-project.properties` file:

```properties
sonar.projectKey=[your-project-key]
sonar.sources=.
sonar.language=py
sonar.host.url=http://localhost:9000
sonar.token=[your-authentication-token]
```

### 2. Get the Required SonarQube Parameters

🔑 **sonar.projectKey**  
Create a new project on your SonarQube dashboard and define the project key during the setup process.

📂 **sonar.sources**  
No change needed — `.` includes all `.py` files in the current directory.

🐍 **sonar.language**  
Keep this as `py` to specify Python.

🌐 **sonar.host.url**  
This should point to your SonarQube instance.  
If you're using SonarQube via Docker, run the following command to get the running container’s port:

```bash
docker ps
```

Look for the container running SonarQube and use the mapped port (default is 9000), e.g.:

```arduino
http://localhost:9000
```

🔐 **sonar.token**  
You can generate a token from your SonarQube user profile:

- Click your profile picture (top right).
- Go to **My Account > Security**.
- Generate a new token and copy it.

### 📥 Install SonarScanner  
To install SonarScanner, follow the official guide:  
👉 [SonarScanner Installation Guide](https://docs.sonarqube.org/latest/analysis/scan/sonarscanner/)

Make sure `sonar-scanner` is available in your system path after installation.

### 🚀 Run the Analysis  
Once everything is configured, run the following command in your terminal:

```bash
sonar-scanner
```
