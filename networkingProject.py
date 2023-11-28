#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install azure-cli')



# In[2]:


# Create a virtual environment
get_ipython().system('python -m venv myenv')

# Activate the virtual environment
# On Windows
get_ipython().system('myenv\\Scripts\\activate')


# Install the required packages
get_ipython().system('pip install azure-cosmos==4.5.1')


# In[3]:


get_ipython().system('pip show azure-cosmos')
import sys
print(sys.path)


# In[4]:


get_ipython().run_line_magic('pip', 'install azure-cosmos==4.5.1')


# In[5]:


import azure.cosmos.cosmos_client as cosmos_client
print(cosmos_client.__file__)


# In[6]:


from azure.cosmos import CosmosClient

endpoint = "https://userregistration.documents.azure.com:443/"
key = "aGqLgZfX8rpycetxZI4dbeJJucQWgtMMfyd4ZaiAcVuuTr2Pa09MVuFY7AixuAKjL2cCQjiXZfBdACDba06CoQ=="
client = CosmosClient(endpoint, key)
# Specify the database name
database_name = "userregisterDB"

# Check if the database already exists
existing_databases = list(client.list_databases())
database_exists = any(db['id'] == database_name for db in existing_databases)

# If the database doesn't exist, create it
if not database_exists:
    database = client.create_database(database_name)
    print(f"Database '{database_name}' created successfully.")
else:
    print(f"Database '{database_name}' already exists.")


# In[4]:


from azure.cosmos import CosmosClient
from azure.cosmos.partition_key import PartitionKey



# Your Cosmos DB account endpoint and key
endpoint = "https://userregistration.documents.azure.com:443/"
key = "aGqLgZfX8rpycetxZI4dbeJJucQWgtMMfyd4ZaiAcVuuTr2Pa09MVuFY7AixuAKjL2cCQjiXZfBdACDba06CoQ=="

# Your existing database name
database_name = "userregisterDB"

# Your new container (collection) name
container_name = "userData"

# Create a Cosmos client
client = CosmosClient(endpoint, key)

# Connect to the existing database
database = client.get_database_client(database_name)

# Create a new container with partition key
container = database.create_container_if_not_exists(
    id=container_name,
    partition_key=PartitionKey(path="/username"),
    offer_throughput=400  # You can adjust the throughput based on your needs
)

print(f"Created container '{container_name}'.")


# In[1]:


get_ipython().system('pip install pyngrok')


# In[ ]:


from flask import Flask, render_template, request
import subprocess
import sys

app = Flask(__name__, template_folder=r'C:\Users\colli\Downloads\networking\templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']
    favorite_team = request.form['favorite_team']

    # Your registration logic here

    return f"User {username} registered successfully!"

# Start ngrok tunnel
ngrok_process = subprocess.Popen(["ngrok", "start", "--all", "--config=ngrok.yml"])

try:
    # Run the Flask app
    app.run(port=5000)
except KeyboardInterrupt:
    # Terminate ngrok process when KeyboardInterrupt (Ctrl+C) is detected
    ngrok_process.terminate()
    sys.exit(0)


# In[25]:


get_ipython().run_line_magic('tb', '')

