# Using this template app

1. Install the Cloud Foundry CLI if you haven't already:
   ```
   # For Windows (using Chocolatey)
   choco install cloudfoundry-cli

   # For macOS (using Homebrew)
   brew install cloudfoundry/tap/cf-cli@8

   # For Linux (Debian/Ubuntu)
   wget -q -O - https://packages.cloudfoundry.org/debian/cli.cloudfoundry.org.key | sudo apt-key add -
   echo "deb https://packages.cloudfoundry.org/debian stable main" | sudo tee /etc/apt/sources.list.d/cloudfoundry-cli.list
   sudo apt-get update
   sudo apt-get install cf8-cli
   ```

2. Login to your Cloud Foundry instance:
   ```
   cf login -a API_ENDPOINT -u USERNAME -p PASSWORD -o ORGANIZATION -s SPACE
   ```

3. Navigate to your project directory:
   ```
   cd path/to/my-cf-app
   ```

4. Deploy your application:
   ```
   cf push
   ```

5. Check the status of your app:
   ```
   cf apps
   ```

6. View app logs (if needed):
   ```
   cf logs my-python-app --recent
   ```

### Troubleshooting

If your deployment fails, check the logs:
```
cf logs my-python-app --recent
```

Common issues:
- Memory limits: If your app requires more memory, adjust the 'memory' parameter in manifest.yml
- Python version: Make sure your runtime.txt specifies a version supported by Cloud Foundry
- Dependencies: Ensure all required packages are in requirements.txt
- Port binding: Make sure your app binds to the port provided by the PORT environment variable

### Notes
- The app uses Flask for simplicity, but you can use any Python web framework
- Gunicorn is used as the production WSGI server
- The health endpoint can be used for monitoring
- The manifest.yml uses random-route to avoid route conflicts in shared environments