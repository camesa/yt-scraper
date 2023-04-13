<h1>YouTube Search to MongoDB</h1>
<p>This script searches for channels and videos on YouTube based on a specified keyword and saves the results to a MongoDB database.</p>
<h2>Requirements</h2>
<ul>
  <li>Python 3.6 or higher</li>
  <li>Google API client library</li>
  <li>Pymongo library</li>
  <li>dotenv library</li>
  <li>A Google Cloud project with the YouTube Data API enabled and an API key</li>
  <li>A MongoDB Atlas account and a connection string to your database</li>
</ul>
<h2>Usage</h2>
<ol>
  <li>Clone the repository to your local machine.</li>
  <li>Install the required libraries by running the following command in your terminal: <code>pip install -r requirements.txt</code></li>
  <li>Create a <code>.env</code> file in the root directory of the project and add your environment variables:</li>
  <ul>
    <li><code>YOUTUBE_API_KEY</code>: your Google Cloud API key for the YouTube Data API</li>
    <li><code>MONGODB_CONNECTION_STRING</code>: the connection string for your MongoDB database</li>
  </ul>
  <li>Run the script by executing the following command in your terminal: <code>python youtube_search.py</code></li>
  <li>Enter the keyword you want to search for when prompted.</li>
  <li>The script will search for channels and videos related to the keyword on YouTube and save the results to the specified MongoDB database.</li>
</ol> 
