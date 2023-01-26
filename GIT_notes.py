# HELP
git add --help

# MANUAL
man git

# STATUS
git status # check current status

# display files and folders
ls
ls -la

# LOG
git log
git log --online
git log --oneline --decorate --graph --all

# create Repo
git init

# clone repo
git clone <url>

# Add file to Stage
git add .   # add ALL files

git commit
git commit -m "some text for comit"
git commit -a ""


**************** WRONG ****************

# rename from "filename1" to "filename2"
mv filename1 filename2
git add filename1 # confirm delete
git add filename2 # confirm add

# delete
rm filename1
git add filename1 # confirm delete

**************** CORRECT ****************

# rename from "filename1" to "filename2"
git mv filename1 filename2

# delete
git rm filename1

# Change commit message and/or add files to the latest commit
git commit --amend
git commit --amend --no-edit          # update commit w/o modifying commit message

# Delete file from commit
git rm <filename>
git commit --amend --no-edit

# new branch
1) 
git branch <new_branch_name>
git checkout <new_branch_name>
2) 
git checkout -b <new_branch_name>