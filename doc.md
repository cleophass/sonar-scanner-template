# Documentation Sonar - Création de règles personnalisées Python

## Prérequis

### JDK (Java Development Kit)
```bash
sudo apt install openjdk-17-jdk -y
```
**Test :**
```bash
java -version
```

### Docker
Suivez les instructions d'installation :  
👉 [Installation Docker Debian](https://docs.docker.com/engine/install/debian/#install-using-the-repository)

**Test :**
```bash
sudo docker run hello-world
```

### Maven
```bash
sudo apt install maven -y
```
**Test :**
```bash
mvn -v
```

---

## Présentation du projet Creedengo Python

Pour développer des règles personnalisées pour Python dans Sonar, nous utilisons un projet Maven.  
Exemple avec le projet **Creedengo**, mais vous pouvez aussi partir de zéro avec ce [tutoriel officiel](https://docs.sonarsource.com/sonarqube-server/latest/analyzing-source-code/languages/python/#custom-rules).

### Cloner le projet :
```bash
git clone https://github.com/green-code-initiative/creedengo-python.git
cd creedengo-python
code .
```

### Structure du projet :

- **Fichiers de règles Java**  
  `src/main/java/org/greencodeinitiative/creedengo/python/checks/`  
  ![image](assets/image1.png)

- **Métadonnées JSON + HTML pour affichage dans Sonar**  
  `src/main/resources/org/green-code-initiative/rules/python/`  
  ![image](assets/image2.png)

- **Tests Java des règles**  
  `src/test/java/org/greencodeinitiative/creedengo/python/checks/`  
  ![image](assets/image3.png)

- **Fichiers Python pour tests**  
  `src/test/resources/checks/`  
  ![image](assets/image4.png)

Une fois compilées, vos règles seront disponibles dans le dossier `target/` au format `.jar`  
![image](assets/image5.png)

---

## Créer sa première règle

### Étape 1 : Créer la règle Java

- Allez dans :  
  `src/main/java/org/greencodeinitiative/creedengo/python/checks/`
- Copiez une règle existante pour obtenir la structure de base
- Modifiez :
  - `@Rule(key = "GCI99")` → changez l’identifiant
  - La méthode `visitCallExpression` → adaptez la logique

---

### Étape 2 : Ajouter la règle à la liste

- Modifiez ce fichier :  
  `src/main/java/org/greencodeinitiative/creedengo/python/PythonRuleRepository.java`  
  ![image](assets/image6.png)

---

### Étape 3 : Ajouter les tests unitaires

- Allez dans :  
  `src/test/java/org/greencodeinitiative/creedengo/python/checks/`
- Créez une classe de test (ex : `AvoidCSVFormatTest`) en vous basant sur un exemple existant  
  ![image](assets/image7.png)

- Créez un fichier de test Python dans :  
  `src/test/resources/checks/`
  - Ajoutez `# Noncompliant` sur les lignes problématiques  
    ![image](assets/image8.png)

---

### Étape 4 : Lancer les tests

Lancez Maven avec votre classe de test :

```bash
mvn clean test -Dtest=AvoidCSVFormatTest -DtrimStack
```

#### Détails :
- `mvn` : Lance Maven
- `clean` : Nettoie le dossier `target/`
- `test` : Lance les tests
- `-Dtest=...` : Spécifie la classe de test
- `-DtrimStack` : Raccourcit les traces d’erreur

---

### Étape 5 : Ajouter le front (HTML) et les métadonnées (JSON)

#### HTML : `GCI99.html`
Dans `src/main/resources/org/green-code-initiative/rules/python/`

```html
<div class="paragraph">
  <p>Using CSV format for data storage and transfer is less efficient compared to modern formats like Parquet or Feather. These formats save CPU cycles, reduce memory usage, and improve performance.</p>
</div>
<div class="sect1">
  <h2 id="_non_compliant_code_example">Non-compliant Code Example</h2>
  <div class="listingblock">
    <div class="content">
<pre><code data-lang="python">import pandas as pd

df = pd.read_csv('data.csv') # Noncompliant: Use Parquet or Feather format instead
</code></pre>
    </div>
  </div>
</div>
<div class="sect1">
  <h2 id="_compliant_solution">Compliant Solution</h2>
  <div class="listingblock">
    <div class="content">
<pre><code data-lang="python">import pandas as pd

df = pd.read_parquet('data.parquet') # Compliant
# or
df = pd.read_feather('data.feather') # Compliant
</code></pre>
    </div>
  </div>
</div>
```

#### JSON : `GCI99.json`
Même dossier que le HTML.

```json
{
  "title": "Avoid using CSV format",
  "type": "CODE_SMELL",
  "status": "ready",
  "remediation": {
    "func": "Constant/Issue",
    "constantCost": "20min"
  },
  "tags": [
    "eco-design",
    "performance",
    "network",
    "sql",
    "creedengo"
  ],
  "defaultSeverity": "Minor"
}
```

---

### Étape 6 : Compiler le projet

Commandes utiles :
```bash
mvn clean       # Supprime le dossier target
mvn compile     # Compile le code Java
mvn package     # Compile les tests + génère les JARs
```

Lister le contenu d’un JAR :
```bash
jar tf fichier.jar
```

Les `.jar` seront dans `./target/`  
![image](assets/image9.png)

---

### Étape 7 : Lancer Sonar et ajouter la règle

1. Lancer Sonar via Docker :
   ```bash
   ./tool_docker-init.sh
   ```

2. Vérifier le nom du conteneur :
   ```bash
   docker ps
   ```

3. Copier le `.jar` :
   ```bash
   docker cp ./target/creedengo-python-plugin-2.0.2-SNAPSHOT.jar sonar_creedengo_python:/opt/sonarqube/extensions/plugins/
   ```

4. Redémarrer Sonar :
   ```bash
   ./tool_stop.sh
   ./tool_start.sh
   ```

5. Vérifier la présence de la règle dans l'interface Sonar.  
   Sinon, inspectez le JAR :
   ```bash
   jar tf fichier.jar
   ```

---

## Vérification de la règle avec sonar-scanner

Utilisez ce template :  
👉 [sonar-scanner-template](https://github.com/cleophass/sonar-scanner-template)

Suivez les instructions dans le README pour analyser votre code avec vos règles personnalisées.
