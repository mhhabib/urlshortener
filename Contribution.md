# Contribution
 If you find any bugs, need any suggestion, want to improve or need to implement a new feature then you can contribute.

# How to contribute!

## Steps:
  -  First create an issue in which you want to work upon.
  
  -  Fork the [repository](https://github.com/mhhabib/urlshortener)
  
  -  Clone the fork [repo](https://github.com/mhhabib/urlshortener)
     - git clone https://github.com/<Your_Username>/finiz  
  
  - Add Upstream or the remote of the original project to your local repository

   ```bash
   # check remotes
   git remote -v
   git remote add upstream https://github.com/mhhabib/urlshortener.git
   ```

  - Make sure you update the local repository

   ```bash
   # Get updates
   git fetch upstream
   # switch to master branch
   git checkout master
   # Merge updates to local repository
   git merge upstream/master
   # Push to github repository
   git push origin master
   ```

  - Create a branch locally with a succinct but descriptive name

   ```bash
   git checkout -b branch-name
   ```
  
  -  Add Scripts related to your respective issues.
  ```
     git add <your-contribution>
  ```
 
  -  Add a commit message !
  ```git
     git commit -a -m "<Added your message>"
  ```
  -  Push changes
  ```git
    git push -u origin <name_of_your_branch>
  ```
 
  -  Create pull requests
    - [ Try to Mention the related issue for your PR ]
