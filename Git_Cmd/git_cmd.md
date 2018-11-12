# CMD
* Move file
```move source/filename destination/filename```
# BASH
* Current working directory
```
pwd
```
* Change directory to home directory
```
cd ~
```
* Delete A File
```
rm -i MyFile.rtf MyCV.rtf MyGreatAmericanNovel.rtf
```
* Delete A Folder (Delete recursively to the base_file)
```
rm -R folder
```
* Delete An Empty Folder
```
rmdir folder
```
* List all items including the hiddens in the repository
```ls -la```
---
<p align="center">
  <img width="460" height="450" src="https://i.stack.imgur.com/caci5.png">
</p>

# GIT
* Set username and email 
```
git config –global user.name “name”
git config –global user.email “email”
```
* Show username and email
```
git config user.name
git config user.email
```
* Show help 
```
git help ../commit/add/... 
```
* Create a local repository
```
git init
git clone url
```
* Initial push 
```
git push origin master 
```
* Show all of commits
```
git log
```
* Show Commits by author
```
git log --author="name"
```
* Show all changes to files in the **Working Area** vs **Local Committed Repo**
* **not committed yet**/the saved file is different from **Local Repo**
* If files added to **Staging Area**, no comparison
```
git diff
```
* Comparing files of **Staging Area** to **Committed Local Repo**
```
git diff --staged
```
* Delete file from **Working Area** but not **committed** 
```
git rm <file>
```
* rename file
```
git mv second.txt pudding.txt
```
* Move file into folder and change the name
```
git mv pudding.txt LoveNote/patty.txt 
```
