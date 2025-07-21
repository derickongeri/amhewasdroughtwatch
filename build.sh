#!/bin/bash

# This script automatically builds the quasar projec, stages, commits and pushes code to a remote repository on Github.
# sphinx-build -M html source/ build/

# #!/bin/bash

langs=(en fr pt ar)

for lang in "${langs[@]}"; do
  echo "Building $lang..."
  SPHINX_LANGUAGE=$lang sphinx-build -b html source build/$lang
done


# Define the remote repository URL
REPO_URL="https://github.com/derickongeri/amhewasdroughtwatch.git"

# Get commit message from command line argument
COMMIT_MESSAGE="$1"

# Check if the commit message was provided
if [ -z "$COMMIT_MESSAGE" ]; then
  echo "Please provide a commit message as an argument."
  exit 1
fi

# Stage changes
echo "Adding files..."
git add .

# Commit changes with the provided commit message
echo "Commiting changes..."
git commit -m "$COMMIT_MESSAGE"

# Push changes to remote repository
echo "Pushhing to github..."
git push $REPO_URL main

