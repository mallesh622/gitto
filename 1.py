hello this is to check

1. so first we need initialize the git by init (which creates the .git file and makes the folder repository which means it can be trackable )
2. * when we make change to the files (any files in the git ) we can add them by git add .\filename(specific file) or git add .(all the changes done)
3. we can check the history(the commits we have done so far) by git log or git log --oneline(to get it in a line)
4.untracked -->files that git doesn't know of(the ones which we have created but not added) and trackable file -->which git knows of
git add -u will add the changes that been made to a trackable file and adds to staging area.
git add -a add all files to staging area.(trackable & untracked)

checking the remove.item .\new.txt
reset .\filename - to bring the change from staging area to working tree it's called reset
restore ---staged .\filename
git reset --hard removes all the changes from the index tree(staging) and working tree at once
git reset --hard doesn't remove the untracked file
git clean -fd (fd -> force delete)for untracked files.

commit -m "message"
push origin master -u
git log --stat (to know the summary of each commit)

git branch name to create a new branch

git checkout -b name to create and move to that branch

git push -u origin master
